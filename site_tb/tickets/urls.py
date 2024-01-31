from django.urls import path
from . import views

urlpatterns = [path('', views.TicketView.as_view()),
               path('<slug:ticket_slug>/', views.TicketDetail.as_view(), name='ticket'),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments')]
