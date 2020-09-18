from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3
from decouple import config 

from .models import Art, Profile, Comment
from .forms import CommentForm

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
            user_profile = Profile()
            user_profile.user = user
            user_profile.save()
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
    fields = ['title', 'media_type', 'genre', 'description', 'colors_used', 'karma', 'date_posted','is_public']

    def form_valid(self, form):
        art_file = self.request.FILES.get('art-file', None)
        if art_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + art_file.name[art_file.name.rfind('.'):]
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
    fields = ['title', 'media_type', 'genre', 'description', 'colors_used', 'karma', 'date_posted', 'is_public']

    def form_valid(self, form):
        art_file = self.request.FILES.get('art-file', None)
        if art_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + art_file.name[art_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(art_file, BUCKET, key)
                url = f'{S3_BASE_URL}{BUCKET}/{key}'
                form.instance.url = url
            except:
                print('An error occurred uploading the file to s3.')
        form.instance.user = self.request.user
        return super().form_valid(form)

class ArtDelete(LoginRequiredMixin, DeleteView):
    model = Art
    success_url = '/art/'

def gallery_index(request):
    art = Art.objects.all()
    return render(request, 'gallery/gallery_index.html', { 'art': art })

def gallery_detail(request, art_id):
    art = Art.objects.get(id=art_id)
    comment_form = CommentForm()
    return render(request, 'gallery/gallery_detail.html', { 'art': art, 'comment_form': comment_form })

@login_required
def add_comment(request, art_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.art_id = art_id
        new_comment.user = request.user
        new_comment.save()
        print(new_comment, request.user)
    return redirect('gallery_detail', art_id=art_id)

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['comment', 'rating', 'date_created']
    
class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = '/gallery/'
        
class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['bio', 'birthday', 'artist_type', 'is_public', 'location', 'profile_img', 'points']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['bio', 'birthday', 'artist_type', 'is_public', 'location', 'profile_img', 'points']
                


def profile_detail(request, user_id):
    profile = Profile.objects.get(user=user_id)
    return render(request, 'profile/detail.html', { 'profile': profile })
    
    # def form_valid(self, form):
    #     art_file = self.request.FILES.get('art-file', None)
    #     if art_file:
    #         s3 = boto3.client('s3')
    #         key = uuid.uuid4().hex[:6] + art_file.name[art_file.name.rfind('.'):]
    #         try:
    #             s3.upload_fileobj(art_file, BUCKET, key)
    #             url = f'{S3_BASE_URL}{BUCKET}/{key}'
    #             form.instance.url = url
    #         except:
    #             print('An error ocurred uploading the file to s3.')
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
