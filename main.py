count = int(input('Введите количество чисел: '))
consecution = []
back_consecution = []

for i in range(1, count + 1):
    number = int(input(f'{i}-е число: '))
    consecution.append(number)
for i in range(1, count + 1):
    back_consecution.append(consecution[-i])


for i in range(0, count):
    if consecution == back_consecution:
        print('\nМножество симметрично!')
        break
    else:
        if consecution[i] == back_consecution[i]:
            back_consecution.remove(back_consecution[i])
            continue
        else:
            print(f'Нужно добавить {len(back_consecution)} чисел\nСами числа {back_consecution}')
            consecution.extend(back_consecution)
            break

print(consecution)
