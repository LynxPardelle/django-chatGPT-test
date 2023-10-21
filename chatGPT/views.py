from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def author(request):
    return HttpResponse("""<h1>Lynx Pardelle</h1>
    <h2>From ChatGPT APP</h2>                    
    """)
