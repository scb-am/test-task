from django.conf.urls import url
#from .views import Index
from . import views

urlpatterns = [
    url(r'^$', views.show_tasks, name='show_tasks'),
    url(r'^change_table/$', views.change_table, name='change_table'),
    url(r'^add_topic/$', views.add_topic, name='add_topic'),
    url(r'^del_topic/$', views.del_topic, name='del_topic'),
    url(r'^edit/(?P<id>\d+)/', views.edit, name='edit'),
]
