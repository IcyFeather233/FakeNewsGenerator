import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.views.decorators.http import require_http_methods

from webApp.models import News


@csrf_exempt
def generate(request):
    response = {}
    if request.method == 'GET':
        response['method'] = 'get'
        return JsonResponse(response)
    else:
        response['method'] = 'post'
        postBody = request.body
        json_result = json.loads(postBody)
        news = News(json_result)
        content = news.gen()
        response['content'] = content
        return JsonResponse(response)





