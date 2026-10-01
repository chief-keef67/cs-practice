num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
sign = input("Введите операцию (+, -, *): ")
if sign == '+':
	print(f'{num1}+{num2}={num1+num2}')
elif sign == '-':
	print(f'{num1}-{num2}={num1-num2}')
