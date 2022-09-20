b=0
print('В чем измеряется сила ?')
print('1). Ньютон')
print('2). Паскаль')
print('3). Джоуль')
a=int(input('Write your answer '))
if a==1:
    print('Your right!')
    b+=1
    print('Youre score is',b,'points')ggggg
else:
    print('Wrong!')
    print('Youre score is', b,'points')
print('Кто Президент России ?')
print('1). Тинькофф')
print('2). Медведев')
print('3). Путин')
a=int(input('Write your answer '))
if a==3:
    print('Your right!')
    b+=1
    print('You are score is',b,'points')
else:
    print('Wrong!')
    print('You are score is', b,'points')
print('В каком году крестили Русь')
print('1). 988')
print('2). 962')
print('3). 1003')
a=int(input('Write you are answer '))
if a==1:
    print('You are right!')
    b+=1
    print('You are score is',b,'points')
else:
    print('Wrong!')
    print('You are score is', b,'points')
print('Сколько законов Ньютона ?')
print('1). 4')
print('2). 3')
print('3). 5')
a=int(input('Write you are answer '))
if a==2:
    print('You are right!')
    b+=1
    print('You are score is',b,'points')
else:
    print('Wrong!')
    print('You are score is', b,'points')
if b==0:
    print('Поздравляю ты ебаный лох')
else:
    print('Congratulations! You are score is',b,'points')

