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
to_address = "myemail@gmail.com"
to_name = "Test Aroo"
send_email(subject, from_address, to_address, message_plaintext, to_name, from_name, message_html)

