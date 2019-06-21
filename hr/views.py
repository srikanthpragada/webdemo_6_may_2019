import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Passenger


def hello(request):
    if 'name' in request.GET:
        name = request.GET['name']  # take value for name parameter
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
                  {"countries": countries})


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def add_passenger(request):
    if 'plist' in request.session:
        plist = request.session['plist']
    else:
        plist = []

    if request.method == "POST":
        p = Passenger(request.POST["pname"], request.POST["page"])
        # Convert object to dict so that it is JSON serializable
        plist.append(p.__dict__)
        request.session['plist'] = plist

    return render(request, 'reservation.html',
                   {'plist': plist, 'len' : len(plist) })


def delete_passenger(request):
    if 'plist' in request.session:
        plist = request.session['plist']
    else:
        return redirect("/hr/plist")

    # find out passenger to be deleted
    pname = request.GET["name"]
    for idx,p in enumerate(plist):
        if p['name'] == pname:
            pos = idx
            break
    else:
        return redirect("/hr/plist")

    del plist[pos]
    request.session['plist'] = plist

    return redirect("/hr/plist")

