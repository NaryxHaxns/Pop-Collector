from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pop
from .forms import DustingForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pops_index(request):
    pops = Pop.objects.all()
    return render(request, 'pops/index.html', {'pops': pops})

def pops_detail(request, pop_id):
    pop = Pop.objects.get(id=pop_id)
    dusting_form = DustingForm()
    return render(request, 'pops/detail.html', {
        'pop': pop,
        'dusting_form': dusting_form,
        })

def add_dusting(request, pop_id):
    form = DustingForm(request.POST)
    if form.is_valid():
        new_dusting = form.save(commit=False)
        new_dusting.pop_id = pop_id
        new_dusting.save()
    return redirect('detail', pop_id=pop_id)

class PopCreate(CreateView):
    model = Pop
    fields = '__all__'

class PopUpdate(UpdateView):
    model = Pop
    fields = '__all__'

class PopDelete(DeleteView):
    model = Pop
    success_url = '/pops/'

