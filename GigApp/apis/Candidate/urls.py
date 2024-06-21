from django.urls import path
from . import views

urlpatterns = [

    path('user-add', views.CbtUserViewSet.as_view({'post': 'UserAdd'})),

]