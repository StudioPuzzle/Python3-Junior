#Определить, есть ли в заданной строке заданный символ.
st = input('Введите строку ')
sim = input('Введите символ ')
if sim in st:
	print('Да, такой символ имеется')
else:
	print('Нет, такого символа нет')
