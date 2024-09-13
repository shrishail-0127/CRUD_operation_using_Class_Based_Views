from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Book

# Create your views here.

class MyView(View):

    def get(self,request):
        return HttpResponse("Home View")
    


class BookCreateView(CreateView):
    model = Book
    fields = ['name','description','author','pages']
    success_url = reverse_lazy('book-list')


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'