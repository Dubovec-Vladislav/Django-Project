from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class Home(ListView):
    model = Post
    template_name = 'main/home.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


def main(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')
