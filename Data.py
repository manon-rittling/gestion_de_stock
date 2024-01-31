import _mysql_connector

class Data:
    def__init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connexion(self):
        self.db = _mysql_connector.connect(
            host=self.host, 
            user=self.user, 
            password=self.password, 
            database=self.database
        ) 
        self.cursor = self.db.cursor()

    def deconnexion(self):
        self.db.close()

    def execute(self, requete, params=None):
        self.connexion()
        self.cursor.execute(requete, params or ())
        self.db.commit()
        self.deconnexion()

    def fetch(self, requete, params=None):
        self.connexion()
        self.cursor.execute(requete, params or ())
        result = self.cursor.fetchall()
        self.deconnexion()
        return result