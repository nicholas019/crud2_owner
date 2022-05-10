import json

from django.http import JsonResponse
from django.views import View
from owners.models import Owner, Dogs


class OwnerRegister(View):
    def get(self, request):
        result = []
        owner = Owner.objects.all()
        # 쿼리문이기 때문에 바로 response를 하지못한다 그래서 반복문을 통해 딕셔너리형테로 만들어준뒤에 response를 해야한다.
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
        
        # 쿼리문이기 때문에 바로 response를 하지못한다 그래서 반복문을 통해 딕셔너리형테로 만들어준뒤에 response를 해야한다.
        for dogs in dog:
            result.append(
                {
                    'id':dogs.id,
                    'dog_name': dogs.dog_name,
                    'dog_age': dogs.dog_age,
                    'owner_id': dogs.owner.owner_name 
                    # 정참조의경우 .id, .owner_name, .owner_email, .owner_age 다 가능하다.
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

class OwnerList(View):
    def get(self, request):
        result = []
        owner = Owner.objects.all()
        for owners in owner:
            dog = owners.dogs_set.all()
            # 역참조를 할때 _set 사용할땐 models에서 related_name= 속성을 사용할 수 없다.
            # 역참조는 정참조와 다르게 여러개일수 있음으로 모든내역을 다 출력하려면 반복문으로 리스트화시켜서 넣어주고, 
            # 하나만 찝어서 넣고싶다면 범위를 정확하게 지정해줘야한다.
            result1 = []
            for dogs in dog:
                result1.append(
                        {
                            'dog_name': dogs.dog_name,
                            'dog_age': dogs.dog_age,
                        }
                    )    
            result.append(
                {
                    'id':owners.id,
                    'owner_name': owners.owner_name,
                    'owner_email': owners.owner_email,
                    'owner_age': owners.owner_age,
                    'owner_id':result1,
                }
            )
        
        return JsonResponse({'owner_doglist':result}, status=200)        
