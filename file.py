from memory_profiler import memory_usage
a = int(input("Введите число"))
arr_goda = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94,
            102, 103, 104, 112, 113, 114, 122, 123, 124, 132, 133, 134, 142, 143, 144]
arr_let = [5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45,
           46, 47, 48, 49, 50, 55, 56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88,
           89, 90, 95, 96, 97, 98, 99, 100, 105, 106, 107,
           108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 125, 126, 127, 128, 129, 130, 135, 136, 137,
           138, 139, 140, 145, 146, 147, 148, 149, 150]
arr_god = [1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131, 141]

for i in range(0, len(arr_goda)):
    if arr_goda[i] == a:
        print("Вам ", a, " года")
for i in range(0, len(arr_let)):
    if arr_let[i] == a:
        print("Вам ", a, " лет")
for i in range(0, len(arr_god)):
    if arr_god[i] == a:
        print("Вам ", a, " год")
print(memory_usage())
