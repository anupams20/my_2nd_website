from django.urls import path
from . import views
from .views import signup_view, signup_done

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('login/', views.login_view, name='login'),
    path('hey/', views.hello, name='post_list'),
    path('signup/',signup_view, name='signup'),
    path('signup/done',signup_done, name='signup_done'),
    path('shopping-items/', views.shopping_items_view, name='shopping_items'),
    path('shopping-items/done/', views.shopping_items_done, name='shopping_items_done'),
    path('success/', views.success_view, name='success_url'),
    path('logout/', views.logout_view, name='logout'),
 
    path('password_change/', views.password_change_view, name='password_change'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),
    path('logout_done/', views.logout_done, name='logout_done'),
    path('api/read', views.read, name='read'),
    path('api/create', views.create, name='create'),
    path('api/update', views.update, name='update'),
    path('api/delete', views.delete, name='delete'),
]