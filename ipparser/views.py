import os
import requests
from collections import OrderedDict
import traceback

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
                f = form.cleaned_data["file"]
                (nameToLessons, IPTotals, GTTotals) = outputLessons(f)
                nameToLessons = OrderedDict(sorted(nameToLessons.iteritems(), key= lambda (k,v): getLastName(k)))
                return render(request, 'index.html', {'form': form, 'nameToLessons': nameToLessons, "ipTotals": IPTotals, "gtTotals": GTTotals})
            except Exception as e:
                traceback.print_exc()
                return render(request, 'index.html', {"form": form, "error": True})
    # Create a blank form (GET request)
    else:
        form = IPScheduleForm()
    return render(request, 'index.html', {'form': form})
