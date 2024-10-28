from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import DetailsForm
from .models import *
from django.contrib import messages



# Create your views here.

def details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            
            Details.objects.create(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                city=form.cleaned_data['city'],
                phone_number=form.cleaned_data['phone_number']
            )
            messages.success(request, 'Detail successfully updated')
            return redirect('details')  
    else:
        form = DetailsForm()
    return render(request,'details.html', {'form': form})
    
