from Baseapp.views import landing_page,home,blog_category
from django.urls import path
from .views import PostDetailView
urlpatterns = [
    path('home/', home, name='home'),
    path('home/search/posts/<slug:slug>/', PostDetailView.as_view(),),
    path("<category>/", blog_category, name="blog_category"),
    path("<str:category>/", blog_category, name="blog_category"),
    path("",landing_page, name="landing_page"),
]