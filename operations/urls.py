from django.urls import path
from operations.views import MyView,BookCreateView,BookListView

urlpatterns = [

    # path('',MyView.as_view(), name='myview'),
    path('book-form/',BookCreateView.as_view(), name='book-form'),
    path('',BookListView.as_view(), name="book-list"),
]