class UserPoint:

    def __init__(self, u_id, u_longitude, u_latitude):
        self.u_id = u_id
        self.u_longitude = u_longitude
        self.u_latitude = u_latitude
        self.fake_location_list = []
        self.send_longitude = None
        self.send_latitude = None
        self.in_voronoiCell = None
