from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
import csv
import random
from .models import Question

QUESTIONS = []
QUESTION_LENGTH = 0
RANDOM_NUMBERS = []
COUNTER = 0
CORRECTS = 0

#ページに表示する回数を計算するクラス
class CountClass():
    def start(self):
        global COUNTER
        COUNTER = 0

    def add(self):
        global COUNTER
        COUNTER += 1

    def reset(self,num):
        global COUNTER
        if COUNTER == num:
            COUNTER = 0

#問題を生成するクラス        
class QuizClass():
    def __init__(self):
        QUESTIONS.clear()
        path = '../exam_app/exam/files/01_aki.csv'
        with open(path, encoding='utf-8-sig') as f:
            datas = csv.DictReader(f)
            for data in datas:
                QUESTIONS.append(data)
        global QUESTION_LENGTH
        QUESTION_LENGTH = len(QUESTIONS)-1
    
    def set_random(self,num):
        RANDOM_NUMBERS.clear()
        while len(RANDOM_NUMBERS) < num:
            x = random.randint(0, QUESTION_LENGTH)
            if not x in RANDOM_NUMBERS:
                RANDOM_NUMBERS.append(x)
             
            
class IndexView(TemplateView):
    template_name = 'exam/index.html'

    def post(self, request, *args, **kwargs):
        quiz = QuizClass()
        quiz.set_random(5)
        counter = CountClass()
        counter.start()
        return redirect('exam:quiz')
        
class TestView(TemplateView):
    template_name = 'exam/test.html'

class QuizView(TemplateView):
    
    counter = CountClass()

    def get(self,request):
        params = QUESTIONS[RANDOM_NUMBERS[COUNTER]]
        self.counter.add()
        print(COUNTER)
        return render(request, 'exam/quiz.html', params)

    
    def post(self,request):
        params = QUESTIONS[RANDOM_NUMBERS[COUNTER-1]]
        name='choice'
        select_num = 0
        for i in range(4):
            if name+str(i+1) in request.POST:
                select_num = i+1
        params['select_num'] = select_num

        if select_num == int(params['answer']):
            params['judgment'] = True
        else:
            params['judgment'] = False

        if COUNTER == 5:
            params['finished'] = True
        else:
            params['finished'] = False

        return render(request, 'exam/answer.html', params)

class QuizResultView(TemplateView):
    def get(self, request, *args, **kwargs):
        qusetion_items = []
        for i in range(len(RANDOM_NUMBERS)):
            qusetion_items.append(QUESTIONS[RANDOM_NUMBERS[i]])
        params = {'list': qusetion_items}
        return render(request, 'exam/result.html',params)

class QuizCreateView(CreateView):
    def get(self, request, index):
        params = QUESTIONS[RANDOM_NUMBERS[index]]
        return render(request, 'exam/create.html',params)
    
    def post(self, request, index):
        print(RANDOM_NUMBERS)
        comprehension = request.POST["Comprehension"]
        QUESTIONS[RANDOM_NUMBERS[index]].pop('select_num')
        QUESTIONS[RANDOM_NUMBERS[index]].pop('judgment')
        QUESTIONS[RANDOM_NUMBERS[index]].pop('finished')
        obj = Question(**QUESTIONS[RANDOM_NUMBERS[index]],comprehension=comprehension)
        obj.save()

        RANDOM_NUMBERS.pop(index)
        qusetion_items = []
        for i in range(len(RANDOM_NUMBERS)):
            qusetion_items.append(QUESTIONS[RANDOM_NUMBERS[i]])
        params = {'list': qusetion_items}
        print(index)
        
        
        return render(request, 'exam/result.html',params)

class QuizListView(ListView):
    template_name = 'exam/list.html'
    model = Question
    context_object_name = 'list'
    

class QuizDetailView(DetailView):
    template_name = 'exam/detail.html'
    model = Question


class QuizDeleteView(DeleteView):
    template_name = 'exam/delete.html'
    model = Question
    success_url = reverse_lazy('exam:list')
    

class QuizUpdateView(TemplateView):
    template_name = 'exam/update.html'
    
    def post(self, request, pk):
        comprehension = request.POST["Comprehension"]
        obj = Question.objects.get(pk=pk)
        obj.comprehension = comprehension
        obj.save()
        return redirect('exam:list')
    
    
