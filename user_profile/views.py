from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import utilities

@api_view(['POST'])
def sign_up(request):
    '''
    gets a mobile number, generates a 4 digit number
    and sends it to the input number.
    request from existing user or a new user.
    '''
    mobile_number = request.data.get('mobile')
    verification_code = "1234"

    print "printing mobile_number"
    print mobile_number

    print "printing verification code"
    print verification_code

    output = utilities.send_sign_up_sms(mobile_number,verification_code)
    print output
    return Response(output)


@api_view(['POST'])
def verify(request):
    '''
    get a mobile number and a code and checks
    if they match.
    '''
    mobile_number = request.data.get('mobile')
    code = request.data.get('code')
    output={}

    if code == "1234":
        output['status'] = "verified"
    else:
        output['status'] = "failed"

    return Response(output)
