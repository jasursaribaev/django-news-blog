from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('news/<slug:slug>', views.NewsDetailView.as_view(), name='news_detail'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('category/<slug:slug>', views.CategoryPostsViews.as_view(), name='category-posts'),
    path('news/update/<slug:slug>', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/delete/<slug:slug>', views.NewsDeleteView.as_view(), name='news-delete'),
    path('news/create/', views.NewsCreateView.as_view(), name='news-create'),
]
