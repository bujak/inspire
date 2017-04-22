class Beacon():
    def __init__(self, id, pick):
        self.id = id
        self.pick = pick


    def add_pick(self):
        self.pick += 1

    @staticmethod
    def get_by_id(beacon_id):
        #TODO get from DB
        return