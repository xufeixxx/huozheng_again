class Settings:

    def __init__(self):
        self.map_width = [-166.524881, 145.003318]  # 经度
        self.map_length = [30.000060, 59.999807]  # 纬度
        # self.map_width = [1, 500]  # 经度
        # self.map_length = [1, 500]
        self.road_point_num = 100000
        # self.user_dataset_filename = 'D:\\研究生\\数据集\\gowalla\\new_gowalla.csv'
        self.user_dataset_filename = 'D:\\研究生\\数据集\\gowalla\\gowalla.csv'
        self.limit_user_number = 1000000  # 避免通过数据集过大是程序运行缓慢，来限制用户数量，例如，10即表示只读取数据集前十行的用户数据
        # limit_user_number = 0时将没有限制,会读取数据集中的全部数据
        self.num_of_fake_location = 5
        # self.Privacy_parameters = 0.25  # theta
        # self.Real_location_probability = math.exp(self.Privacy_parameters) / (
        #             self.num_of_fake_location + math.exp(self.Privacy_parameters))
        # self.Fake_location_probability = 1 / (self.num_of_fake_location + math.exp(self.Privacy_parameters))
        # self.space_range_size = 0.05


"""
根据实验记录，点数为20的时候，不是全部封闭维诺个的比例大约是0.4还是比较高的
200 ---> 0.07
2000 ----> 0.011
20000 ----> 0.008
由此可见当使用上百万的数据点（道路交叉口）时，数据小的可以忽略不计了，所以本模型只记录封闭性维诺格
只计算用户位置信息在封闭维诺格中的数据,不在封闭维诺格中的位置信息不去计算.vor.regions某一项有-1的话说明不封闭
"""
