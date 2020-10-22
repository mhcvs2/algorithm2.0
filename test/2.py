"""
题目描述：某物流派送员p，需要给a、b、c、d4个快递点派送包裹，请问派送员需要选择什么的路线，才能完成最短路程的派送。
假设如图派送员的起点坐标(0,0)，派送路线只能沿着图中的方格边行驶，每个小格都是正方形，且边长为1，如p到d的距离就是4。
随机输入n个派送点坐标，求输出最短派送路线值（从起点开始完成n个点派送并回到起始点的距离）。
"""

import sys
import copy


class Points(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visit = False


start = Points(0, 0)
points = [Points(1, 4), Points(5, 3), Points(2, 2), Points(3, 1)]

min_length = sys.maxsize
min_processor = []


def get_length(p, q):
    return abs(p.x - q.x) + abs(p.y - q.y)


def dfs(p, cur_length, count, processor):
    global min_length
    global min_processor
    if count == len(points):
        if cur_length < min_length:
            min_length = cur_length
            min_processor = copy.deepcopy(processor)
        return
    for point in points:
        if point.visit:
            continue
        point.visit = True
        processor.append(point)
        dfs(point, cur_length+get_length(p, point), count+1, processor)
        processor.remove(point)
        point.visit = False


if __name__ == '__main__':
    dfs(start, 0, 0, [])
    print(min_length)
    print("(%d, %d)" % (start.x, start.y), end=" -> ")
    for point in min_processor:
        print("(%d, %d)" % (point.x, point.y), end=" -> ")
    print()

# 14
# (0, 0) -> (1, 4) -> (2, 2) -> (3, 1) -> (5, 3) ->