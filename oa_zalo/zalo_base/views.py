from django.http import HttpResponse
from django.template import loader

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
 
from .services import ZaloService
from .automation import *

import json

def index(request):
    template = loader.get_template('zalo_base/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@api_view(['POST'])
def follow_hook(request):
    if (request.method == 'POST'):
        datas = json.loads(request.body)
        event = datas.get('event_name', False)
        if event:
            result = ZaloService().action_by_event(event, datas)
            return JsonResponse(result)

    return JsonResponse({
        'success': 0, 
        'message': f"Request method {request.method} is not allowed!"
        })

@api_view(['GET'])
def init(request):
    if (request.method == 'GET'):
        result = createDriverInstance()
        return JsonResponse(result) 

    return JsonResponse({
        'success': 0, 
        'message': f"Request method {request.method} is not allowed!"
        })

@api_view(['GET'])
def signin(request):
    if (request.method == 'GET'):
        datas = request.GET
        return JsonResponse(signin_ccos(datas))

    return JsonResponse({
        'success': 0, 
        'message': f"Request method {request.method} is not allowed!"
        })

@api_view(['GET'])
def otp(request):
    if (request.method == 'GET'):
        datas = request.GET
        return JsonResponse(otp_code(datas))

    return JsonResponse({
        'success': 0, 
        'message': f"Request method {request.method} is not allowed!"
        })

@api_view(['GET'])
def close(request):
    if (request.method == 'GET'):
        return JsonResponse(close_ccos())

    return JsonResponse({
        'success': 0, 
        'message': f"Request method {request.method} is not allowed!"
        })

