from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'backendcore_api'
urlpatterns = [

    # If user not logged in
    path('', views.homepage, name='homepage'),

    # Registration
    # path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/', views.profile_request, name='profile'),
    # path('profile/edit/', views.profile_edit, name='profile_edit'),


    # Profile API
    path('ratings/', include('star_ratings.urls', namespace='ratings')),

    # path('serviceregistration/', views.service_register_request, name='serviceregistration')
    path('contractor/', include('Contractor.urls')),
    # path('contractor/', include('django.contrib.auth.urls')),
    # path('home/contractor/', include('Contractor.urls')),
    # path('home/contractor/homepage/', views.contractor_homepage, name='Contractor_homepage'),
    # #path('home/contractor/login/', include('Contractor.urls', namespace='Contractor_login')),
    # path('contractor/login', views.contractor_login_request, name='Contractor_login'),

    # Customer path
    path('request_service/', views.request_service, name = 'request_service'),
    path('request_service/<int:customer_id>/delete/', views.delete_service_request, name='delete_service_request'),
    # path('customer/', include('django.contrib.auth.urls')),
    # path('home/customer/', include('Customer.urls')),
    # path('home/customer/homepage/', views.customer_homepage, name='Customer_homepage'),
    # #path('home/customer/login/', include('Customer.urls', namespace='Customer_login')),
    # path('customer/login', views.customer_login_request, name='Customer_login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





