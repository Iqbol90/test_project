from django.urls import path
from .views import *

urlpatterns=[
    path('', basic, name='basic'),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('gallery/', gallery, name="gallery"),
    path('packages/', packages, name="packages"),
    path('pricing/', pricing, name="pricing")
]
