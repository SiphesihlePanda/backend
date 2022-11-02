from django import views
from django.urls import path
from .views import contactView, displayTime, loginView
from blog.views import book_list, post_list, post_detail

#create a name space
app_name = 'blog'


urlpatterns = [
    path("books_list/",book_list),
    path("",post_list),
    path("contact/",contactView),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path("login/",loginView,name='login'),
]