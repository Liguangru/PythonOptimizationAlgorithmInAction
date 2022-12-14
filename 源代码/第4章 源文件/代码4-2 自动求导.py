from sympy import diff, symbols, exp, log
# 定义变量
x1, x2, t = symbols('x1 x2 t')
# 定义目标函数
func = t*(-70*x1-30*x2) - log(-3*x1-9*x2+540) - log(-5*x1 - 5*x2+450) - log(-9*x1-3*x2+720) - log(-x1) - log(-x2)
# 求导
diff(func, x1, 1)   # 对x1求一阶导
diff(func, x2, 1)   # 对x2求一阶导
diff(func, x1, x1)  # 对x1,x1求二阶导
diff(func, x1, x2)  # 对x1,x2求二阶导
diff(func, x2, x1)  # 对x2,x1求二阶导
diff(func, x2, x2)  # 对x2,x2求二阶导

# 输出
# 对x1求一阶导
# -70*t + 3/(-3*x1 - 9*x2 + 540) + 5/(-5*x1 - 5*x2 + 450) + 9/(-9*x1 - 3*x2 + 720) - 1/x1

# 对x2求一阶导
# -30*t + 9/(-3*x1 - 9*x2 + 540) + 5/(-5*x1 - 5*x2 + 450) + 3/(-9*x1 - 3*x2 + 720) - 1/x2

# 对x1,x1求二阶导
# 9/(3*x1 + x2 - 240)**2 + (x1 + 3*x2 - 180)**(-2) + (x1 + x2 - 90)**(-2) + x1**(-2)

# 对x1,x2求二阶导
# 3/(3*x1 + x2 - 240)**2 + 3/(x1 + 3*x2 - 180)**2 + (x1 + x2 - 90)**(-2)

# 对x2,x1求二阶导
# 3/(3*x1 + x2 - 240)**2 + 3/(x1 + 3*x2 - 180)**2 + (x1 + x2 - 90)**(-2)

# 对x2,x2求二阶导
# (3*x1 + x2 - 240)**(-2) + 9/(x1 + 3*x2 - 180)**2 + (x1 + x2 - 90)**(-2) + x2**(-2)

