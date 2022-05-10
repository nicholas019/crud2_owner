
from django.urls import path

from owners.views import OwnerRegister, DogRegister

urlpatterns = [
    path("owner", OwnerRegister.as_view()),
    path("dog", DogRegister.as_view()),

]