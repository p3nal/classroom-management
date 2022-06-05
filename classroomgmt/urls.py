from django.urls import path
from . import views

app_name = 'classroomgmt'
urlpatterns = [
        # /index/
        path('', views.index, name='index'),
        path('<int:class_id>/', views.book, name='book'),
        path('logout/', views.logout_view, name='logout'),
        path('myreservations/', views.myreservations, name='myreservations'),
        path('myreservations/<int:class_id>/', views.unbook, name='unbook')
        # TODO
]
