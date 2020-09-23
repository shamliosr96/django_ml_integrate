"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from myapp import views
from myproject import settings





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^contactus/', views.contact, name = 'contactus'),
    url(r'^about/', views.about, name = 'about'),
    url(r'^wine/', views.wine, name='wine'),
    url(r'^migration/', views.migration, name='migration'),
    url(r'^car/', views.car, name='car'),
    url(r'^heart/', views.heart, name='heart'),
    url(r'^diabetes/', views.diabetes, name='diabetes'),
    url(r'^Glass/', views.Glass, name='Glass'),
    url(r'^liver/', views.liver, name='liver'),
    url(r'^iris/', views.Iris, name='iris'),
    url(r'^estate/', views.house, name='estate'),
    url(r'^balance/', views.Bscale, name='balance'),
    url(r'^cancer/', views.cancer, name='cancer'),
    url(r'^blood/', views.Bdonate, name='blood'),
    url(r'^happy/', views.mood, name='happy'),
    url(r'^poker/', views.Poker, name='poker'),
    url(r'^haber/', views.haber, name='haber'),
    url(r'^teach/', views.teach, name='teach'),
    url(r'^wheat/', views.wheat, name='wheat'),
    url(r'^creditcard/', views.creditcard, name='creditcard'),
    url(r'^titanic/', views.titanic, name='titanic'),




] + static(settings.STATIC_URL, STATIC_ROOT=settings.STATIC_ROOT)
