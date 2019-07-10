from django.shortcuts import render
from BRMapp.models import Books
from BRMapp.forms import NewBookForm, Search
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@never_cache
def user_login(request):
    data = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect('/brmapp/view-book')
        else:
            data['error'] = '!Wrong UserName or Password'
            return render(request, 'login_page.html', data)
    else:
        return render(request, 'login_page.html', data)


@never_cache
@login_required(login_url='/brmapp/user-login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/brmapp/user-login')


@never_cache
@login_required(login_url='/brmapp/user-login')
def new_book(request):
    form = NewBookForm()
    username = request.session['username']
    return render(request, 'newbook.html', {'form': form, 'username': username})


@never_cache
@login_required(login_url='/brmapp/user-login')
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


@never_cache
@login_required(login_url='/brmapp/user-login')
def view_book(request):
    book = Books.objects.order_by('price')
    username = request.session['username']
    return render(request, 'view_book.html', {'book': book, 'username': username})


@never_cache
@login_required(login_url='/brmapp/user-login')
def edit_book(request):
    book = Books.objects.get(id=request.GET['bookid'])
    fields = {'title': book.title, 'author': book.author, 'price': book.price, 'publisher': book.publisher}
    form = NewBookForm(initial=fields)
    username = request.session['username']
    return render(request, 'edit_book.html', {'form': form, 'book': book, 'username': username})


@never_cache
@login_required(login_url='/brmapp/user-login')
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


@never_cache
@login_required(login_url='/brmapp/user-login')
def delete_book(request):
    book = Books.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/brmapp/view-book')


@never_cache
@login_required(login_url='/brmapp/user-login')
def search_book(request):
    form = Search()
    username = request.session['username']
    return render(request, 'search_book.html', {'form': form, 'username': username})


@never_cache
@login_required(login_url='/brmapp/user-login')
def search(request):
    if request.method == 'POST':
        form = Search(request.POST)
        book = Books.objects.filter(title__icontains=form.data['title'])
        book = book.order_by('price')
        username = request.session['username']
        return render(request, 'search_book.html', {'book': book, 'form': form, 'username': username})
