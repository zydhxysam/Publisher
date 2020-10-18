from django.urls import re_path
from publisher_list import views

urlpatterns = [
    re_path(r'^all_publisher/$', views.publisher_list, name='all_pub'),
    re_path(r'^publisher_add/$', views.publisher_add),
    re_path(r'^publisher_delete/$', views.publisher_delete, name='pub_del'),
    re_path(r'^publisher_edit/$', views.publisher_edit),
    re_path(r'^book/$',views.book, name='book'),
    re_path(r'^book/add/$', views.book_add.as_view(), name='book_add'),
    re_path(r'^book/edit/(\d+)$', views.book_edit.as_view(), name='book_edit'),
    re_path(r'^book/del/(\d+)$', views.book_del, name='book_del'),
]