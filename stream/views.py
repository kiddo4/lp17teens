from django.shortcuts import render, redirect, get_object_or_404
from . models import VidStream
from Baseapp.models import Socialmediahandle
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 
from hitcount.views import HitCountDetailView

class GeneralVideoListView(ListView):
    model = VidStream
    template_name = 'stream/video-list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']
    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all
        context = super(GeneralVideoListView, self).get_context_data(**kwargs)
        context['cats_menu']=cats_menu
        return context
    def get_context_data(self, *args, **kwargs):
        social_menus = Socialmediahandle.objects.all
        context = super(GeneralVideoListView, self).get_context_data(**kwargs)
        context['social_menus']=social_menus
        return context
class VideoDetailView(HitCountDetailView):
    template_name = "stream/video-detail.html"
    model = VidStream
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True
    def get_context_data(self, *args, **kwargs):
        social_menus = Socialmediahandle.objects.all
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        context['social_menus']=social_menus
        return context
    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        context['cats_menu']=cats_menu
        return context
    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_videos': VidStream.objects.order_by('-hit_count_generic__hits')[:5],
        })
        return context
    
    
    
def search(request):
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = VidStream.objects.filter(title__contains=query)
            return render(request, 'stream/search.html',{'videos':results})
    
    return render(request, 'stream/search.html')
# Create your views here.
