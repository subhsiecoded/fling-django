from django.shortcuts import render,get_object_or_404, redirect
from .models import Fling
from .forms import FlingForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def fling_list(request): #this is to show the flings/posts
    flings= Fling.objects.all().order_by('created_at')
    return render(request, 'fling_list.html', {'flings': flings})

#there's this decorator which will wrap the function under any functionality
@login_required
def fling_create(request):
    #what if the user has posted/submitted the form already
    if request.method=="POST":
        form = FlingForm(request.POST, request.FILES) #you are accepting files too
        #csrf security is provided by django
        if form.is_valid():
            #how to take the user who's filling the form?
            fling = form.save(commit=False) #commit=false means we are not saving it into the database
            fling.user = request.user
            fling.save() #now it is saved in the database
            return redirect('fling_list') #the function above is given here as the argument saying that the user is redirected to the list of flings 
    else:
        form = FlingForm()#user is given an empty form 
    return render(request, 'fling_form.html', {'form': form})

@login_required
def fling_edit(request, fling_id):
    fling = get_object_or_404(Fling, pk=fling_id, user=request.user) #Fling here is the model, but what primary key you want to view (which is going to be the id)
    #user=request.user mean that only the current user can edit his fling not other's flings
    if request.method=="POST":
        form = FlingForm(request.POST, request.FILES, instance=fling) #instance=fling means that you are editing the old fling.
        #now we need to save the fling
        if form.is_valid():
            fling = form.save(commit= False)
            fling.user = request.user
            fling.save()
            return redirect('fling_list')
        pass
    else:
        form = FlingForm(instance= fling) #define the fling, since you are editing the form must be prefilled with some data 
    return render(request, 'fling_form.html', {'form': form})

@login_required
def fling_delete(request, fling_id):
    fling = get_object_or_404(Fling, pk = fling_id, user =request.user)
    if request.method == "POST":
        fling.delete()
        return redirect('fling_list')
    #now you need to render something after the delete operation
    return render(request, 'fling_confirm_delete.html', {'fling': fling})

def register(request):
    if:
        pass
    else:
        form = UserRegistrationForm
    return render(request, 'registration/register.html', {'form': form})
