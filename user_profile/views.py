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
    #mobile_number = request.data.get('mobile')
    mobile_number = "09128199668"
    verification_code = "1234"

    print "printing mobile_number"
    print mobile_number

    print "printing verification code"
    print verification_code

    output = utilities.send_sign_up_sms(mobile_number,verification_code)
    print output
    return Response(output)


@api_view(['GET'])
def verify(request):
    output = {}
    output['status'] = "True"
    return Response(output)
