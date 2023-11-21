from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import User
import json

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        data = {
            'username': user.username,
            'email': user.email,
        }
        return JsonResponse(data)

    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=data['password'],
        )
        response_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
        return JsonResponse(response_data, status=201)

    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        data = json.loads(request.body)
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)
        user.save()
        response_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
        return JsonResponse(response_data)

    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=204)
