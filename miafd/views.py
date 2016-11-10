from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .form import BusinessForm
from .models import Business

# Create your views here.

def thanks(request):
    return HttpResponse("Thanks MIAFD")

def about(request):
    return render(request, 'miafd/about.html')

def index(request):
    return render(request, 'miafd/home.html')

def visit(request):
    return render(request, 'miafd/visiters.html')

def business_form(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = BusinessForm(request.POST)
        # check whether it's valid:
        data = request.POST
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        b = Business(business_type=data["type"],
                        businees_name=request.POST["name"],
                        business_address=request.POST["address"],
                        businees_telephone=request.POST["phone"],
                        businees_fax=data["fax"],
                        businees_email=data["email"])
        b.save()
        #TODO: fix this later
        return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    
    #TODO: fix later
    return render(request, 'miafd/name.html')