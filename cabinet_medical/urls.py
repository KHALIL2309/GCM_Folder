from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    # path('patient/', views.patient , name="patient"),
    path('patient/<str:pk>', views.patient , name="patient"),
    path('create/', views.create , name="create"),
    path('update/<str:pk>', views.update , name="update"),
    path('delete/<str:pk>', views.delete , name="delete"),
] 