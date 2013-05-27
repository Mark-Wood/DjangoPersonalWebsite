from django.views.generic import DetailView, ListView

from models import Post


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(published=True)
        return context


class PostList(ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.filter(published=True)
    template_name = 'blog/post_list.html'