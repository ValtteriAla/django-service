from django.views import generic


from .models import BlogPost

class IndexView(generic.TemplateView):
    model = BlogPost
    template_name = "blog/index.html"

