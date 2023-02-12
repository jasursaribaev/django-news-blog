from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormView
from news_app.models import News, Category
from news_app.form import ContactForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_posts'] = News.objects.filter()[:4]
        context['popular_posts'] = News.objects.filter()[:4]
        context['categories'] = Category.objects.all()
        return context
    
class NewsDetailView(LoginRequiredMixin, DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'new'
    
class ContactFormView(FormView):
    template_name = 'news/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class CategoryPostsViews(ListView):
    model = News
    template_name = "news/post_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])
        context['posts'] = category.category_news.all()
        return context
    
class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'news/news_update.html'
    # success_url = reverse_lazy('home')
    
    def get_success_url(self):
        
        return reverse('news_detail', kwargs={'slug': self.kwargs['slug']})
    
class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('home')
    
class NewsCreateView(LoginRequiredMixin,CreateView):
    model = News
    template_name = 'news/news_create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')
    success_url = reverse_lazy('home')
    
    def get_success_url(self):
        return reverse('news_detail', kwargs={'slug': self.object.slug})