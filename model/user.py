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
        a = sql.query(query, value)
        return sql.query(query, value)

    @staticmethod
    def get_clients():
        query = """SELECT day, SUM(amount), COUNT(DISTINCT email) FROM picks GROUP BY day;"""
        clients = sql.query(query)
        return clients

    @staticmethod
    def sigle_client():
        query = """SELECT email, SUM(amount), COUNT(DISTINCT day) FROM picks GROUP BY email;"""
        clients = sql.query(query)
        return clients
