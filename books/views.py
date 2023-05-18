from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from books.models import Author, Book, Publisher

# Create your views here.


class BooksModelView(TemplateView):
    template_name = "books/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_list"] = ["Book", "Author", "Publisher"]
        return context


class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


class BookDetail(DetailView):
    model = Book


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher
