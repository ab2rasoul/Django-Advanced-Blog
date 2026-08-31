from django.urls import path
from . import views
from .views import RedirectToMaktab
from django.views.generic import TemplateView, RedirectView

app_name = "blog"

urlpatterns = [    
    path('cbv-index', views.IndexView.as_view(),name = 'cbv-index'),
    path('post/', views.PostList.as_view(),name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(),name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(),name='post-edit'),
    path('go-to-maktabkhooneh/<int:pk>/', RedirectToMaktab.as_view(pattern_name="blog:cbv-index"), name = 'redirect-to-index')
]