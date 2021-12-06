from django.shortcuts import render, redirect
from .models import Story, Exists
from .forms import StoryForm, ExistsForm
from django.views.generic import DetailView, UpdateView,DeleteView


def story(request):
    story = Story.objects.all()
    return render(request, 'main/story.html', {'story': story})

def exists(request):
    exists = Exists.objects.all()
    return render(request, 'main/exists.html', {'exists': exists})

class DetailView1(DetailView):
    model = Story
    template_name = 'main/detail_view1.html'
    context_object_name = 'story'

class UpdateView1(UpdateView):
    model = Story
    template_name = 'main/create.html'

    form_class = StoryForm

class DeleteView1(DeleteView):
    model = Story
    success_url = '/'
    template_name = 'main/delete1.html'

class DetailView2(DetailView):
    model = Exists
    template_name = 'main/detail_view2.html'
    context_object_name = 'exists'

class UpdateView2(UpdateView):
    model = Exists
    template_name = 'main/create2.html'

    form_class = ExistsForm

class DeleteView2(DeleteView):
    model = Exists
    success_url = '/exists/'
    template_name = 'main/delete2.html'


def create(request):
    error = ''
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('story')
        else:
            error = 'Form is incorrect'


    form = StoryForm()

    data = {
        'form': form,
        'error': error
    }


    return render(request, 'main/create.html', data)

def create2(request):
    error = ''
    if request.method == "POST":
        print(request)
        form = ExistsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exists')
        else:
            error = 'Form is incorrect'

    form2 = ExistsForm()

    data2 = {
        'form2': form2
    }
    return render(request, 'main/create2.html', data2)
# Create your views here.
