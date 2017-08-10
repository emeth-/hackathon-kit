from django.http import HttpResponse
import datetime
import json
from api.models import Fish, Person
from django.db.models import Q
from dateutil import parser
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from custom_decorators import print_errors
import sendgrid
from bs4 import BeautifulSoup, SoupStrainer
import django_rq

def send_email(subject, from_name, from_address, message_plaintext, message_html=None, reply_to_address=None):
    if not reply_to_address:
        reply_to_address = from_address

    if not message_html:
        message_html = message_plaintext

    sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME', ''), os.environ.get('SENDGRID_PASSWORD', ''))

    message = sendgrid.Mail()
    message.add_to(reply_to_address)
    message.set_subject(subject)
    message.set_html(message_html)
    message.set_text(message_plaintext)
    message.set_from(from_name+" <"+from_address+">")
    status, msg = sg.send(message)
    print "EMAIL SENT STATUS", status
    print "EMAIL SENT MSG", msg


@print_errors
def catch_all(request):
    """
        catch_all()
        forward("http://yoursite.com/email/catch_all")
    """
    try:

        print "request.POST", request.POST
        print "request.FILES", request.FILES

        from_address = request.POST['From']
        if type(from_address) is list:
            from_address = from_address[0]

        to_address = request.POST['To']
        if type(to_address) is list:
            to_address = to_address[0]

        reply_to_address = from_address
        try:
            reply_to_address = request.POST.get('Reply-To', '')
            if type(reply_to_address) is list:
                reply_to_address = reply_to_address[0]
        except:
            pass

        try:
            from_address = from_address.split('<')[1].split('>')[0]
        except:
            pass

        try:
            to_address = to_address.split('<')[1].split('>')[0]
        except:
            pass

        try:
            reply_to_address = reply_to_address.split('<')[1].split('>')[0]
        except:
            pass

        print "to_address", to_address
        print "from_address", from_address
        print "reply_to_address", reply_to_address
        print "links in email", extract_links(request.POST['body-html'])
        email_attachment_ids = save_email_attachments(request.FILES)
        print "saving email attachments...", email_attachment_ids

        """
        for attach_id in email_attachment_ids:
            # Execute the binary from the email attachment.
            # Don't actually do this, unless you're building a CTF or something.
            django_rq.enqueue(run_attachment, args=[attach_id], timeout=300)
        """


        if to_address == "bobdole@"+os.environ.get('MAILGUN_DOMAIN', ''):
            if from_address == "tedjones@"+os.environ.get('MAILGUN_DOMAIN', ''):
                pass

def extract_links(email_html):
    links = []
    if type(email_html) is list:
        email_html = email_html[0]
    for link in BeautifulSoup(email_html, "html.parser", parse_only=SoupStrainer('a')):
        print "Found link!", str(link)
        if link.has_attr('href'):
            links.append(link['href'])
    return links

def save_email_attachments(files):
    email_attachment_ids = []
    for k in files:
        nea = EmailAttachment(attachment=files[k].read(), name=k)
        nea.save()
        email_attachment_ids.append(nea.id)
    return email_attachment_ids

def run_attachment(email_attachment_id):
    nea = EmailAttachment.objects.get(pk=email_attachment_id)
    with open('email_attachments/'+nea.name, 'w') as outfile:
        outfile.write(nea.attachment.__str__())
    os.system("chmod +x ./email_attachments/"+nea.name)
    os.system('./email_attachments/'+nea.name)