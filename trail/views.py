from django.shortcuts import render
from django.http import HttpResponse
def myapp(request):
    return HttpResponse("""<html><body bgcolor=black><font fgcolor=white><h1><center>welcome govardhana</center></h1></font></body></html>""")



