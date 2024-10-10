import random
def guess_number():
    while True:
        min = input('最小値を入力してください。')
        if min.isdigit():
            break
        print('入力された値は数字ではありません。')
    while True:
        max = input('最大値を入力してください。')
        if max.isdigit():
            break
        print('入力された値は数字ではありません。')

    result = random.randint(int(min), int(max))
    true_sentence = f'正解です。答えは{result}です。'
    false_sentence = '不正解です。別の回答を入力してください。'

    while True:
        answer = (input('生成された数字を予測してください。'))
        if answer.isdigit():
            if result == int(answer):
                print(true_sentence)
                break
            else:
                print(false_sentence)
        else:
            print('入力された値は数字ではありません。')
