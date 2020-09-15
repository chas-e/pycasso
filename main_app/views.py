from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3

from .models import Art, Profile

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'pycasso629bucket'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else: 
            error_message = 'Invalid sign up, please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class ArtList(LoginRequiredMixin, ListView):
    model = Art

class ArtCreate(LoginRequiredMixin, CreateView):
    model = Art
    fields = ['title', 'media_type', 'genre', 'description', 'colors_used', 'karma', 'date_posted', 'is_public']

    def add_art_image(request):
        art_file = request.FILES.get('art_file', None)
        if art_file:
            s3 = boto3_client('s3', kwargs={'profile_name': pycasso629 })
            key = uuid.uuid4().hex[:6] + art_file.name[art_file.name.rfind('.'):]

            try:
                s3.upload_fileobj(art_file, BUCKET, key)
                url = f'{S3_BASE_URL}{BUCKET}/{key}'
                art = Art(url=url, art_id=art_id)
                art.save()
            except:
                print('An error ocurred uploading the file to s3.')
        return redirect('art_index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
