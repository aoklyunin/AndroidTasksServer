
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from tasks.models import Task


def index(request):
    latest_question_list = Task.objects.order_by('author')
    template = loader.get_template('tasks/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
