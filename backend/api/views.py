import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data.keys())
    data['headers'] = request.headers
    data['content_type'] = request.content_type
    return JsonResponse()

