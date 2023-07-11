from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from rest_framework import status
from user_app import models
from user_app.api.serializers import ResgistrationSerializer

class LoginView(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        response.data['username']=token.user.username
        return Response(response.data)
        
    
    
    
    
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
    
    

@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = ResgistrationSerializer(data=request.data)
        
        data ={}
        
        if serializer.is_valid():
            account=serializer.save()
            data['username']=account.username
            data['email']=account.email
            
            token=Token.objects.get(user=account).key
            data['token']=token
            
        else:
            data=serializer.errors
            
        return Response(data)
            
          
         
        
    
