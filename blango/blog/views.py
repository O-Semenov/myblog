from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from blog.forms import CommentForm
import logging

logger = logging.getLogger(__name__)

class index(ListView):
    model = Post
    template_name = 'blog/index.html'
    

class post_detail(FormMixin, DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(post_detail, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Your comment form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if request.user.is_active:
            if request.method == "POST":
                comment_form = CommentForm(request.POST)

                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.content_object = self.object
                    comment.creator = request.user
                    comment.save()
                    logger.info(
                        "Created comment on Post for user %s", request.user
                    )
                    return redirect(request.path_info)
            else:
                comment_form = CommentForm()
        else:
            comment_form = None
