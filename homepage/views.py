from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Project  

def home(request):
    return render(request, 'frontend/build/index.html')

@api_view(['GET'])
def top_rated_projects(request):
    projects = Project.objects.filter(is_running=True).order_by('-rating')[:5]
    data = [{"id": p.id, "title": p.title, "description": p.description} for p in projects]
    return Response(data)
