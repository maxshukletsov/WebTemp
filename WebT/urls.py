from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.graph_temp, name='TData'),
    url(r'^(?P<pk>[\w.@+-]+)/$', views.graph_temp, name='TData'),
    path('<int:pk>/<int:days>days/', views.graph_temp, name='TDataF'),
    path('edit/<int:pk>/', views.sensor_edit, name='sensor_edit'),
    path('delete/<int:pk>/', views.sensor_delete, name='sensor_delete'),
]
