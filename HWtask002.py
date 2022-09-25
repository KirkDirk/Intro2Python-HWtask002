# Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат

x = input('Введите x(0 или 1): ')
y = input('Введите y(0 или 1): ')
z = input('Введите z(0 или 1): ')

leftside = not(x or y or z)
rightside = not(x) and not(y) and (z)
if leftside == rightside: print('Истинно!')
else: print('Ложно!')


