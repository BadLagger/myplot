# Информация о версии
version = 1.0
print('DrawGraph ' + str(version))

# Проверка на наличие входящих аргументов
import sys
argnum = len(sys.argv)
if argnum <= 2:
    print('Не достаточно аргументов')
    quit()

# Первый аргумент (обязательный) - путь к файлу
file_path = sys.argv[1]
  # Проверка существования файла
import os
if os.path.exists(file_path) is False:
    print('Некорректный путь к файлу или файла не существует!')
    quit()

# Второй аргумент (обязательный) - номер колонки для отрисовки
col_num = int(sys.argv[2])
# Третий аргумент (опционально) - номер колонки для отрисовки второго графика
second_col = False
if argnum >= 4:
    second_col = True
    col_num2 = int(sys.argv[3])
# Четвёртый аргумент (опционально) - смещение второго графика
offset = 0
if argnum == 5:
    offset = int(sys.argv[4])



# Работа с файлом
array = []
with open(file_path) as file:
    line = file.readline().split()

    # Проверка выбраной колонки
    if ( len(line) - 1 ) < col_num:
      print('Выбрана не существующая колонка')
      quit()

    while line:
      for i in range( len(line) ):
        line[i] = float( line[i] )
      array.append( line )
      line = file.readline().split()



# Рисуем график
import matplotlib.pyplot as plt
x = list( range( len(array) ) )       # шкала Х равна количеству отсчётов
y = [ row[col_num] for row in array ] # выбор колонки в качестве Y
plt.plot(x, y)                        # запомнить первую гистограмму

# Отрисовка второго графика (если задан)
if second_col is True:
    y2 = [ row[col_num2] for row in array ]  # выбор колонки в качестве Y
    if offset != 0:                             # если задано смещение, то прибавить ко всем элементам Y это смещение
        y2 = list(map(lambda n: n + offset, y2))
    plt.plot(x, y2)

plt.show()

# Конец
print('Отладка: завершение программы')
