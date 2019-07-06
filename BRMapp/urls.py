from django.conf.urls import url
from BRMapp import views

urlpatterns = [
    url('^new-book', views.new_book),
    url('^add-book', views.add_book),
    url('^view-book', views.view_book),
    url('^edit-book', views.edit_book),
    url('^delete-book', views.delete_book),
    url('^search-book', views.search_book),
    url('^search', views.search),
    url('^edit', views.edit),
]
