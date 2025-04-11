from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView , DetailView , CreateView ,UpdateView  
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import post



def home(request):

    context = {
        'posts' : post.objects.all()
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request , 'blog/home.html' , context)

class postListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    odering = ['-date_posted']

class postDetailView(DetailView):
    model = post



class postCreateView(LoginRequiredMixin , CreateView):
    model = post
    fields = ['title' , 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class postUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title' , 'content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post  = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request , 'blog/about.html' , {'title': 'about'} )