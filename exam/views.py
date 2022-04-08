from curses import reset_prog_mode
import re
from django.shortcuts import render
from django.views.generic import TemplateView
import csv
import random
from .models import Question


#ページに表示する回数を計算するクラス
class CountClass():
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def reset(self,num):
        if self.count == num:
            self.count = 0
        
class QuizClass():
    def __init__(self):
        path = '../exam_app/exam/files/01_aki.csv'
        with open(path, encoding='utf-8-sig') as f:
            datas = csv.DictReader(f)
            self.questions = []
            for data in datas:
                self.questions.append(data)
        self.length = len(self.questions)-1

# Create your views here.
class IndexView(TemplateView):
    template_name = 'exam/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context


class QuizView(TemplateView):
    
    counter = CountClass()
    quiz = QuizClass()
    questions = quiz.questions
    length = quiz.length
    random_nums = []
    def __init__(self):
        num = 5
        while len(self.random_nums) < num:
                x = random.randint(0, self.length)
                if not x in self.random_nums:
                    self.random_nums.append(x)

        print(self.random_nums)

    def get(self,request):
        self.counter.add()
        params = self.questions[self.random_nums[self.counter.count%5]]
        return render(request, 'exam/quiz.html', params)

    
    def post(self,request):
        self.counter.reset(5)
        params = self.questions[self.random_nums[self.counter.count%5]]
        name='choice'
        for i in range(4):
            if name+str(i+1) in request.POST:
                select_num = i+1
        params['select_num'] = select_num

        if select_num == int(params['answer']):
            params['judgment'] = '正解！'
        else:
            params['judgment'] = '不正解！\n正解は{}です'.format(params['answer'])


        return render(request, 'exam/answer.html', params)

