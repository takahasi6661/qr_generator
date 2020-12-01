from django.urls import path
from .views import *


urlpatterns=[
    path('', sites_list),
    path('img/<str:id>/', ImageGenerator.as_view(),name='image_generator')
]
