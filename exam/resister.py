from .models import Question
import csv


path = '../exam_app/exam/files/01_aki.csv'
with open(path, encoding='utf-8-sig') as f:
    datas = csv.DictReader(f)
    questions = []
    for data in datas:
        questions.append(data)

for question in questions:
    question_model = Question()
    question_model.question = question['question']
    question_model.title = question['title']
    question_model.filed = question['filed']
    question_model.choice1 = question['choice1']
    question_model.choice2 = question['choice2']
    question_model.choice3 = question['choice3']
    question_model.choice4 = question['choice4']
    question_model.answer = question['answer']
    question_model.url = question['url']
    question_model.save()