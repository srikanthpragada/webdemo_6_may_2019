from django.http import HttpResponse


def hello(request):
    if 'name' in request.GET:
        name = request.GET['name'] # take value for name parameter
    else:
        name = "Django"

    return HttpResponse(f"<h1 style='color:blue'>Hello {name}!</h1>")


def goodbye(request):
    return HttpResponse("<h2>Good Bye! </h2> <h3>Thanks for using HR Application.</h3>")
