# Информация о версии
version = 1.0
print('DrawGraph ' + str(version))

# Проверка на наличие входящих аргументов
import sys
if len(sys.argv) <= 2:       
    print('Не достаточно аргументов')
    quit()

# Первый аргумент - путь к файлу 
file_path = sys.argv[1]
col_num = int(sys.argv[2])

# Проверка существования файла
import os
if os.path.exists(file_path) is False:
    print('Некорректный путь к файлу или файла не существует!')
    quit()

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

    
#print(array)

# Рисуем график
import matplotlib.pyplot as plt
x = list( range( len(array) ) )
#print( x )
y = [ row[col_num] for row in array ]
#print( y )
plt.plot(x, y)
plt.show()

# Конец    
print('Отладка: завершение программы')

