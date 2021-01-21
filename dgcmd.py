import drawgraph
import sys
import os

def show_help():
    print(""" Справка:
              Обязательные параметры:
                -p<путь к файлу> - путь к файлу с данными
                -с<номер колонки> - колонка по которой будет построен график
                                    допускается указание двух таких параметров (второй не обязательно)
                                    Номерация колонок начинается с 0
              Необязательные параметры:
                -o<сдвиг> - сдвиг второго графика по оси У относительно первого
                -nmea - если файл содержит NMEA-подобные строки. Поля "не числа" будут заменены значениями 0

              Пример:
              python dgcmd.py -pmy_data.txt -c1 -c3 -o100 -nmea

                При этом будет построено 2 графика по колонкам 1 и 2 из файла c NMEA данными my_data.txt
    """)

print('DrawGraph', drawgraph.version())

argnum = len(sys.argv)

if argnum < 3:
    print('Ошибка: Не достаточно аргументов')
    show_help()
    quit()

file_path = [False, '']
col_1     = [False, 0]
col_2     = [False, 0]
offset    = [False, 0]
nmea      = False

for i, arg in enumerate(sys.argv):
    if i > 0:
        if arg[0] != '-':
            print('Ошибка: Не верный аргумент', arg,'Все аргументы должны начинаться символом -')
            quit()
        if arg[1] == 'p':
            file_path = [True, arg[2:]]
        elif arg[1] == 'c':
            if col_1[0] is False:
                col_1 = [True, int(arg[2:])]
            else:
                col_2 = [True, int(arg[2:])]
        elif arg[1] == 'o':
            offset = [True, int(arg[2:])]
        elif arg[1:] == 'nmea':
            nmea = True
        else:
            print('Ошибка: неизвестный аргумент', arg)
            quit()

if file_path[0] is False or col_1[0] is False:
    print('Ошибка: отсутствует параметр пути к файлу или номер первой колонки')
    quit()

result = drawgraph.drawgraph(file_path[1], col_1[1], col_2[0], col_2[1], offset[1], nmea)
print(result[1])
