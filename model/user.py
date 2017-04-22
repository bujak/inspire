class User:

    user_list = []

    def __init__(self, mail, beacon_list = None):
        self.mail = mail
        if beacon_list:
            self.beacon_list = beacon_list
        else:
            self.beacon_list = []

    def add_beacon(self, beacon):
        self.beacon_list.append(beacon)

    def is_beacon_in_list(self, beacon):
        if beacon in self.beacon_list:
            beacon.add_pick()
        else:
            self.add_beacon(beacon)

    @classmethod
    def get_user_from_list(cls, email):
        pass
