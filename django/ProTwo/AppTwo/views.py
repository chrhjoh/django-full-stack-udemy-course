from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import RegisterUserForm

# Create your views here.
def index(reponse):
    return HttpResponse('<em>My Second App</em>')

def help(response):
    var_dict = {'help_text' : 'This is the Help Page'}
    return render(response, 'AppTwo/help.html', context=var_dict)

def users(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    user_form = RegisterUserForm()
    user_info = User.objects.order_by('first_name')
    result_dict = {"user_info" : user_info,
                   "form" : user_form}
    return render(request, 'AppTwo/users.html', context=result_dict)

