from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(reponse):
    return HttpResponse('<em>My Second App</em>')

def help(response):
    var_dict = {'help_text' : 'This is the Help Page'}
    return render(response, 'AppTwo/help.html', context=var_dict)

def users(response):
    user_info = User.objects.order_by('first_name')
    result_dict = {"user_info" : user_info}
    return render(response, 'AppTwo/users.html', context=result_dict)
