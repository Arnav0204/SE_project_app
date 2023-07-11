from django.contrib.auth.models import User
from flashcards.models import Flashcard
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from flashcards.api.permissions import UserOrReadOnly,AdminOrReadOnly
from  flashcards.models import Flashcard
from flashcards.api.serializers import CardSerializer

class CardList(APIView):
    
    permission_classes = [UserOrReadOnly]
    
    def get(self,request,username):
        card=Flashcard.objects.filter(app_user=request.user)
        serializer=CardSerializer(card,many=True)
        return Response(serializer.data)
            
        
    
    
    def post(self,request,username):
        serializer = CardSerializer(data=request.data)
        user=self.request.user
        if serializer.is_valid():
            serializer.save(app_user=user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
class CardDetail(APIView):
    
    permission_classes = [UserOrReadOnly]
    
    def get(self,request,pk,username):
         try:
             card = Flashcard.objects.get(pk=pk)
             
          
         except Flashcard.DoesNotExist:
              return Response({'error': 'card does not exist'})
             
         serializer = CardSerializer(card)
         return Response(serializer.data)
     
    def put(self,request,pk,username):
        card = Flashcard.objects.get(pk=pk)
        serializer = CardSerializer(card,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk,username):
         card = Flashcard.objects.filter(pk=pk)
         card.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
        
         
        
   
    
        
    
    
    
