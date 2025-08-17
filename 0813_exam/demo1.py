'''

题目描述
在魔法大陆的「卷轴之塔」中，存放着成千上万的魔法卷轴。大法师常用 show 命令在水晶终端上查看某个法阵仓库下的所有卷轴名称。
然而，卷轴的排列顺序十分讲究：当学徒 先纵向浏览、再横向浏览时，卷轴的名称必须按照词典顺序递增排列。
为了方便学徒阅读，卷轴的展示需要遵循以下规则：
1. 每行的总字符数不得超过 viewWidth。
2. 每列左对齐，并且相邻两列之间必须至少空 2 个空格。
3. 卷轴名称先纵向摆放，再横向排列（即先填满第一列的所有行，再依次填充后续列）。
4. 所有卷轴名称在纵向→横向阅读时，必须是词典序递增的。
你的任务是：
给定卷轴展示的最大行宽 viewWidth 以及卷轴名称列表 scrollNames，计算出展示所有卷轴所需的最少行数。
输入格式
- 第一行输入一个整数 viewWidth，满足 30 <= viewWidth <= 200。
- 第二行输入一个整数 n，表示卷轴数量，满足 1 < n <= 1000。
- 接下来 n 行，每行一个字符串，表示一个卷轴名称 scrollNames[i]，满足：
  - 1 <= len(scrollNames[i]) <= viewWidth
  - 只包含字符数字和字母
输出格式
输出一个整数，表示展示所有卷轴所需的最少行数。
样例
样例1
样例输入：
44
4
FlameOrb20
Crystal9
CrystalC4
EmberStone12
样例输出：
2
样例说明：
将卷轴名称按词典序排序后为：
Crystal9、CrystalC4、EmberStone12、FlameOrb20
展示效果如下（纵向优先）：
Crystal9   EmberStone12
CrystalC4  FlameOrb20
从上到下、再从左到右查看时，顺序为：
Crystal9 → CrystalC4 → EmberStone12 → FlameOrb20，符合要求。
样例2
样例输入：
45
10
Altar1
Arcanum3
BeastDen4
BlightWood5
Dragonspire8
EldritchTome2
Moonwell9
ObsidianGate6
PhoenixRoost7
Starfall0
样例输出：
4

'''




class Solution:
    def minRows(self, viewWidth: int, scrollNames: list) -> int:
        # 先按词典序对卷轴名称排序
        scrollNames.sort()
        n = len(scrollNames)  # 卷轴总数
        sz = [len(s) for s in scrollNames]  # 预先计算每个卷轴名称的长度，避免重复计算

        # 定义检查函数：判断在给定行数 rows 下，是否能在 viewWidth 宽度限制内完成排版
        def can_fit(rows: int) -> bool:
            # 计算需要的列数，(n + rows - 1) // rows 是向上取整
            cols = (n + rows - 1) // rows

            s = 0  # 用来记录所有列的总宽度（不含列间距）
            # 按列分组，每列包含 rows 个（最后一列可能不足）
            for i in range(0, n, rows):
                # 找出当前列中最长的卷轴名的长度
                s += max(sz[i:i+rows])
            # 总宽度 = 列宽总和 + 列间距 (cols - 1) * 2
            return s + (cols - 1) * 2 <= viewWidth
        # 从 1 行开始枚举，直到 n 行（最多每行一个卷轴）
        for rows in range(1, n + 1):
            # 一旦找到第一个满足宽度要求的行数，立即返回
            if can_fit(rows):
                return rows
        # 理论上不会执行到这里，但为了保险，返回 n（即每行一个）
        return n

if __name__ == "__main__":
    # 从标准输入读取数据
    viewWidth = int(input().strip())  # 最大行宽
    n = int(input().strip())  # 卷轴数量
    scrollNames = [input().strip() for _ in range(n)]  # 卷轴名称列表

    sol = Solution()  # 创建 Solution 类实例
    ans = sol.minRows(viewWidth, scrollNames)  # 调用方法计算最小行数
    print(ans)  # 输出结果
