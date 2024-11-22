                #1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(b=25)
print_params(c=[1,2,3])
print()
                #2.Распаковка параметров:
values_list = ('случайный текст',356,False)
print_params(*values_list)
values_dict = {'a':'text','b':True,'c':248}
print_params(**values_dict)
print()
                #3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
