from django.urls import path

from web import views

app_name = 'web'
urlpatterns = [
    path('message/leave/', views.leave_message, name='leave_message'),
    path('message/list/', views.message_list, name='message_list'),
]
