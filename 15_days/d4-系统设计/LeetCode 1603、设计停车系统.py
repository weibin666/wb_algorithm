'''
题目描述
请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。
请你实现 ParkingSystem 类：
- ParkingSystem(int big, int medium, int small) 初始化 ParkingSystem 类，三个参数分别对应每种停车位的数目。
- bool addCar(int carType) 检查是否有 carType 对应的停车位。 carType 有三种类型：大，中，小，分别用数字 1， 2 和 3 表示。一辆车只能停在 carType 对应尺寸的停车位中。如果没有空车位，请返回 false ，否则将该车停入车位并返回 true 。
示例 1：
输入：
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
输出：
[null, true, true, false, false]

解释：
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // 返回 true ，因为有 1 个空的大车位
parkingSystem.addCar(2); // 返回 true ，因为有 1 个空的中车位
parkingSystem.addCar(3); // 返回 false ，因为没有空的小车位
parkingSystem.addCar(1); // 返回 false ，因为没有空的大车位，唯一一个大车位已经被占据了

提示：
- 0 <= big, medium, small <= 1000
- carType 取值为 1， 2 或 3
- 最多会调用 addCar 函数 1000 次
解题思路
1、用三个变量分别维护各类车型的剩余空位的数目，每次 addCar(carType) 的时候就把对应类型的停车空位数目 -1。
2、如果当前车型的剩余空位数目 == 0，那么说明无法再停车了，就返回 False；否则说明可以停车，就返回 True。
3、carType 的取值为 1,2,3 ，因此可以使用数组保存停车位的剩余空位数目，根据下标来获取对应车型的停车位剩余数目。

'''


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        # 数组的第 0 位置初始化为 0，起到占位符的作用
        # 这样在 addCar 方法里面
        # park[1] 就是 big 的数量
        # park[2] 就是 medium 的数量
        # park[3] 就是 small 的数量
        self.park = [0, big, medium, small]

    def addCar(self, carType):
        # 当前类型没有车位了，返回 False
        if self.park[carType] == 0:
            return False

        # 否则当前类型车位数量减少一个
        self.park[carType] -= 1
        return True
