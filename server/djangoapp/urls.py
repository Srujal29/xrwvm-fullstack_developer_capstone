from django.urls import path
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Auth
    path('registration', views.registration, name='registration'),
    path('registration/', views.registration, name='registration_slash'),
    path('register', views.registration, name='register'),
    path('register/', views.registration, name='register_slash'),
    path('login', views.login_user, name='login'),
    path('login/', views.login_user, name='login_slash'),
    path('logout', views.logout_request, name='logout'),
    path('logout/', views.logout_request, name='logout_slash'),

    # Dealers & Reviews for React UI
    path('get_cars', views.get_cars, name='getcars'),
    path('get_cars/', views.get_cars, name='getcars_slash'),
    path('get_dealers', views.get_dealers, name='get_dealers'),
    path('get_dealers/', views.get_dealers, name='get_dealers_slash'),
    path('get_dealers/<str:state>', views.get_dealers, name='get_dealers_by_state'),
    path('get_dealers/<str:state>/', views.get_dealers, name='get_dealers_by_state_slash'),
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details_slash'),
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews_slash'),
    path('add_review', views.add_review, name='add_review'),
    path('add_review/', views.add_review, name='add_review_slash'),

    # Sentiment analyzer
    path('analyze/<str:text>', views.analyze_sentiment, name='analyze_sentiment'),
    path('analyze/<path:text>', views.analyze_sentiment, name='analyze_sentiment_path'),
]