import model.sql as sql
from datetime import date


class Beacon():
    def __init__(self, id, pick):
        self.id = id
        self.pick = pick

    @staticmethod
    def add_pick(beacon_id, email):
        today = date.today()
        query = """SELECT * FROM picks WHERE uid = ? AND email = ? AND day = ?"""
        param = [beacon_id, email, today]

        if not sql.query(query, param):
            query = """INSERT INTO picks (email, uid, amount, day) VALUES (?, ?, ?, ?)"""
            values = [email, beacon_id, 1, today]
            sql.query(query, values)
        else:
            query = """UPDATE picks SET amount = amount + 1 WHERE uid =(?) AND day = ?"""
            param = [beacon_id, today]
            sql.query(query, param)
        return

    @staticmethod
    def get_product_details(product_name):
        query = """SELECT product_details.details FROM product_details where product = ?;"""


        value = [product_name]

        details = sql.query(query, value)
        return details[0][0]

    @staticmethod
    def get_beacon_by_uid(beacon_uid):
        query = """SELECT product_details.details FROM product_details JOIN beacons on product_details.product = beacons.product where beacons.uid = ?; """
        value = [beacon_uid]
        return sql.query(query, value)[0][0]


    @staticmethod
    def get_product_amount():
        query = """SELECT beacons.product, SUM(picks.amount)
                    FROM picks 
                    JOIN beacons ON beacons.uid = picks.uid
                    GROUP BY picks.uid;"""
        products = sql.query(query)
        return products

    @staticmethod
    def get_product_amount():
        query = """SELECT beacons.product, COUNT(DISTINCT picks.email)
                    FROM picks 
                    JOIN beacons ON beacons.uid = picks.uid
                    GROUP BY picks.uid;"""
        products = sql.query(query)
        return products

    @staticmethod
    def get_products():
        query = """SELECT beacons.product, COUNT(DISTINCT picks.email), SUM(picks.amount)
                  FROM picks 
                  JOIN beacons ON beacons.uid = picks.uid
                  GROUP BY picks.uid;"""
        products = sql.query(query)
        return products

    @staticmethod
    def get_sum():
        query = """SELECT SUM(amount) from picks;"""
        suma = sql.query(query)
        return suma\

    @staticmethod
    def get_sum_a():
        query = """SELECT COUNT(DISTINCT email) from picks"""
        suma = sql.query(query)
        return suma


