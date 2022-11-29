lines_num = int(input())

for num in range(lines_num):
    text1, text2 = input().split('|')
    sum_text , name = text1.split('@')
    some, age_sum = text2.split('#')
    age , other = age_sum.split('*')
    print(f'{name} is {age} years old.')