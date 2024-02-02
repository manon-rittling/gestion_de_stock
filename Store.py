from Produits import Produits
from Categories import Categories

class Store:
    def __init__(self):
        self.produit = Produits()
        self.categories = Categories()

    def createProduit(self, nom, description, prix, quantite, id_categories):
        self.produit.create(nom, description, prix, quantite, id_categories)

    def readProduit(self):
        produits = self.produit.read()
        listeProduits = []


        for produit_tuple in produits:
            print(produit_tuple)
            produit_dict = {
                "id": produit_tuple[0],
                "nom": produit_tuple[1],
                "description": produit_tuple[2],
                "prix": produit_tuple[3],
                "quantite": produit_tuple[4],
                "id_categorie": produit_tuple[5]
            }

            listeProduits.append(produit_dict)

        return listeProduits

    def updateProduit(self, id, nom, description, prix, quantite, id_categories):
        self.produit.update(id, nom, description, prix, quantite, id_categories)

    def deleteProduit(self, id):
        self.produit.delete(id)

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
    
    
        