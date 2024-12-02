team1 = "Мастера кода"
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
#tasks_total = 82
#time_avg = 45.2

print('"В команде %(name)s, участников: %(num)s!"' % {'name': team1, 'num': team1_num})
print('"Итого сегодня в командах участников: %(num1)s и %(num2)s!"' % {'num1': team1_num, 'num2': team2_num})

print('"Команда {} решила задач: {}!"'.format(team2, score_2))
print('"{} решили задачи за {} c!"'.format(team2, round(team2_time, 1)))

print(f'"Команды решили {score_1} и {score_2} задач."')

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        print(f'"Победа команды {team1}!"')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        print(f'"Победа команды {team2}!"')
    else:
        print(f'"Ничья!"')

result = challenge_result()

print(f'"Сегодня было решено {score_1 + score_2} задач, в среднем по '
      f'{round((team1_time + team2_time)/(score_1 + score_2),1)} секунды на задачу!."')