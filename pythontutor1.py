# from math import  *
# h = 9
# m = 0
# k = 0
# a = int(input())
# if a % 2 == 0:
#     k = int((a / 2 - 1)) * 15 + ((a / 2) * 5) + (45 * a)
# elif a%2 !=0:
#     k = ceil((a/2-1))*15 + (a/2)*5 + 45 *a
#     print(a/2-1)
#
#
# h += int(k//60)
# m += int(k%60)
#
# print(h," ",m)
#
# a = int(input())
# b = int(input())
# n = int(input())
#
# a1 = a*n
# b1 = b*n
# b1 = b1/100
# a1 += int(b1//100)
# print(a1," ", b1)

# h = int(input())
# a = int(input())
# b = int(input())
# k = 0
# while a<=h:
#     k+=1
#     a += a-b
# print(k)
#
# A = int(input())
# B = int(input())
# a = []
# for i in range(B,A+1):
#     if i%2!=0:
#         a.append(i)
# a.reverse()
# for i in range(0, len(a)):
#     print(a[i])
#
# a = int(inpur())
# arr = []
# for i in range(0,a):
#     arr.append(i*i*i)
# print(sum(arr))

k = 0
c = int(input())
for i in range(0,c):
    a = int(input())
    if a == 0:
        k+=1
print(k)