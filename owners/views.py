import json

from django.http import JsonResponse
from django.views import View
from owners.models import Owner, Dogs


class OwnerRegister(View):
    def get(self, request):
        result = []
        owner = Owner.objects.all()
        for owners in owner:
            result.append(
                {
                    'id':owners.id,
                    'owner_name': owners.owner_name,
                    'owner_email': owners.owner_email,
                    'owner_age': owners.owner_age,
                }
            )
        return JsonResponse({'owner':result}, status=200)    

    def post(self, request):
        data = json.loads(request.body)

        owner = Owner(
            owner_name = data['owner_name'],
            owner_email = data['owner_email'],
            owner_age = data['owner_age'])
        owner.save()   

        return JsonResponse({'message': '등록되었습니다'}, status=201)

        
class DogRegister(View):
    def get(self, request):
        result = []
        dog = Dogs.objects.all()
        for dogs in dog:
            result.append(
                {
                    'id':dogs.id,
                    'dog_name': dogs.dog_name,
                    'dog_age': dogs.dog_age,
                    'owner_id': dogs.owner.id,
                }
            )
        return JsonResponse({'dogs':result}, status=200)    

    def post(self, request):
        data = json.loads(request.body)
        owner_name = Owner.objects.get(owner_name=data['owner_name'])
        
        dogs = Dogs(
            dog_name = data['dog_name'],
            dog_age = data['dog_age'],
            owner_id = owner_name.id
            )

        dogs.save()   

        return JsonResponse({'message': '등록되었습니다'}, status=201)

