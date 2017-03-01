import random
while True:
	try:
		from PIL import Image
		name = input("Введите имя файла : ")
		im = Image.open(name+".jpg")

		pixels = im.load()

		x,y = im.size

		spisok = ("""Выберите оттенок \n
		Оттенок серого	""")

		spisok1 = input("Введите что-то")

		if spisok1 == "spisok":
			print(spisok)

		print("""Выберите оттенок: \n
		Оттенок серого - grown \n
		Негатив - negative \n
		Сепия - sepia\n	
		Проиизвольны - prois\n
		Рандомный - random""")


		filtr = input("Введите команду ыыыы))")
		if filtr == "grown":
			for i in range(x):
				for j in range(y):
					r = pixels[i, j][0]
					g = pixels[i, j][1]
					b = pixels[i, j][2]
					S = (r + g + b) // 3
					S = r,g,b

		elif filtr == "negative" :
		    for i in range(x):
		        for j in range(y):
		            r = pixels[i, j][0]
		            g = pixels[i, j][1]
		            b = pixels[i, j][2]
		            pixels[i,j] = (255 - r, 255 - g , 255- b)

		elif filtr == "sepia":
			dep = int(input("Введите число"))
			for i in range(x):
				for j in range(y):
					r, g, b = pixels[i, j]
					mid = (r + g + b) //3
					pixels[i ,j] = mid , mid , mid 
					r, g, b = mid + dep *2,mid +dep,mid
					pixels[i, j] = r ,g ,b

		elif filtr == "prois":
			a = int(input("Введите r"))
			b = int(input("Введите g"))
			c = int(input("Введите b"))
			for i in range(x):
				for j in range(y):
					r,g,b = pixels[i,j]
					pixels[i,j] = a,b,c
		elif filtr == "random":
			a = random.randint(1,1000)
			b = random.randint(1,1000)
			c = random.randint(1,1000)
			for i in range(x):
				for j in range(y):
					r,g,b = pixels[i,j]
					pixels[i,j] = a,b,c
		else :
			print("Такого фильтра нет...")



		im.show()
		im.save("l18.jpg")

	except FileNotFoundError:
		print("Возможно такого файла не существует... Введите настоящее имя")
	except ValueError:
		print("Введите число !!! За это вам наказание в качестве того,что вы должны заново всё ввести:D")
