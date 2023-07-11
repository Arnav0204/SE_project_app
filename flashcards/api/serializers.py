from flashcards.models import Flashcard
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    app_user = serializers.StringRelatedField()
    class Meta:
        model=Flashcard
        fields=['id', 'title', 'content','app_user']
    
    def create(self,validated_data):
        return Flashcard.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.content=validated_data.get('content',instance.content)
        instance.save()
        return instance
        
