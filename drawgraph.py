import os
from matplotlib import pyplot

Version = 2.2

def drawgraph(file_path, col_1_num, second_line = False, col_2_num = 0, col_2_offset = 0, nmea=False):
    if os.path.exists(file_path) is False:
        return [False, 'Некорректный путь к файлу или файла не существует!']

    array = []
    with open(file_path) as file:
       line = file.readline()

       line_num = line.split() if nmea is False else line.split(',')

       # Проверка выбраной колонки
       if (( len(line_num) - 1 ) < col_1_num) or ( len(line_num) - 1 ) < col_2_num:
         return [False, 'Выбрана не существующая колонка']

       while line:
         for index, element in enumerate(line_num):
             element = element.strip().strip('\n')
             try:
                 line_num[index] = float( element )
             except Exception as e:
                 line_num[index] = 0
         array.append( line_num )
         line = file.readline()
         line_num = line.split() if nmea is False else line.split(',')

    x = list( range( len(array) ) )       # шкала Х равна количеству отсчётов
    y = [ row[col_1_num] for row in array ] # выбор колонки в качестве Y
    pyplot.plot(x, y)                        # запомнить первую гистограмму

    if second_line is True:
        y2 = [ row[col_2_num] for row in array ]  # выбор колонки в качестве Y
        if col_2_offset != 0:                             # если задано смещение, то прибавить ко всем элементам Y это смещение
            y2 = list(map(lambda n: n + col_2_offset, y2))
        pyplot.plot(x, y2)

    pyplot.show()

    return [True, 'Обработка завешена успешно!']

def version():
    return Version
