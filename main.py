from func.function import make_voronoi, make_points
from func.function import Function, get_send_data, make_userPoints, disturbance_location_data
from func.region_query import space_range_size
from overall.list import *
import profile


def main():
    make_points()
    vor = make_voronoi()
    func = Function(vor)
    func.make_vertices()
    func.make_voronoiCells()
    make_userPoints()
    disturbance_location_data()
    size_list = [0.05, 0.1, 0.15, 0.2, 0.4]
    theta_list = [0.25, 0.5, 0.75, 1]
    for theta in theta_list:
        get_send_data(theta)
        for size in size_list:
            pro = space_range_size(size)
            print("theta = ", theta, "size = ", size, "相对误差 = ", pro, "\n")
    print("hello world")
    # get_send_data(0.4)
    # pro = space_range_size(1)
    # print("theta = 0.4","size = 0.9","相对误差 = ", pro, "\n")


if __name__ == "__main__":
    profile.run("main()")

# func.show()


