from Data import Data

class Categories:
    def __init__(self):
        self.table = "categories"
        self.db = Data(host="localhost", user="root", password="manon", database="store")

    def create(self, nom):
        requete = f"INSERT INTO {self.table} (nom) VALUES (%s)"
        params = (nom,)
        self.db.executeRequete(requete, params)

    def joinId(self):
        requete = f"SELECT {self.table}.id, {self.table}.nom AS categorie_nom, produits.* FROM {self.table} INNER JOIN produits ON {self.table}.id = produits.id_categorie WHERE {self.table}.id = produits.id_categorie"
        
        return(self.db.fetch(requete))


    def read(self):
        requete = f"SELECT * FROM {self.table}"
        return (self.db.fetch(requete))

    def update(self, id, nom):
        requete = f"UPDATE {self.table} SET nom = %s WHERE id = %s"
        params = (nom, id)
        self.db.executeRequete(requete, params)

    def delete(self, id):
        requete = f"DELETE FROM {self.table} WHERE id=%s"
        params = (id,)
        self.db.executeRequete(requete, params)

if __name__ == "__main__":
        
    categorie1 = Categories()
    # categorie1.create("boucherie")
    
    
    

    