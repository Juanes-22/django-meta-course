from django.http import HttpResponse, HttpResponseNotFound

# def handler404(request, exception):
#     return HttpResponse("404: Page not found!")

def handler404(request, exception):
    return HttpResponseNotFound("404: Page not found!")
