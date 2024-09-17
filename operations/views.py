from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView,DetailView,DeleteView
from .models import Book

# Create your views here.

class home(View):

    def get(self,request):
        return HttpResponse("Home View")
    


class BookCreateView(CreateView):
    model = Book
    fields = ['name','description','author','pages']
    success_url = reverse_lazy('book-list')


class BookListView(ListView):
    model = Book
    template_name = 'operations/book_list.html'
    context_object_name = 'books'



class BookDetailView(DetailView):
    model = Book
    template_name = 'operations/book_detail.html'
    context_object_name = 'book'




class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'operations/book_update.html'
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'operations/book_delete_confirm.html'
    success_url = reverse_lazy('book-list')
   