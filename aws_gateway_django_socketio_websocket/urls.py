"""
URL configuration for aws_gateway_django_socketio_websocket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import JsonResponse, SeatSocketView

@csrf_exempt
def test(request, *args, **kwargs):
    return JsonResponse({"seats": ["a", "b"]})

@csrf_exempt
def test_select(request, *args, **kwargs):
    return JsonResponse({"seats": ["a", "b"], "status": "selected"})

@csrf_exempt
def test_unselect(request, *args, **kwargs):
    return JsonResponse({"seats": ["a", "b"], "status": "unselected"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('seats/', test),
    path('seats/select/', test_select),
    path('seats/unselect/', test_unselect),
    # path('seats/', SeatSocketView.as_view()),
]
