from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3
import json
from decouple import config

from .models import Art, Profile, PaintFile

S3_BASE_URL = config('S3_BASE_URL')
BUCKET = config('BUCKET')

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


@csrf_exempt
def paint(request):
    if request.method == 'GET':
        return render(request, 'paint.html')
    elif request.method == 'POST':
        filename = request.POST.get('save_fname')
        data = request.POST.get('save_cdata')
        image = request.POST.get('save_image')
        file_data = PaintFile(name=filename, image=data, canvas_image=image)
        file_data.save()
        return redirect('home')


@csrf_exempt
def files(request):
    if request.method == 'GET':
        all_data = PaintFile.objects.all()
        return render(request, "files.html", {'files': all_data})



class ArtList(LoginRequiredMixin, ListView):
    model = Art


class ArtCreate(LoginRequiredMixin, CreateView):
    model = Art
    fields = ['title', 'media_type', 'genre', 'description',
              'colors_used', 'karma', 'date_posted', 'is_public']

    def form_valid(self, form):
        art_file = self.request.FILES.get('art-file', None)
        if art_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + \
                art_file.name[art_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(art_file, BUCKET, key)
                url = f'{S3_BASE_URL}{BUCKET}/{key}'
                form.instance.url = url
            except:
                print('An error ocurred uploading the file to s3.')
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArtDetail(LoginRequiredMixin, DetailView):
    model = Art


class ArtUpdate(LoginRequiredMixin, UpdateView):
    model = Art
    fields = ['title', 'media_type', 'genre', 'description',
              'colors_used', 'karma', 'date_posted', 'is_public']


class ArtDelete(LoginRequiredMixin, DeleteView):
    model = Art
    success_url = '/art/'
