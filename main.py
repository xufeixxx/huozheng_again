from func.function import make_voronoi, make_points
from func.function import Function,get_send_data, make_userPoints, disturbance_location_data
from func.region_query import space_range_size
from overall.list import *


make_points()
vor = make_voronoi()
func = Function(vor)
func.make_vertices()
func.make_ridges()
func.make_voronoiCells()
make_userPoints()
disturbance_location_data()
size_list = [0.05, 0.1, 0.15, 0.2, 0.4]
theta_list = [0.25, 0.5, 0.75, 1]
for theta in theta_list:
    get_send_data(theta)
    for size in size_list:
        pro = space_range_size(size)
        print("theta = ",theta,"size = ",size,"相对误差 = ",pro,"\n")

#func.show()

print("helloworld")

"""
空维诺格的比例
i = 0
for reg in vor.regions:
    for k in reg:
        if k == -1:
            i += 1
print(i/(len(vor.regions)-1))
"""
