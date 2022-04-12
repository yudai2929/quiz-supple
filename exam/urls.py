from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('index',views.IndexView.as_view(),name='index'),
    path('quiz',views.QuizView.as_view(),name='quiz'),
    path('test',views.TestView.as_view(),name='test'),
    path('result',views.QuizResultView.as_view(),name='result'),
    path('create/<int:index>',views.QuizCreateView.as_view(),name='create')
]