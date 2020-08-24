from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.
def home(request) :
    return render(request, 'generator/home.html')

def about(request) :
    return render(request,'generator/about.html')

def password(request) :
    chars = list(string.ascii_lowercase)
    

    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase') :
        chars.extend(list(string.ascii_uppercase))
    
    if request.GET.get('numbers') :
        chars.extend(list(string.digits))
    
    special_chars = '@!/?:_-#$&*^'
    if request.GET.get('special') :
        chars.extend(list(special_chars))

    thepassword = ''

    for x in range(length) :
        thepassword += random.choice(chars)
        


    return render(request, 'generator/password.html',{'password':thepassword})