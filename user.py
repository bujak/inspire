class User:

    def __init__(self, name, beacon_list = None):
        self.name = name
        if beacon_list:
            self.beacon_list = beacon_list
        else:
            self.beacon_list = []

    def add_beacon(self, beacon):
        self.beacon_list.append(beacon)


