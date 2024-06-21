from django.urls import path
from . import views

urlpatterns = [

   path('user-list/', views.UserList, name='user_list'),
   path('fatch-user-list/', views.FatchUserList , name='fatch_user_list'),
   path('edit-user/<int:user_id>/', views.EditUser, name='edit_user'),
   path('add-user/', views.EditUser, name='add_user'),

]