from django.views.generic import TemplateView
from .models import Book


class HomeView(TemplateView):
    model = Book
    template_name = 'dashboard/home.html'
    context_object_name = 'books'
    queryset = Book.objects.all()
    paginate_by = 10
