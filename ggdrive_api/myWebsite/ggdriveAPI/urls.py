from django.urls import path, include
from . import views

resources = [
    'About',
    'Changes',
    'Channels',
    'Comments',
    'Files',
    'Permissions',
    'Replies',
    'Revisions',
    'Teamdrives'
]

app_name = 'ggdriveAPI'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('changes/', views.changes, name='changes'),
    path('channels/', views.channels, name='channels'),
    path('comments/', views.comments, name='comments'),
    path('files/', views.files, name='files'),
    path('permissions/', views.permissions, name='permissions'),
    path('replies/', views.replies, name='replies'),
    path('revisions/', views.revisions, name='revisions'),
    path('teamdrives/', views.teamdrives, name='teamdrives'),
]