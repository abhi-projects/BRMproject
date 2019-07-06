from django.shortcuts import render
from BRMapp.models import Books
from BRMapp.forms import NewBookForm, Search
from django.http import HttpResponse, HttpResponseRedirect


def new_book(request):
    form = NewBookForm()
    return render(request, 'newbook.html', {'form': form})


def add_book(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST)
        book = Books()
        book.title = form.data['title']
        book.author = form.data['author']
        book.price = form.data['price']
        book.publisher = form.data['publisher']
        book.save()
        return HttpResponseRedirect('/brmapp/view-book')


def view_book(request):
    book = Books.objects.all()
    return render(request, 'view_book.html', {'book': book})


def edit_book(request):
    book = Books.objects.get(id=request.GET['bookid'])
    fields = {'title': book.title, 'author': book.author, 'price': book.price, 'publisher': book.publisher}
    form = NewBookForm(initial=fields)
    return render(request, 'edit_book.html', {'form': form, 'book': book})


def edit(request):
    if request.method == 'POST':
        book = Books()
        form = NewBookForm(request.POST)
        book.id = request.POST['bookid']
        book.title = form.data['title']
        book.author = form.data['author']
        book.price = form.data['price']
        book.publisher = form.data['publisher']
        book.save()
        return HttpResponseRedirect('/brmapp/view-book')


def delete_book(request):
    book = Books.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/brmapp/view-book')


def search_book(request):
    form = Search()
    return render(request, 'search_book.html', {'form': form})


def search(request):
    if request.method == 'POST':
        book_list = []
        form = Search(request.POST)
        book = Books.objects.all()
        for item in book:
            if form.data['title'].lower() in item.title.lower():
                book_list.append(item)
        return render(request, 'search_book.html', {'book_list': book_list, 'form': form})
