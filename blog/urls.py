from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='home'),
                  path('posts/', views.post_list, name='post_list'),
                  path('posts/<str:pk>', views.post_detail, name='post_detail'),
                  path('python/', views.python, name='python'),
                  path('django/', views.django, name='django'),
                  path('flask/', views.flask, name='flask'),
                  path('pyramid/', views.pyramid, name='pyramid'),
                  path('rest_framework/', views.rest_framework, name='rest_framework'),
                  path('javascript/', views.javascript, name='javascript'),
                  path('react/', views.react, name='react'),
                  path('node/', views.node, name='node'),
                  path('angular/', views.angular, name='angular'),
                  path('html/', views.html, name='html'),
                  path('css/', views.css, name='css'),
                  path('bootstrap/', views.bootstrap, name='bootstrap'),
                  path('databases/', views.databases, name='databases'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
