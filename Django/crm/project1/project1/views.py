from django.http import HttpResponse

def index(request):
    html="<h1>HELLO</h1>"
    return HttpResponse(html)

