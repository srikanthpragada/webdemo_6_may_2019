from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View, ListView

from .models import Employee


class AboutView(TemplateView):
    template_name = 'about.html'


class WishView(View):

    def get(self, request):
        return HttpResponse("<h1>Handling Get...</h1>")

    @method_decorator(csrf_exempt)
    def post(self, request):
        return HttpResponse("<h1>Handling POST...</h1>")


class ListEmployeesView(ListView):
    model = Employee
    template_name = 'employee_list.html' # hr/employee_list.html
    context_object_name = 'employees'    # object_list
