from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('index',views.IndexView.as_view(),name='index'),
    path('quiz',views.QuizView.as_view(),name='quiz'),
    path('test',views.TestView.as_view(),name='test'),
    path('result',views.QuizResultView.as_view(),name='result'),
    path('create/<int:index>',views.QuizCreateView.as_view(),name='create'),
    path('list',views.QuizListView.as_view(),name='list'),
    path('detail/<int:pk>',views.QuizDetailView.as_view(),name='detail'),
    path('delete/<int:pk>',views.QuizDeleteView.as_view(),name='delete'),
    path('update/<int:pk>',views.QuizUpdateView.as_view(),name='update'),
]