from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pop
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
    return render(request, 'pops/detail.html', { 'pop': pop })

class PopCreate(CreateView):
    model = Pop
    fields = '__all__'

class PopUpdate(UpdateView):
    model = Pop
    fields = '__all__'

class PopDelete(DeleteView):
    model = Pop
    success_url = '/pops/'