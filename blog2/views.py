from django.views import generic


from .models import BlogPost

class IndexView(generic.DetailView):
    model = BlogPost
    template_name = "blog/index.html"

