ЗАДАНИЕ:

С использованием любого языка программирования или командного (скриптового) файла оболочки (Windows или Linux) написать программы (скрипты) для формирования файлов с результатами обработки прилагаемых файлов:
(допустимо использование готового инструментария для пакетного поиска в файлах, т.е. можно обойтись без программирования, но результат должен быть воспроизводим, например, при помощи "записи" макросов на основании действий пользователя)
2. sc_device.log
2.1. Все строки, содержащие подстроку вида "grabber : ntc reply = NTC,0000,0370,TTTT" (TTTT - числовой параметр), с результатом сравнения числового параметра со значением, передаваемым в скрипт (программу): OK, если он больше или равен, ERR - если меньше.
3. sc_device_v.log
3.1. сформировать пары строк (для всех ID):
    - первая строка содержит подстроку вида "info: <BOARD> : Sending command: <ID>", <BOARD> передается параметром скрипта (значения: grabber, wash, tip, reagents)
	- вторая строка - следующая, содержащая подстроку вида "info: <BOARD> : Got reply: <ID+1> NAK"
4. sc_runtime.log
4.1. сформировать пары строк (для всех ID):
    - первая строка содержит подстроку вида "info: Slot to run: <ID>"
    - вторая строка - следующая, содержащая подстроку вида "info: Slot to run: <ID>"

ЗАПУСК:

Скрипты реализованы на языке программирования Python 3.10
Для работы скриптов в системе должен быть установлен Python 3 версии не ниже 3.7
Как запустить скрипты через консоль
Запуск t2_1. Чтобы запустить файл в консоли надо набрать команду python <путь до файла t2_1.py на устройстве c:\script\t2_1.py> <TTTT - числовой параметр> <путь до открываемого файла sc_device.log на устройстве> 
Запуск t3_1. Чтобы запустить файл в консоли надо набрать команду python <путь до файла со cкриптом на устройстве> <путь до открываемого в скрипте файла sc_device_v.log на устройстве>
Результат выполнения скрипта t3_1.py появится в файле out_3_1.txt, расположенном в той же папке, что и скрипт t3_1.py.
Запуск t4_1. Чтобы запустить файл в консоли надо набрать команду python <путь до файла со cкриптом на устройстве> <путь до открываемого в скрипте файла sc_runtime.log на устройстве>
Результат выполнения скрипта t4_1.py появится в файле out_4_1.txt, расположенном в той же папке, что и скрипт t4_1.py. 









