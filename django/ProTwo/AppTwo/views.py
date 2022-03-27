from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(reponse):
    return HttpResponse('<em>My Second App</em>')

def help(response):
    var_dict = {'help_text' : 'This is the Help Page'}
    return render(response, 'AppTwo/help.html', context=var_dict)