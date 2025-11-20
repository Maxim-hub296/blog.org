from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Story

# Create your views here.
class StoriesListView(ListView):
    model = Story
    context_object_name = 'stories'
    template_name = 'stories/stories_list.html'
    paginate_by = 2
    ordering = ['data']

class StoriesDetailView(DetailView):
    model = Story
    template_name = "stories/story_detail.html"