from itertools import combinations

def min_walking_distance(stations, k):
    n = len(stations)
    min_total = float('inf')
    
    # 生成所有可能的关闭站组合（选择 k 个站关闭）
    #  Todo
    for closed in combinations(range(n), k):
        open_stations = [i for i in range(n) if i not in closed]
        total = 0
        
        for closed_station in closed:
            left = -1  # 左边最近的开放站
            right = n  # 右边最近的开放站
            
            # 找到左边最近的开放站
            for o in open_stations:
                if o < closed_station:
                    if o > left:
                        left = o
                elif o > closed_station:
                    if o < right:
                        right = o
                    break  # 因为 open_stations 是排序的，可以提前退出
            
            # 计算走路距离
            if left == -1:
                distance = right - closed_station
            elif right == n:
                distance = closed_station - left
            else:
                distance = min(closed_station - left, right - closed_station)
            
            total += stations[closed_station] * distance
        
        if total < min_total:
            min_total = total
    
    return min_total

# 测试
stations = [10, 9, 11, 5, 2]
k = 2
print(min_walking_distance(stations, k))  # 输出应为 9