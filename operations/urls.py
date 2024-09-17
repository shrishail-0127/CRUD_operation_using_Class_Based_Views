from django.urls import path
from operations.views import home,BookCreateView,BookListView,BookUpdateView,BookDetailView,BookDeleteView

urlpatterns = [

    path('',home.as_view(), name='myview'),
    path('book-form/',BookCreateView.as_view(), name='book-form'),
    path('book-list/',BookListView.as_view(), name="book-list"),
    path('book-detail/<int:pk>/',BookDetailView.as_view(),name='book-detail'),
    path('book-update/<int:pk>/',BookUpdateView.as_view(),name='book-update'),
    path('book-delete/<int:pk>/',BookDeleteView.as_view(),name='book-delete'),
]