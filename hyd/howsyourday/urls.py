from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'upvote/(?P<color_id>[0-9]+)', views.upvote, name='upvote')
]
