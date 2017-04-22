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

    @staticmethod
    def get_picks_by_email(email):
        query = """SELECT picks.id, picks.email, picks.amount, beacons.product FROM picks
                  JOIN beacons on picks.uid = beacons.uid WHERE email = ? ORDER BY picks.amount DESC """
        value = [email]
        return sql.query(query, value)

    @staticmethod
    def get_clients():
        query = """SELECT day, COUNT(DISTINCT email) FROM picks GROUP BY day;"""
        clients = sql.query(query)
        print(clients[0][0])
        return clients







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
