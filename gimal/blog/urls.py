from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^post/create/$', views.PostCreate.as_view(), name="post-create"),
    url(r'^post/(?P<pk>\d+)/commentcreate/$', views.CommentCreate.as_view(), name="comment-create"),
]
