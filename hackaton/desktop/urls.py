from django.urls import path
from . import views
from django.urls import path, include
# from qr_code import urls as qr_code_urls
app_name = 'desktop'


urlpatterns = [
    # path(r'^qr_code/', include(qr_code_urls, namespace="qr_code")),
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('mobile_qr/', views.mobile_qr, name='mobile_qr'),
    path('result/', views.result, name='result')
]
