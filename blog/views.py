# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category, Tag, Comment
from .forms import CommentForm

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy


class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Boocic'
        return context


class PostsByCategory(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])


class PostsByTag(ListView):
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Записи по тегу: {Tag.objects.get(slug=self.kwargs['slug'])}"
        return context

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single_post.html'
    context_object_name = 'post'


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"  # Для того чтобы
        # пристыковать ?s=пост к page=2 в строке запроса
        context['title'] = "Searching Results"
        return context

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))


def LikeView(request, slug):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, slug=request.POST.get('post_slug'))
        post.likes.add(request.user)
        # return HttpResponseRedirect(reverse('view_news', args=[str(pk)]))
        return redirect('post', slug)
    else:
        return redirect('/')


def RemoveLikeView(request, slug):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, slug=request.POST.get('post_slug'))
        post.likes.remove(request.user)
        # return HttpResponseRedirect(reverse('view_news', args=[str(pk)]))
        return redirect('post', slug)
    else:
        return redirect('/')


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/add_comment.html"
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
