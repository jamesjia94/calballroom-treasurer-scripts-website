import os
import requests
import pprint
from collections import OrderedDict

from django.shortcuts import render
from django.http import HttpResponse
from .forms import IPScheduleForm
from .models import Greeting
from parser import outputLessons, getLastName


# Create your views here.
def index(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = IPScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                pp = pprint.PrettyPrinter()
                f = form.cleaned_data["file"]
                (nameToLessons, IPTotals, GTTotals) = outputLessons(f)
                nameToLessons = OrderedDict(sorted(nameToLessons.iteritems(), key= lambda (k,v): getLastName(k)))
                for key,value in nameToLessons.iteritems():
                    print key
                    pp.pprint(value)
                    print
                results = {"nameToLessons": nameToLessons, "ipTotals": IPTotals, "gtTotals": GTTotals}
                return render(request, 'index.html', {'form': form, 'results': results})
            except Exception as e:
                print e
                return render(request, 'index.html', {"form": form, "error": True})
    # Create a blank form (GET request)
    else:
        form = IPScheduleForm()
    return render(request, 'index.html', {'form': form})

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

