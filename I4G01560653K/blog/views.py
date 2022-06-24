from audioop import reverse
from dataclasses import field
from msilib.schema import ListView
from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy



class PostListView(ListView):
    model = Post
    def PostCreateView(CreateView):
        model = Post,
        fields = "__all__"
        success_url  = reverse_lazy('blog:all')
    def  PostDetailView(DetailView):
        model = Post,
    def PostUpdateView(UpdateView):
        model = Post 
        fields = "__all__" 
        success_url  = reverse_lazy('blog:all')
    def PostDeleteView(UpdateView):
        model = Post 
        fields = "__all__" 
        success_url  = reverse_lazy('blog:all')
