from django.http import HttpResponse, JsonResponse


def author(request):
    return JsonResponse(
        {
            "author": "Lynx Pardelle",
            "from": "ChatGPT APP / user-actions.py"
        })
