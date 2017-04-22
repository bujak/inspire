import model.sql as sql

class Beacon():
    def __init__(self, id, pick):
        self.id = id
        self.pick = pick

    @staticmethod
    def add_pick(beacon_id, user_id):
        query = """SELECT * FROM picks WHERE beacon_id = (?)"""
        param = [beacon_id]

        if not sql.query(query, param):
            query = """INSERT INTO picks (user_id, beacon_id, amount) VALUES (?, ?, ?)"""
            values = [user_id, beacon_id, 1]
            sql.query(query,values)
        else:
            query = """UPDATE picks SET amount = amount + 1 WHERE beacon_id =(?)"""
            sql.query(query, param)
        return

    @staticmethod
    def get_by_id(beacon_id):
        query = """SELECT """
        return
