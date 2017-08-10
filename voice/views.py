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
    input_from_user = request.GET.get('Digits', '')

    if 'step' not in request.session:
        #New user!

        request.session['step'] = 2
        twil = '''<?xml version="1.0" encoding="UTF-8"?>
                <Response>
                    <Gather timeout="20" method="GET"><Say>Welcome to our hackathon entry. Please enter your favorite number, followed by a pound sign.</Say></Gather>
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
                        <Gather timeout="20" method="GET" numDigits="1"><Say>Your favorite number is ''' + str(request.session['favorite_number']) + '''. Please enter another number, zero to nine.</Say></Gather>
                    </Response>
                    '''
            return HttpResponse(twil, content_type='application/xml', status=200)

        elif current_step == 3:
            if int(input_from_user) >= 0 and int(input_from_user) <= 9:
                twil = '''<?xml version="1.0" encoding="UTF-8"?>
                        <Response>
                            <Say>Thank you. You entered ''' + str(input_from_user) + '''. Goodbye! </Say>
                        </Response>
                        '''
                return HttpResponse(twil, content_type='application/xml', status=200)
            else:
                twil = '''<?xml version="1.0" encoding="UTF-8"?>
                        <Response>
                            <Gather timeout="20" method="GET" numDigits="1"><Say>Sorry, that is not a valid option. Please enter another number, zero to nine. No need to hit the pound sign.</Say></Gather>
                        </Response>
                        '''
                return HttpResponse(twil, content_type='application/xml', status=200)
