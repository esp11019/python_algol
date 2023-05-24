
counter = 0
for n in range(2, 1000):
    for i in range(2, n):
        counter += 1
        if n % i == 0:
            break
    else:
        print(n)
print("나눗셈을 실행한 횟수 : {}".format(counter))
