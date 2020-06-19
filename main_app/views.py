from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pop, Group
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
    groups_pop_doesnt_have = Group.objects.exclude(id__in = pop.groups.all().values_list('id'))
    dusting_form = DustingForm()
    return render(request, 'pops/detail.html', {
        'pop': pop,
        'dusting_form': dusting_form,
        'groups': groups_pop_doesnt_have
        })

def assoc_group(request, pop_id, group_id):
    pop = Pop.objects.get(id=pop_id)
    pop.groups.add(group_id)
    return redirect('detail', pop_id=pop_id)

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

class GroupList(ListView):
    model = Group

class GroupDetail(DetailView):
    model = Group

class GroupCreate(CreateView):
    model = Group
    fields = '__all__'

class GroupUpdate(UpdateView):
    model = Group
    fields = '__all__'

class GroupDelete(DeleteView):
    model = Group
    success_url = '/groups/'
