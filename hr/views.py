from django.http import HttpResponse
from django.shortcuts import  render
import requests

def hello(request):
    if 'name' in request.GET:
        name = request.GET['name'] # take value for name parameter
    else:
        name = "Django"

    return HttpResponse(f"<h1 style='color:blue'>Hello {name}!</h1>")


def goodbye(request):
    return HttpResponse("<h2>Good Bye! </h2> <h3>Thanks for using HR Application.</h3>")


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    # Send template to client
    return render(request, "countries.html",
                  {"countries" : countries})