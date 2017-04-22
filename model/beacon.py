import model.sql as sql

class Beacon():
    def __init__(self, id, pick):
        self.id = id
        self.pick = pick

    @staticmethod
    def add_pick(beacon_id, email):
        query = """SELECT * FROM picks WHERE uid = ? AND email = ?"""
        param = [beacon_id, email]

        if not sql.query(query, param):
            query = """INSERT INTO picks (email, uid, amount) VALUES (?, ?, ?)"""
            values = [email, beacon_id, 1]
            sql.query(query, values)
        else:
            query = """UPDATE picks SET amount = amount + 1 WHERE uid =(?)"""
            param = [beacon_id]
            sql.query(query, param)
        return

    @staticmethod
    def get_by_id(beacon_id):
        query = """SELECT """
        return
