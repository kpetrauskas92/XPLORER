from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

def error_400(request, exception):
    return render(request, 'error/400.html', {}, status=400)

def error_403(request, exception):
    return render(request, 'errors/403.html', {}, status=403)

def error_404(request, exception):
    return render(request, 'errors/404.html', {}, status=404)

def error_500(request):
    return render(request, 'errors/500.html', {}, status=500)