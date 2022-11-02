from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Socialmediahandle
from django.http import HttpResponse
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from django.db.models import Q 
def home(request):
 posts = Post.objects.all()
 cats_menu = Category.objects.all()
 social_menus = Socialmediahandle.objects.all()
 context={
 'posts':posts,
 'cats_menu':cats_menu,
 'social_menus':social_menus
 }
 return render(request,'home.html', context)
 
class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context
    def get_context_data(self, *args, **kwargs):
        cats_menu = Category.objects.all
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['cats_menu']=cats_menu
        return context
    def get_context_data(self, *args, **kwargs):
        social_menus = Socialmediahandle.objects.all
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['social_menus']=social_menus
        return context
        

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    cats_menu = Category.objects.all()
    social_menus = Socialmediahandle.objects.all()
    context = {
        "category": category,
        "posts": posts,
        'cats_menu':cats_menu,
        "social_menus":social_menus
    }
    return render(request, "blog_category.html", context)
def landing_page(request):
	social_menus = Socialmediahandle.objects.all()
	return render(request,'landing_page.html',{"social_menus":social_menus})
# Create your views here.
