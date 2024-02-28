from django.urls import path
from . import views
from .views import predict_salary,make_prediction


urlpatterns = [
    path('',views.homee,name='homee'),
    path('user_login/',views.user_login,name='user_login'),
    # path('logout/', views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('About/',views.About,name='About'),
    path('Contact/',views.Contact,name='Contact'),
    path('Service/',views.Service,name='Service'),
    path('home2/',views.predict_salary,name="predict_salary"),
    path('results/',make_prediction, name='make_prediction'),
    # Add more URL patterns as needed
]