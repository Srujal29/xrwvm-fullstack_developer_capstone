from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from djangoapp import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),

    # Root microservice endpoints for cURL test suite
    path('fetchDealers', app_views.fetch_dealers, name='fetch_dealers'),
    path('fetchDealers/', app_views.fetch_dealers, name='fetch_dealers_slash'),
    path('fetchDealers/<str:state>', app_views.fetch_dealers, name='fetch_dealers_state'),
    path('fetchDealers/<str:state>/', app_views.fetch_dealers, name='fetch_dealers_state_slash'),
    path('fetchDealer/<int:dealer_id>', app_views.fetch_dealer_by_id, name='fetch_dealer_by_id'),
    path('fetchDealer/<int:dealer_id>/', app_views.fetch_dealer_by_id, name='fetch_dealer_by_id_slash'),
    path('fetchReviews/dealer/<int:dealer_id>', app_views.fetch_dealer_reviews, name='fetch_dealer_reviews'),
    path('fetchReviews/dealer/<int:dealer_id>/', app_views.fetch_dealer_reviews, name='fetch_dealer_reviews_slash'),

    # Static HTML pages
    path('', TemplateView.as_view(template_name="Home.html")),
    path('about', TemplateView.as_view(template_name="About.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact', TemplateView.as_view(template_name="Contact.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),

    # React App routes
    path('login', TemplateView.as_view(template_name="index.html")),
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('register', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="index.html")),
    path('dealers', TemplateView.as_view(template_name="index.html")),
    path('dealers/', TemplateView.as_view(template_name="index.html")),
    path('dealer/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),
    path('dealer/<int:dealer_id>/', TemplateView.as_view(template_name="index.html")),
    path('postreview/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),
    path('postreview/<int:dealer_id>/', TemplateView.as_view(template_name="index.html")),
    path('add_review/<int:dealer_id>', TemplateView.as_view(template_name="index.html")),
    path('add_review/<int:dealer_id>/', TemplateView.as_view(template_name="index.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)