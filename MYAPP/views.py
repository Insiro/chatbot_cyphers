from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def keyboard(request):

    return JsonResponse({
        "type": "buttons", "text"
        "buttons": ["강아지 사료양"]
    })

@csrf_exempt    #보안
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == "강아지 사료양":
        global section
        section = '사료1'

        return JsonResponse({
            'message': {
                'text': "강아지의 몸무게(kg)를 알려주세요!"
            },
            'keyboard': {
                'type': 'text'
            }
        })