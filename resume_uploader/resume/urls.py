from django.urls import path
from. import views

urlpatterns =[
    path('',views.index),
    path('upload/',views.upload_resume,name="upload_resume"),
    path('success/',views.success,name="success"),



]