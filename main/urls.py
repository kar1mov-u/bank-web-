from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'main-page' ),
    path('login',views.login_view, name ='login-page'),
    path('create-account',views.create_acc,name='create-acc-page'),
    path('logout',views.log_out,name='logout-page'),
    path('profile',views.profile, name= 'profile-page'),
    path('bank-cards',views.view_cards,name="bank-cards-page"),
    path('add-card', views.add_card, name='add-card-page'),
    path('support', views.support, name = "support-page"),
    path('transfer', views.transfer_money, name="transfer-page")
    
]