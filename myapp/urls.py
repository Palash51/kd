from django.conf.urls import url
from django.conf.urls import include
from myapp import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
	
    #url(r'^find/$',views.use_api, name="search"),
    url(r'^$', views.home, name = "homepage"),
    url(r'^cotton/$', views.cotton, name = "cotton"),
    url(r'^contact/$', views.contact, name = "contact"),
    url(r'^about/$', views.about, name = "about"),
    url(r'^registration/$', views.registration, name = "registration"),

]
