from django.conf.urls import url
from reletive_urls import views

#template tagging 
app_name='reletive_urls'
urlpatterns = [
    url(r'^reletive/$',views.reletive,name='reletive'),
    url(r'^other/$',views.other,name='other'),
]
