'''
题目描述
在神秘的大陆「阿斯卡隆」，有一条由 n 颗魔法水晶组成的水晶链。每颗水晶都拥有一个整数的魔力值，依次排列在一起，形成一个整数数组 a[1], a[2], ..., a[n]。
为了测量魔力的稳定性，大魔法师会取出所有长度恰好为 d 的连续水晶段进行分析。
对于每一段连续的 d 颗水晶，我们定义它的波动幅度为：max_value - min_value。
其中 max_value 是该段水晶的最大魔力值，min_value 是该段水晶的最小魔力值。
你的任务是：
找出所有这些长度为 d 的连续水晶段的波动幅度中，最大的那个值，并输出它。
输入格式
第一行包含一个整数 n (1 <= n <= 10^3)，表示水晶链的长度。
- 第二行包含 n 个整数 a[1], a[2], ..., a[n] (-10^9 <= a[i] <= 10^9)，表示每颗水晶的魔力值。
- 第三行包含一个整数 d (1 <= d <= n)，表示要分析的连续水晶段的长度。
输出格式
- 输出一个整数，表示所有长度为 d 的连续水晶段的波动幅度中的最大值。
样例
样例1
样例输入：
5
1 3 2 5 4
3

样例输出：
3

样例说明：
对于 a = [1, 3, 2, 5, 4] 且 d = 3，所有长度为 3 的连续水晶段及其波动幅度为：
- [1, 3, 2] → max_value = 3, min_value = 1 → 波动幅度 = 3 - 1 = 2
- [3, 2, 5] → max_value = 5, min_value = 2 → 波动幅度 = 5 - 2 = 3
- [2, 5, 4] → max_value = 5, min_value = 2 → 波动幅度 = 5 - 2 = 3
最大波动幅度为 3，因此输出 3。
题目解析

理解题目
题目要求在一个长度为 n 的整数数组中，考察所有长度为 d 的连续子数组。每个子数组的波动幅度定义为该子数组中的最大值减去最小值。最终答案是所有子数组波动幅度中的最大值。
换句话说，若数组为 a[1..n]，窗口长度为 d，则答案是：
max_{i ∈ [1..n-d+1]} ( max(a[i..i+d-1]) - min(a[i..i+d-1]) )
其中 a[i..i+d-1] 表示从第 i 个元素开始的长度为 d 的连续区间。
使用算法
这道题的解法是朴素枚举法。
- 遍历所有可能的窗口起点，从 i = 1 到 i = n - d + 1。
- 在每个窗口中，逐一检查其中的 d 个元素，求出最大值与最小值。
- 计算两者的差值，作为该窗口的波动幅度。
- 在全局范围内维护一个最大值，最后输出该值作为结果。
实现
输入读取
- 第 1 行读入整数 n。
- 第 2 行读入数组 a[1..n]。
- 第 3 行读入整数 d。
窗口枚举
- 初始化答案变量 ans = -∞。
- 对于每个起点 i（范围从 0 到 n-d，假设从下标 0 开始存储数组）：
  - 初始化 window_max = -∞ 和 window_min = +∞。
  - 遍历子数组 a[i..i+d-1]，逐个更新 window_max 和 window_min。
  - 得到该窗口的波动幅度 window_diff = window_max - window_min。
答案维护
- 更新全局最大波动幅度：ans = max(ans, window_diff)
输出结果
- 循环结束后，输出 ans。


'''

class Solution:
    def max_fluctuation(self, a, d):
        """
        计算长度为 d 的所有连续子数组的波动幅度（max - min），并返回最大值
        朴素做法：O(n * d)
        """
        n = len(a)
        max_diff = float('-inf')

        # 枚举所有长度为 d 的连续子数组
        for i in range(n - d + 1):
            current_segment = a[i: i +d]
            diff = max(current_segment) - min(current_segment)
            max_diff = max(max_diff, diff)

        return max_diff


if __name__ == "__main__":
    # 读取输入
    n = int(input().strip())                       # 第一行：n
    a = list(map(int, input().strip().split()))    # 第二行：数组 a
    d = int(input().strip())                       # 第三行：d

    # 创建 Solution 实例并计算结果
    sol = Solution()
    result = sol.max_fluctuation(a, d)

    # 输出结果
    print(result)
