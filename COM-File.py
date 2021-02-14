import serial															# импорт библиотеки
import time																# импорт библиотеки

print("Данный скрипт принимает данные из COM-порта")
print("и записывает их файл с заданным именем.")
print("Предварительно требуется задать имя файла, номер COM-порта и число строк.")
print("-------------------------------------------------------------\n")

name_file = None
new_com = None
new_strok = None
num_port = '3'
strok = 100
################################################################
while (name_file == None or name_file == ''):
	name_file = input('введите имя файла: ')
name_file = name_file + '.txt'											# имя файла
print("\n")
################################################################
new_com = str(input('введите номер COM-порта, либо нажмите "Enter", по умолчанию COM3: '))
if new_com != '' and new_com != ' ' and new_com != None:
	com_port = 'COM' + new_com											# задаем COM-порт
else:
	com_port = 'COM' + num_port											# задаем COM-порт
print("\n")
################################################################
new_strok = str(input('введите число строк в файле, либо нажмите "Enter", по умолчанию 100: '))
if new_strok != '' and new_strok != ' ' and new_strok != None:
	strok = int(new_strok)												# задаем число строк в файле
print("\n")
################################################################

idcom = []																# пустой массив
i = 0																	# начальный индекс

ser = serial.Serial(
    port = com_port,\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=None)

print("connected to: " + ser.portstr + "\n")

files1 = open(name_file, 'w')											# открываем файл в режиме перезаписи

while (i != strok):
	m = ''																# объявляем строковую переменную
	for line in ser.readline():
		idcom.append(line)
    #time.sleep(1)
	for j in range(len(idcom)):
		if idcom[j] == 48:
			m = m + '0'
		if idcom[j] == 49:
			m = m + '1'
	print(m + "\n")
	files1.write(m +'\n')												# запись в файл
	del(m)																# удаляем строковую переменную
	idcom.clear()														# очищаем массив
	i += 1

files1.close()															# закрываем файл			
print('запись закончена')												# сообщение в консоль
