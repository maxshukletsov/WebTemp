from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.graph_temp, name='TData'),
    # path('new', views.add_new_sensor, name='add_new_sensor'),
    url(r'^(?P<pk>[\w.@+-]+)/$', views.graph_temp, name='TData'),
    path('<int:pk>/<int:days>days/', views.graph_temp, name='TDataF'),
    #url(r'^(?P<pk>[\w.@+-]+)/(?P<date1>[\d{4}-\d{2)-\d{2}])/$', views.graph_temp, name='TDataD'),
    path('edit/<int:pk>/', views.sensor_edit, name='sensor_edit'),
    path('delete/<int:pk>/', views.sensor_delete, name='sensor_delete'),
]
