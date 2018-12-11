# accounts/urls.py
from django.urls import path
from .views import objectApprove
from . import views
from django.conf.urls import url

urlpatterns = [
    #url('events', views.EventsView, name='events'),
    #path('events/', views.EventsView, name='events'),
    #path('events/', include('events.urls'))
    #path('mine/', MyView.as_view(), name='my-view'),
    #url(r'^(?P<object_id>[0-9]+)/delete_answer/$', views.objectDelete, name='delete_object')
    #path('^events/approve/<slug:object_id>',objectApprove, name="approve"),
]

