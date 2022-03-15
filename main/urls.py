from django.urls import path
from .views import *


urlpatterns = [
    path("about_api/", about_api, name="about_api"),
    path("product_api/", product_api, name="product_api"),
    path("video_api/", video_api, name="video_api"),
    path("feedback_api/", feedback_api, name="feedback_api"),
    path("infor_api/", infor_api, name="infor_api"),
    path("cause_api/", cause_api, name="cause_api"),
    path('send_number/', send_number, name='send_number')
]
