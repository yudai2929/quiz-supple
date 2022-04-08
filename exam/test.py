import csv
import random

path = '../exam_app/exam/files/01_aki.csv'
with open(path, encoding='utf-8-sig') as f:
    datas = csv.DictReader(f)
    questions = []
    for data in datas:
        questions.append(data)

num = 5
xs = []
for i in range(num):
    flag = 0
    while flag == 0:
        x = random.randint(0, len(questions)-1)
        if not(x in xs):
            xs.append(x)
            flag = 1
            
    print('question.{}: {}\n'.format(i+1,questions[x]['question']))
    print('choice1 {}'.format(questions[x]['choice1']))
    print('choice2 {}'.format(questions[x]['choice2']))
    print('choice3 {}'.format(questions[x]['choice3']))
    print('choice4 {}'.format(questions[x]['choice4']))
    print('\nPlease serect your answer!\n')

    my_choice = input()
    if my_choice == questions[x]['answer']:
        print('good!')
    else:
        print('bad!')
    

