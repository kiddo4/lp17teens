from . import views
from . views import (
    VideoDetailView, 
    GeneralVideoListView, 
)
from django.urls import path 


app_name = "stream"

urlpatterns = [
    path('video/',GeneralVideoListView.as_view(),),
    path('video/<slug:slug>/', VideoDetailView.as_view(),),
    path('search',views.search,name="search"),
]