from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('/', views.post_list),
    path('<int:id>/',views.post_detail)
]