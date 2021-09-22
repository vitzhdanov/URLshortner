from django.urls import path
from shortner import views


urlpatterns = [
    path('', views.main, name='main'),
    path('<url>', views.url, name='url')
]