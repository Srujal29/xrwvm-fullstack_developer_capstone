from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('registration/', views.registration, name='registration_slash'),
    path('login', views.login_user, name='login'),
    path('login/', views.login_user, name='login_slash'),
    path('logout', views.logout_request, name='logout'),
    path('logout/', views.logout_request, name='logout_slash'),
    path('get_cars', views.get_cars, name='getcars'),
    path('get_cars/', views.get_cars, name='getcars_slash'),
    path('get_dealers', views.get_cars, name='get_dealers'),
    path('get_dealers/', views.get_cars, name='get_dealers_slash'),
    path('get_dealers/<str:state>', views.get_cars, name='get_dealers_by_state'),
    path('get_dealers/<str:state>/', views.get_cars, name='get_dealers_by_state_slash'),
    path('dealer/<int:dealer_id>', views.get_cars, name='dealer_details'),
    path('dealer/<int:dealer_id>/', views.get_cars, name='dealer_details_slash'),
    path('add_review', views.get_cars, name='add_review'),
    path('add_review/', views.get_cars, name='add_review_slash'),
]