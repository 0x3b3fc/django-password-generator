# implemented modules and packages
from django.shortcuts import render
from django.http import HttpResponse
import random
import pyperclip


# the home function to get view
def home(request):
    return render(request, 'generator/home.html')


# the password function to access the password generator page with view
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    # conditions for generated password
    # check if the uppercase mode is on
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # check if the numbers mode is on
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    # check if the special characters mode is on
    if request.GET.get('special'):
        characters.extend(list('./*-+_=()&^%$#@!ّّ":;><~'))
    # function to convert string to integer
    length = int(request.GET.get('length'))
    # condition to check if the password length equal or more than 6 chars and less than or equal 14 chars
    if 6 <= length <= 14:
        length = int(request.GET.get('length'))
    else:
        length = 10
    # create variable named the password to save generated password
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)
    # method to copy password to clipboard if you click on it
    pyperclip.copy(thepassword)
    # the return of the function to pass the generated password to the view with mvc technology
    return render(request, 'generator/password.html', {'password': thepassword})
