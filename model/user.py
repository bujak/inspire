import model.sql as sql


class User:

    @staticmethod
    def make_user(user):
        query = "SELECT id FROM users WHERE email=?"
        params = [user["email"]]
        user_id = sql.query(query, params)
        if not user_id:
            query2 = "INSERT INTO users (`email`) VALUES (?)"
            sql.query(query2, params)
            user_id = sql.query(query, params)
        return user_id[0][0]










    # def __init__(self, mail, beacon_list = None):
    #     self.mail = mail
    #     if beacon_list:
    #         self.beacon_list = beacon_list
    #     else:
    #         self.beacon_list = []
    #
    # def add_beacon(self, beacon):
    #     self.beacon_list.append(beacon)
    #
    # def is_beacon_in_list(self, beacon):
    #     if beacon in self.beacon_list:
    #         beacon.add_pick()
    #     else:
    #         self.add_beacon(beacon)
    #
    # @classmethod
    # def get_user_from_list(cls, email):
    #     pass
