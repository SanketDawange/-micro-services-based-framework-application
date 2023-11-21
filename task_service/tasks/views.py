from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Task
import json

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        data = {
            'title': task.title,
            'description': task.description,
        }
        return JsonResponse(data)

    def post(self, request):
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data['title'],
            description=data['description'],
        )
        response_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
        }
        return JsonResponse(response_data, status=201)

    def put(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.save()
        response_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
        }
        return JsonResponse(response_data)

    def delete(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=204)
