'''
题目描述
在魔法大陆的西东走向的“星辰之路”上，分布着若干个冒险者聚集点，每个聚集点都有一定数量的冒险者，人数记录在数组 mages 中。为了方便冒险者快速传送到远方，魔法议会计划在部分聚集点上设置传送阵。
然而，由于稀有魔力水晶的数量有限，议会必须关闭 banNum 个聚集点的传送阵。这些被关闭的聚集点的冒险者必须前往最近的、仍然开放的传送阵，通过步行完成转移。
请你帮助魔法议会规划传送阵的分布，使得所有冒险者步行经过的区间总数最少，并输出这个最小的总数。
输入格式
- 第一行输入一个整数 n，表示聚集点的数量，满足 1 <= n <= 100。
- 第二行输入 n 个整数，mages[i] 表示第 i 个聚集点的冒险者人数，满足 0 <= mages[i] <= 10^5。
- 第三行输入一个整数 banNum，表示需要关闭传送阵的聚集点数量，满足 0 <= banNum <= min(6, n - 1)。
输出格式
- 输出一个整数，表示最少的步行区间总数。
样例
样例1
样例输入：
5
12 7 15 4 3
2
样例输出：
10
样例说明：
关闭下标为 3 和 4 的传送阵：
- 下标 3 的冒险者：步行 1 个区间到下标 2，贡献 4×1 = 4；
- 下标 4 的冒险者：步行 2 个区间到下标 2，贡献 3×2 = 6；
- 总计 4 + 6 = 10
样例2
样例输入：
7
5 4 5 4 6 7 9
3
样例输出：
14
样例说明：
一种可行的最优方案：关闭下标为 0、2、3 的传送阵：
- 下标 0：步行 1 个区间，贡献 5×1 = 5；
- 下标 2：步行 1 个区间，贡献 5×1 = 5；
- 下标 3：步行 1 个区间，贡献 4×1 = 4；
- 合计 5 + 5 + 4 = 14。

'''


class Solution:
    def minWalk(self, mages: list, banNum: int):

        n = len(mages)  # 聚集点数量（含人数）

        # 预处理 cost[l][r] 表示删除区间 [l..r] 的总代价
        # cost[l][r] 表示把第 l..r 个聚集点全部取消时，这些人到最近保留点的步行区间总和
        cost = [[0 for _ in range(n)] for _ in range(n)]
        inf = float('inf')
        for l in range(n):  # 枚举左端点
            for r in range(l, n):  # 枚举右端点
                for k in range(l, r + 1):  # 遍历区间内的每个点
                    conf = inf  # conf 表示该点步行的最短距离
                    if l != 0:
                        # 如果左边不是边界，那么可以往左走到 l-1
                        conf = min(conf, k - l + 1)
                    if r != n - 1:
                        # 如果右边不是边界，那么可以往右走到 r+1
                        conf = min(conf, r + 1 - k)
                    # 加总该点人数 * 步行距离
                    cost[l][r] += conf * mages[k]

        # f[i][j] 表示：在前 j 个点中，恰好取消了 i 个点的最小代价
        f = [[inf for _ in range(n)] for _ in range(banNum + 1)]

        # 初始化：当没有取消站点时，所有 j 的代价为 0
        for j in range(n):
            f[0][j] = 0

        # 动态规划
        for i in range(1, banNum + 1):  # 枚举取消的数量
            for j in range(i - 1, n):  # 枚举当前处理到的位置 j
                # f[i][j] 继承自 f[i][j-1]（即不在 j 结尾形成新删除区间）
                f[i][j] = f[i][j - 1] if j > 0 else inf
                for k in range(1, i + 1):  # 枚举删除区间长度
                    l = j - k + 1  # 删除区间的左端点
                    if l < 0:  # 左端点越界，退出
                        break
                    else:
                        # 如果区间是 [l..j]，那么前面剩下 i-k 个删除要在 l-2 之前完成
                        # 注意 l-2 是因为 [l..j] 左边紧挨着的位置是 l-1，必须保留
                        prev = f[i - k][l - 2] if l - 2 >= 0 else (0 if i - k == 0 else inf)
                        # 更新最优值：前面的代价 + 删除 [l..j] 的代价
                        f[i][j] = min(f[i][j], prev + cost[l][j])

        # 返回最终结果：在 n-1 位置，恰好删掉 banNum 个点的最小代价
        return f[banNum][n - 1]


if __name__ == "__main__":
    # 输入格式：
    # 第一行：整数 n（聚集点数量）
    # 第二行：n 个整数，表示各聚集点人数
    # 第三行：整数 banNum，表示要删除的聚集点数
    n = int(input().strip())
    mages = list(map(int, input().split()))
    banNum = int(input().strip())

    sol = Solution()
    ans = sol.minWalk(mages, banNum)
    print(ans)


