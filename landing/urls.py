from django.urls import path
from landing.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index')
]

handler400 = 'landing.views.error_400'
handler403 = 'landing.views.error_403'
handler404 = 'landing.views.error_404'
handler500 = 'landing.views.error_500'