from func.function import make_voronoi, make_points
from func.function import Function, get_send_data, make_userPoints, disturbance_location_data
from func.region_query import space_range_size
import profile
import datetime


def main():
    start = datetime.datetime.now()
    print("开始时间是：", datetime.datetime.now())
    make_points()
    print("路交点生成完成的时间：", datetime.datetime.now())
    print()
    vor = make_voronoi()
    print("V图对象生成的时间", datetime.datetime.now())
    print()
    func = Function(vor)
    func.make_vertices()
    print("V图顶点生成完成的时间：", datetime.datetime.now())
    print()
    func.make_voronoiCells()
    print("V格完成的时间：", datetime.datetime.now())
    print()
    make_userPoints()
    print("用户点完成的时间：", datetime.datetime.now())
    print()
    disturbance_location_data()
    print("用户假位置完成的时间：", datetime.datetime.now())
    print()
    size_list = [0.05, 0.1, 0.15, 0.2, 0.4]
    theta_list = [0.25, 0.5, 0.75, 1]
    for theta in theta_list:
        get_send_data(theta)
        for size in size_list:
            pro = space_range_size(size)
            print("theta = ", theta, "size = ", size, "相对误差 = ", pro, "\n")
        print("theta = ", theta, "所有区域的误差计算完成的时间：", datetime.datetime.now())
    # get_send_data(0.25)
    # print("所有用户得到扰动位置的时间：", datetime.datetime.now())
    # print()
    # pro = space_range_size(0.05)
    # print("相对误差是：", pro)
    # print("得到相对误差的时间：", datetime.datetime.now())

    print("总完成用时：", datetime.datetime.now() - start)
    print("全部完成的时间：", datetime.datetime.now())


if __name__ == "__main__":
    profile.run("main()")

# func.show()
