# 추가 실습 3
def bonus_test_3():
    while True:
        left = int(input('left를 입력하세요.: '))
        right = int(input('right를 입력하세요.: '))

        if 1 <= left and left <= right and right <= 1000:
            break

    answer = 0

    for i in range(left, right + 1):
        count = 0
        
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count % 2:
            answer -= i

        else:
            answer += i

    print(f'결과는 {answer}입니다.')