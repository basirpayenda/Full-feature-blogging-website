from django.urls import path
from .views import newsletter_subscribe, newsletter_unsubscribe, send_newsletter


app_name = 'newsletter'
urlpatterns = [
    path('newsletter-subscribe/', newsletter_subscribe, name='subscribe'),
    path('newsletter-unsubscribe/', newsletter_unsubscribe, name='unsubscribe'),
    path('newsletter-subscribe-send/',
         send_newsletter, name='send_newsletter'),
]
