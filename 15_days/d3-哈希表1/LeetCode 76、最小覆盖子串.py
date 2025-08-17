'''

一、题目描述
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：
- 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
- 如果 s 中存在这样的子串，我们保证它是唯一的答案。
示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：
输入：s = "a", t = "a"
输出："a"
示例 3:
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。

'''
import collections


class Solution:
    # 辅助函数，用于检查ht中的各个字符是否出现在hs中，且hs中的个数大于等于ht
    def check(self, ht, hs):
        return all(hs[k] >= ht[k] for k in ht.keys())

    def minWindow(self, s: str, t: str) -> str:
        # start, end 是最终所选择的字串区间的初始和终止位置，初始化均为-1
        start, end = -1, -1
        # min_len 是覆盖字串的最小长度，初始化为len(s)+1
        min_len = len(s)+1
        # 哈希表ht储存t中的字符以及个数，ht是不会发生变化的
        ht = collections.Counter(t)
        # 哈希表hs储存滑动窗口中的字符以及个数，初始化为空，hs是会发生变化的
        hs = collections.Counter()
        # 初始化左指针left
        left = 0
        # 遍历右指针right，进行滑窗过程，思考滑窗三问三答
        for right, ch in enumerate(s):
            # Q1：对于每一个右指针right所指的元素ch，做什么操作？
            # A1：将其加入哈希表hs的计数中
            hs[ch] += 1
            # Q2：什么时候要令左指针left右移？在什么条件下left停止右移？【循环不变量】
            # A2：self.check(hs, ht)为True，left可以右移以缩小窗口长度
            while self.check(ht, hs):
                # Q3：什么时候进行ans的更新？
                # A3：self.check(hs, ht)为True，此时滑窗是一个覆盖子串
                # 如果答案变量的长度大于滑窗长度，则更新答案变量ans为当前滑窗s[left:right+1]
                if min_len > right-left+1:
                    min_len = right-left+1
                    start, end = left, right+1
                    print(start, end)
                hs[s[left]] -= 1
                left += 1

        # 返回原s中的切片
        return s[start:end]