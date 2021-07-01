from django.urls import path
from . import views
from django.conf.urls import url
from .views import AccountformDetailView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^(?P<pk>[\w.@+-]+)/$',
        AccountformDetailView.as_view(template_name='account_detail.html'), name='account_detail'),
]