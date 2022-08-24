from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Join, Login

urlpatterns = [
    path('join', Join.as_view()),
    path('login', Login.as_view()),
]
