questions = {
    'Сколько спутников у Сатурна?': '148',
    'Самый большой спитник Солнечной системы?': 'Ганимед'
}

score = 0

for q, a in questions.items():
    user_answer = input(q + ' ')
    if user_answer.lower() == a.lower():
        print('Правильно!')
        score += 1

    else:
        print('Неверно!')

print(f'Ваш результат: {score} из {len(questions)}')
