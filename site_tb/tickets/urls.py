from django.urls import path
from . import views

urlpatterns = [path('', views.TicketView.as_view()),
               path('<int:pk>/', views.TicketDetail.as_view()),
               path('answer/', views.QuestionDetail.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments')]
