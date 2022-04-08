from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('index',views.IndexView.as_view(),name='index'),
    path('quiz',views.QuizView.as_view(),name='quiz'),
]