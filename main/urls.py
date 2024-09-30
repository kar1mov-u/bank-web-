from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'main-page' ),
    path('login',views.login_view, name ='login-page'),
    path('create-account',views.create_acc,name='create-acc-page'),
    path('logout',views.log_out,name='logout-page')
]