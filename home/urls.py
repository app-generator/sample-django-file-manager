from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('file-manager/', views.file_manager, name='file_manager'),
    re_path(r'^file-manager/(?P<directory>.*)?/$', views.file_manager, name='file_manager'),
    path('delete-file/<str:file_path>/', views.delete_file, name='delete_file'),
    path('download-file/<str:file_path>/', views.download_file, name='download_file'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('save-info/<str:file_path>/', views.save_info, name='save_info'),
]
