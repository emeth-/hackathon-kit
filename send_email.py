import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import hackathon.settings
import json
import django
django.setup()

from eemail.views import send_email

subject = "Testing"
from_name = "Frank Sinatra"
from_address = "franksinatra@gmail.com"
message_plaintext = "test plaintext\nNewline"
message_html = "test<b>html</b><br>newline"
reply_to_address = "robertdole@gmail.com"
send_email(subject, from_name, from_address, message_plaintext, message_html, reply_to_address)

