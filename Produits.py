from Data import Data

class Produits:
    def __init__(self):
        self.table = "produits"
        self.db = Data(host="localhost", user="root", password="manon", database="store")

    def create(self, nom, description, prix, quantite, id_categorie):
        requete = f"INSERT INTO {self.table} (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
        params = (nom, description, prix, quantite, id_categorie)
        self.db.executeRequete(requete, params)

    def read(self):
        requete = f"SELECT * FROM {self.table}"
        return self.db.fetch(requete)
    
    def update(self, id, nom, description, prix, quantite, id_categorie):
        requete = f"UPDATE {self.table} SET nom=%s, description=%s, prix=%s, quantite=%s, id_categorie=%s WHERE id=%s"
        params = (nom, description, prix, quantite, id_categorie, id)
        self.db.executeRequete(requete, params)

    def delete(self, id):
        requete = f"DELETE FROM {self.table} WHERE id=%s"
        params = (id,)
        self.db.executeRequete(requete, params)


if __name__ == "__main__":
        
    produit1 = Produits()
    # produit1.create("roquefort", "200g provenance de roquefort bio", 12, 15, 3)
    # produit1.update(10, "roquefort", "200g provenance de roquefort bio", 15, 12, 3)
    produit1.read()

    