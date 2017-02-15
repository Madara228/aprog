import math
while True
	try:
		while True:
			num1 = int(input("Введите первое число :"))
			op = input("Введите опреатора : ")
			num2 = int(input("Введите второе число :"))	
			if op == "+":
				print("								 Сложение чисел ",num1," и ",num2," = ",num1+num2)
			elif op == "-":
				print(" 							 Вычитание чисел ",num1, " и ",num2," = ",num1-num2)
			elif op == "/":
				print(" 							 Разность чисел ",num1, " и ",num2, " = ",num1/num2)
			elif op == " * ":
				print(" 							 Произведение чисел ",num1, " и ",num2, " = ",num1*num2)
			elif op == "//":
				print(" 							 Корень чисел ",num1," и ",num2, " = ", math.sqrt(num1)," и ",math.sqrt(num2))
			elif op == "sin":
				print("		Синус чисел ",num1," и ",num2, " = ", math.sin(num1), " и ",math.sin(num2))


	except ValueError:
		print("Введите число")