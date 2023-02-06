from django.shortcuts import render, redirect,HttpResponse

def home(request):
    print('test')
    return HttpResponse('Start')