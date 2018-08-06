#normal block


# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
import copy
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
line2 = copy.deepcopy(line)
line3 = copy.deepcopy(line)
def function(a):
    fun_s = str()
    list_f = list()
    for i in a:
        if not i.isupper():
             fun_s =  fun_s + i
        else:
            if fun_s != '':
                list_f.append(fun_s)
                fun_s = str()
            else:
                fun_s = str()
    return(list_f)
print(function(line))

#with re
import re
n = re.split(r'[A-Z]+', line2)
print(n)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line4 = copy.deepcopy(line3)
for i in range(len(line3) - 4):
	if line3[i].islower() and line3[i + 1].islower() and line3[i + 2].isupper() and line3[i + 3].isupper() and line3[i + 4].isupper():
		z = 1
		d = line3[i + 2]
		try:
			while line3[i + 4 + z].isupper():
				d = line3[i + 2: i + 3 + z]
				z += 1
			print(d)
		except:
			print(line3)
n2_2 = re.compile('[a-z]{2}[A-Z]{3,}[a-z]{1}')
res = n2_2.findall(line_4)
for i in range(len(res)):
    res[i] = res[i][2:-3]
print(res)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import random
import re
import os
result = []
f = open("num.txt", 'w')
b = str()
for i in range(1,2051):
    k = str(random.randint(0,9))
    while k == '0' and i == 1:#Убираем вариант с нулем впереди (нам же число надо, а не просто последовательность)
        k = str(random.randint(0,9))
    f.write(k)
f.close()
f = open("num.txt", 'r')
for line in f:
    b = str(line)
b0 = re.compile(r'0{2,}')
b1 = re.compile(r'1{2,}')
b2 = re.compile(r'2{2,}')
b3 = re.compile(r'3{2,}')
b4 = re.compile(r'4{2,}')
b5 = re.compile(r'5{2,}')
b6 = re.compile(r'6{2,}')
b7 = re.compile(r'7{2,}')
b8 = re.compile(r'8{2,}')
b9 = re.compile(r'9{2,}')
y = [b0, b1 ,b2, b3, b4, b5, b6, b7, b8, b9]
for i in y:
    k = i.findall(b)
    result = result + k
maxlength = max(len(s) for s in result)
longest_strings = [s for s in result if len(s) == maxlength]
print(longest_strings)#одинаковые по длине последовательности
print(max(longest_strings))#самое большое число из всех одинаковых последовательностей
a = int(input('Если вы хотите удалить созданный файл нажмите 1'))
if a == 1:
	os.remove('num.txt')
else: print('File not deleted')
