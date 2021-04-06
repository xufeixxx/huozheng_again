import math
from scipy.spatial import Voronoi, voronoi_plot_2d
from overall.settings import Settings
from overall.list import point_list, voronoiCell_list, vertex_list, userPoint_list
from entity.point import Point
from entity.vertex import Vertex
from entity.voronoiCell import VoronoiCell
from entity.uPoint import UserPoint
import csv
import numpy as np
import matplotlib.pyplot as plt
import random

setts = Settings()


class Function:

    def __init__(self, vor):
        self.vor = vor

    def make_vertices(self):
        vertices = self.vor.vertices  # 尽量使用局部变量
        vertex_list.extend(
            list(map(lambda vertex, i: Vertex(i, vertex[0], vertex[1]), vertices, range(1, len(vertices) + 1))))
        # 用map代替for函数
        # i = 1
        # for vertex in self.vor.vertices:
        #     vertex_list.append(Vertex(i, vertex[0], vertex[1]))
        #     i += 1

    # def make_ridges(self):
    #     for ridge in self.vor.ridge_vertices:
    #         if ridge[0] != -1 and ridge[1] != -1:
    #             ridge_list.append(Ridge(ridge[0] + 1, ridge[1] + 1))

    def make_voronoiCells(self):
        k = 1
        v_regions = self.vor.regions
        vc_list_append = voronoiCell_list.append
        for region in v_regions:
            if len(region) != 0 and exist_negative_one(region) is False:
                voronoiCell = VoronoiCell(k)
                vrl_append = voronoiCell.ridge_list.append
                vX_append = voronoiCell.polyX.append
                vY_append = voronoiCell.polyY.append
                num = 0
                for i in range(len(region)):
                    vrl_append([region[i] + 1, region[(i + 1) % len(region)] + 1])
                    vertex = from_vId_find_vertex(region[i] + 1)
                    vX_append(vertex.v_x)
                    vY_append(vertex.v_y)
                    if i == 0:
                        voronoiCell.maxX = vertex.v_x
                        voronoiCell.maxY = vertex.v_y
                        voronoiCell.minX = vertex.v_x
                        voronoiCell.minY = vertex.v_y
                    else:
                        if voronoiCell.maxX < vertex.v_x:
                            voronoiCell.maxX = vertex.v_x
                        if voronoiCell.maxY < vertex.v_y:
                            voronoiCell.maxY = vertex.v_y
                        if voronoiCell.minX > vertex.v_x:
                            voronoiCell.minX = vertex.v_x
                        if voronoiCell.minY > vertex.v_y:
                            voronoiCell.minY = vertex.v_y
                    num += 1
                voronoiCell.polySides = num
                k += 1
                vc_list_append(voronoiCell)

    def show(self):
        voronoi_plot_2d(self.vor)
        plt.show()


def make_points():
    number = setts.road_point_num
    w0 = setts.map_width[0]
    w1 = setts.map_width[1]
    l0 = setts.map_length[0]
    l1 = setts.map_length[1]
    road_point = np.random.uniform([w0, l0], [w1, l1], (number, 2))
    road1 = road_point.T
    point_list.extend(list(map(lambda id, x, y: Point(id + 1, x, y), range(number), road1[0], road1[1])))
    # for i in range(setts.road_point_num):
    #     x = random.uniform(setts.map_width[0], setts.map_width[1])
    #     y = random.uniform(setts.map_length[0], setts.map_length[1])
    #     # x = random.uniform(0, 100)
    #     # y = random.uniform(0, 100)
    #     point = Point(i + 1, x, y)
    #     point_list.append(point)


def make_voronoi():
    xy_list = np.empty((0, 2))
    for point in point_list:
        xy_list = np.append(xy_list, [[point.p_x, point.p_y]], axis=0)
    return Voronoi(xy_list)


def exist_negative_one(list):
    if -1 in list:
        return True
    return False


def from_vId_find_vertex(v_id):
    a = list(filter(lambda v: v.v_id == v_id, vertex_list))
    return a[0]
    # for v in vertex_list:
    #     if v.v_id == v_id:
    #         return v


def point_in_notIn_polygon(x, y, voronoiCell):  # 此算法从网上获得https://blog.csdn.net/hjh2005/article/details/9246967
    # ，经实验当点位于v图的边的时候一定程度上，位于左侧边上判定为在v图之内，右侧边判定之外
    j = voronoiCell.polySides - 1
    oddNodes = False
    vpY = voronoiCell.polyY
    vpX = voronoiCell.polyX
    for i in range(j + 1):
        if vpY[i] < y <= vpY[j] or vpY[i] >= y > vpY[j]:
            if vpX[i] + (y - vpY[i]) / (vpY[j] - vpY[i]) * (
                    vpX[j] - vpX[i]) <= x:
                oddNodes = not oddNodes

        j = i

    return oddNodes


def point_in_which_VCell(x, y):
    a = list(filter(lambda vc: point_in_notIn_polygon(x, y, vc), voronoiCell_list))
    if len(a) == 0:
        return 0
    else:
        return a[0]
    # for voronoiCell in voronoiCell_list:
    #     if point_in_notIn_polygon(x, y, voronoiCell):
    #         return voronoiCell
    # return 0


# 返回0代表不在任何一个维诺格中，此点在实验中应该被舍弃，形参x， y是用户的位置数据


def make_randNum_in_vCell(voronoiCell):
    ru = random.uniform
    v_minX = voronoiCell.minX
    v_maxX = voronoiCell.maxX
    v_minY = voronoiCell.minY
    v_maxY = voronoiCell.maxY
    x = ru(v_minX, v_maxX)
    y = ru(v_minY, v_maxY)
    while not point_in_notIn_polygon(x, y, voronoiCell):
        x = ru(v_minX, v_maxX)
        y = ru(v_minY, v_maxY)

    return [x, y]


def make_userPoints():
    # 用户点随机分布
    number = setts.limit_user_number
    w0 = setts.map_width[0]
    w1 = setts.map_width[1]
    l0 = setts.map_length[0]
    l1 = setts.map_length[1]
    user_point = np.random.uniform([w0, l0], [w1, l1], (number, 2))
    user1 = user_point.T
    userPoint_list.extend(list(map(lambda id, x, y: UserPoint(id + 1, x, y), range(number), user1[0], user1[1])))

    # with open(setts.user_dataset_filename) as f:
    #     reader = csv.reader(f)
    #     userPoint_list.extend(list(map(lambda row:UserPoint(int(row[0]), float(row[2]), float(row[1])), reader)))
    # next(reader)
    # i = 0
    # upa = userPoint_list.append
    # for row in reader:
    #     upa(UserPoint(int(row[0]), float(row[2]), float(row[1])))
    #     i += 1
    #     if i == setts.limit_user_number:
    #         break

    # for i in range(10):
    #     userPoint_list.append(UserPoint(i+1, random.uniform(0, 100), random.uniform(0, 100)))


def disturbance_location_data():
    nfl = setts.num_of_fake_location
    for user in userPoint_list:
        voronoiCell = point_in_which_VCell(user.u_longitude, user.u_latitude)
        if voronoiCell == 0:
            user.in_voronoiCell = False
        else:
            user.in_voronoiCell = True
            user.fake_location_list.extend(list(map(lambda i: make_randNum_in_vCell(voronoiCell), range(nfl))))
            # for i in range(setts.num_of_fake_location):
            #     user.fake_location_list.append(make_randNum_in_vCell(voronoiCell))


def get_send_data(theta):
    Real_location_probability = math.exp(theta) / (
            setts.num_of_fake_location + math.exp(theta))
    ru = random.uniform
    nfl = setts.num_of_fake_location
    for user in userPoint_list:
        if user.in_voronoiCell:
            random_num = ru(0, 1)
            if random_num <= Real_location_probability:
                user.send_longitude = user.u_longitude
                user.send_latitude = user.u_latitude
            else:
                n = nfl
                ran_num = ru(0, 1)
                uf_ll = user.fake_location_list
                for i in range(n):
                    if i / n < ran_num <= (i + 1) / n:
                        user.send_longitude = uf_ll[i][0]
                        user.send_latitude = uf_ll[i][1]
