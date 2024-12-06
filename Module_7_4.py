team1_num = 5
team2_num = 6
score1 = 42
score2 = 40
team1_time = 18015.2
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = "Победа команды Волшебники данных"

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера Кода"
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = "Победа команды Волшебники данных"
else:
    challenge_result = "Ничья"

# Использование %
result_master = 'В команде Мастера кода участников: %s' % team1_num
result_wizard = "В команде Волшебники данных участников: %s" % team2_num
result = "Итого сегодня в командах участников: %s, и %s" % (team1_num, team2_num)

#Использование format()
metod1 =  "Команда Волшебники данных решила задач: {} !".format(score1)
metod2 =  " Мастра кода решили задачи за {} с !".format(team1_time)

#Использование f-стрoк
metod3 = f'Команды решили {score1} и {score2} задач.'
metod4 = f'Результат битвы: победа команды {challenge_result}!'
metod5 = f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.'
challenge_result

with open ("result.txt","w", encoding='utf-8') as file:
    file.write(result_master + '\n')
    file.write(result_wizard + '\n')
    file.write(result + '\n')
    file.write(metod1 + '\n')
    file.write(metod2 + '\n')
    file.write(metod3 + '\n')
    file.write(metod4 + '\n')
    file.write(metod5 + '\n')