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

# parser.parse('2000-01-01')
# citation_in_db = Citation.objects.filter(Q(citation_number=potential_citation_number) | Q(drivers_license_number_phone=input_from_user))

@print_errors
def received(request):
    #Automatically reset user's sessions if they haven't communicated in 5 minutes
    if 'last_validated' in request.session:

        session_expiry = (parser.parse(request.session.get('last_validated', '2000-01-01')) + datetime.timedelta(minutes=5))
        if session_expiry < datetime.datetime.now():
            print "Session expired! Session expiry time", session_expiry, " | current time", datetime.datetime.now()
            del request.session['last_validated']
            logout(request)
    else:
        request.session['last_validated'] = datetime.datetime.now().isoformat()

    if 'Body' in request.POST and request.POST['Body'].lower() == "restart":
        # Cheat code for demos, text 'restart' to reset your session without waiting 5 minutes
        logout(request)

    input_from_user = request.POST.get('Body', '')

    if 'step' not in request.session:
        #New user!

        request.session['step'] = 2
        twil = '''<?xml version="1.0" encoding="UTF-8"?>
                <Response>
                    <Message method="GET">Welcome to our hackathon entry. Please enter your favorite number.</Message>
                </Response>
                '''
        return HttpResponse(twil, content_type='application/xml', status=200)
    else:
        #Returning user!

        current_step = request.session['step']
        if current_step == 2:
            request.session['favorite_number'] = input_from_user
            request.session['step'] = 3

            twil = '''<?xml version="1.0" encoding="UTF-8"?>
                    <Response>
                        <Message method="GET">Your favorite number is ''' + str(request.session['favorite_number']) + '''. Please enter another number, zero to nine.</Message>
                    </Response>
                    '''
            return HttpResponse(twil, content_type='application/xml', status=200)

        elif current_step == 3:
            try:
                input_from_user = int(input_from_user)
            except:
                input_from_user = -1 #not a valid number
            if input_from_user >= 0 and input_from_user <= 9:
                twil = '''<?xml version="1.0" encoding="UTF-8"?>
                        <Response>
                            <Message>Thank you. You entered ''' + str(input_from_user) + '''. Goodbye! </Message>
                        </Response>
                        '''
                return HttpResponse(twil, content_type='application/xml', status=200)
            else:
                twil = '''<?xml version="1.0" encoding="UTF-8"?>
                        <Response>
                            <Message method="GET">Sorry, that is not a valid option. Please enter another number, zero to nine.</Message>
                        </Response>
                        '''
                return HttpResponse(twil, content_type='application/xml', status=200)
