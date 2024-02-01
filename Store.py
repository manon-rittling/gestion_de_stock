from Produits import Produits
from Categories import Categories

class Store:
    def __init__(self):
        self.produits = Produits()
        self.categories = Categories()

    def createProduit(self, nom, description, prix, quantite, id_categories):
        self.produits.create(nom, description, prix, quantite, id_categories)

    def readProduit(self):
        return self.produits.read()
    
    def updateProduit(self, id, nom, description, prix, quantite, id_categories):
        self.produits.update(id, nom, description, prix, quantite, id_categories)

    def deleteProduit(self, id):
        self.produits.delete(id)

    def createCategorie(self, nom):
        self.categories.create(nom)

    def readCategorie(self):
        return self.categories.read()
    
    def updateCategorie(self, id, nom):
        self.categories.update(id, nom)

    def deleteCategorie(self, id):
        self.categories.delete(id)

    def joinId(self):
        return self.categories.joinId()
    
    
        