from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog_list.html'
    # We changed a context variable from object_list to all_posts_list
    context_object_name = 'all_posts_list'
