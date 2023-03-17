f_num = int(input())
s_num = list(input())

c_mul = f_num * int(s_num[2])
b_mul = f_num * int(s_num[1])
a_mul = f_num * int(s_num[0])

print(c_mul)
print(b_mul)
print(a_mul)

print(c_mul + (b_mul * 10) + (a_mul * 100))