import string

# 高分云获取验证码
def veriy_c(dr):
    a = dr.split()[0]
    a = int(a)
    b = dr.split()[2]
    b = int(b)
    c = dr.split()[1]
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '×':
        return a * b
    else:
        return a / b
