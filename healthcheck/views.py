from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world. your health has been checked")
