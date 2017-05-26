from django.views.generic import ListView, DetailView

from core.models import News


class NewsListView(ListView):
    template_name = 'core/news_list.html'
    model = News
    paginate_by = 10


class NewsDetailView(DetailView):
    template_name = 'core/news_detail.html'
    model = News
