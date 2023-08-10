from django.shortcuts import render
from django.views import View
# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

def error_400(request, exception):
    data = {}
    return render(request,'landing/error/400.html', data)

def error_403(request, exception):
    data = {}
    return render(request,'landing/error/403.html', data)

def error_404(request, exception):
    data = {}
    return render(request,'landing/error/404.html', data)

def error_500(request):
    data = {}
    return render(request,'landing/error/500.html', data)