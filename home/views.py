from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Park, Contact
from .forms import contactForm
# Create your views here.
def home(request):
    parks = Park.objects.all()
    if request.method == 'POST':
        form = contactForm(request.POST or None)
        contact = Contact()
        if form.is_valid():
            contact.first_name = form.cleaned_data['first_name']
            contact.last_name = form.cleaned_data['last_name']
            contact.email = form.cleaned_data['email']
            contact.phone = form.cleaned_data['phone']
            contact.location = form.cleaned_data['location']
            contact.destination = form.cleaned_data['destination']
            contact.flight = form.cleaned_data['flight']
            contact.accomodation = form.cleaned_data['accomodation']
            contact.pick_up = form.cleaned_data['pick_up']
            contact.tour_cars = form.cleaned_data['tour_cars']
            contact.save()
            messages.info(request, f'Infomation Submited')
            return redirect('home')

        messages.error(request, f'Infomation was not Submited')
        return redirect('home')

    context = {
        'parks':parks
    }
    return render(request, 'home/index.html', context)



def details(request, id):
    parks = Park.objects.get(id=id)
    if request.method == 'POST':
        form = contactForm(request.POST or None)
        contact = Contact()
        if form.is_valid():
            contact.first_name = form.cleaned_data['first_name']
            contact.last_name = form.cleaned_data['last_name']
            contact.email = form.cleaned_data['email']
            contact.phone = form.cleaned_data['phone']
            contact.location = form.cleaned_data['location']
            contact.destination = form.cleaned_data['destination']
            contact.flight = form.cleaned_data['flight']
            contact.accomodation = form.cleaned_data['accomodation']
            contact.pick_up = form.cleaned_data['pick_up']
            contact.tour_cars = form.cleaned_data['tour_cars']
            contact.save()
            messages.info(request, f'Infomation Submited')
            return redirect('details')

        messages.error(request, f'Infomation was not Submited')
        return redirect('details')
    context = {
        'parks':parks
    }
    return render(request, 'home/details.html', context)