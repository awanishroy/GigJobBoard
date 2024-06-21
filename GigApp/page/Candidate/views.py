from django.shortcuts import render
from django.contrib.auth.models import User  # Import the User model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse


def home(request):
    return render(request, 'website/index.html')

def UserList(request):

    context = {
        'users': ['User1', 'User2', 'User3'],
    }
    return render(request, 'admin/user_list.html', context)

def FatchUserList(request):
    users = User.objects.all().values('id', 'username', 'email', 'first_name', 'last_name')
    data = list(users)  # Convert QuerySet to list for JSON serialization
    for user in data:
        edit_url = reverse('edit_user', kwargs={'user_id': user['id']})
        user['actions'] = f"""
            <div class="btn-group">
                <button type="button" class="btn btn-primary btn-sm dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Actions
                </button>
                <div class="dropdown-menu">
                    <a class="dropdown-item edit-btn" href="{edit_url}" data-user-id="{user['id']}">Edit</a>
                    <button class="dropdown-item delete-btn" type="button" data-user-id="{user['id']}">Delete</button>
                </div>
            </div>
        """
    return JsonResponse({'data': data})

def EditUser(request, user_id=None):
    if user_id is None:
        context = {
            'title': 'Add User',
            'action': 'Create'
        }
    else:
        user = get_object_or_404(User, id=user_id)
        context = {
            'title': 'Update User',
            'action': 'Update',
            'user': user
        }
    
    return render(request, 'admin/candidate/add_user.html', context)