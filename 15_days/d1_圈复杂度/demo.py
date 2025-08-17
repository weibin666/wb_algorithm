import inspect
from radon.complexity import cc_visit


def example(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        for i in range(10):
            if i % 2 == 0:
                print(i)


# 获取函数的源代码
function_code = inspect.getsource(example)

# 解析圈复杂度
complexity = cc_visit(function_code)

# 输出结果
for item in complexity:
    print(f"Name: {item.name}, Complexity: {item.complexity}")

'''
Name: example, Complexity: 5
'''