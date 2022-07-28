# 추가 실습 4
def bonus_test_4():
    data = input('숫자로 이루어진 문자열을 입력하세요.: ')

    if data[0] == '0':
        result = data[0] + '+'

    else:
        result = data[0] + '*' 

    for i in range(1, len(data) - 1):
        if data[i] == '0':
            result = result[:-1]
            result = result + '+' + data[i] + '+'

        else:
            result = result + data[i] + '*'


    if data[i] == '0':
        result = result[:-1]
        result = result + '+' + data[len(data) - 1]

    print(f'결과는 {eval(result)}입니다.')