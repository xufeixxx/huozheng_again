class VoronoiCell:
    def __init__(self, vc_id):
        self.vc_id = vc_id
        self.ridge_list = []
        self.polySides = 0
        self.polyX = []
        self.polyY = []
        self.maxX = 0
        self.maxY = 0
        self.minX = 0
        self.minY = 0

