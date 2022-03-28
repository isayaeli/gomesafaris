from django.shortcuts import render, redirect
from .forms import TrackForm
from .models import UserTracker,AdminTracker
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def index(request):
    admin_tracker = AdminTracker.objects.filter(tourist=request.user)
    user_tracker = UserTracker.objects.filter(tourist=request.user)
    if request.method == 'POST':
        print(request.POST)
        form = TrackForm(request.POST or None)
        tracker = UserTracker()
        if form.is_valid():
            tracker.place_1 = form.cleaned_data['place_1']
            tracker.place_2 = form.cleaned_data['place_2']
            tracker.place_3 = form.cleaned_data['place_3']
            tracker.place_4 = form.cleaned_data['place_4']
            tracker.place_5 = form.cleaned_data['place_5']
            tracker.place_6 = form.cleaned_data['place_6']
            tracker.tourist = request.user
            tracker.save()
            return redirect('dash')
        return redirect('dash')
    form = TrackForm()
    context = {
        'form':form,
        'admin_tracker':admin_tracker
    }
    return render(request, 'dash/index.html', context)