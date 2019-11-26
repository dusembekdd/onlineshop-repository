from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def register_api(request):
    serializer = RegistrationSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        account = serializer.save()
        data['Response'] = 'Successfully registered new account.'
        data['email'] = account.email
        data['username'] = account.username
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)