
from django.contrib import admin
from django.urls import path,include
from flashcards.api.views import CardList,CardDetail

urlpatterns = [
    path('flashcards/',CardList.as_view(),name='cardlist'),
    path('flashcards/<int:pk>/',CardDetail.as_view(),name='carddetail'),  
]
