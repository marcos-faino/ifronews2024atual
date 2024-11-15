from django.views.generic import TemplateView, ListView, DetailView

from news.models import New


class IndexView(ListView):
    template_name = 'index.html'
    queryset = New.objects.filter(status='publicado').all()
    context_object_name = 'news'
    paginate_by = 3


class NewDetailView(DetailView):
    template_name = 'new.html'
    model = New
    context_object_name = 'new'


class SobreView(TemplateView):
    template_name = "about.html"