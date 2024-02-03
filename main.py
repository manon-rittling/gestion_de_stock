import tkinter
from tkinter import messagebox
from tkinter import filedialog
from Store import Store


class Main:
    def __init__(self):
        self.store = Store()
        self.fenetre = tkinter.Tk() 
        self.fenetre.geometry("1000x600")
        self.fenetre.title("Gestion de stock")
        self.bg = tkinter.PhotoImage(file="images/bgMag.png")

        # mettre fond ecran
        self.bg = tkinter.Label(self.fenetre, image=self.bg)
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

        # bouton ajouter produit
        self.ajouter_produit = tkinter.Button(self.fenetre, text="Ajouter produit", command=self.ajouterProduit)
        self.ajouter_produit.place(x=50, y=50)

        # bouton modifier produit
        self.modifier_produit = tkinter.Button(self.fenetre, text="Modifier produit", command=self.modifierProduit)
        self.modifier_produit.place(x=200, y=50)

        # bouton supprimer produit
        self.supprimer_produit = tkinter.Button(self.fenetre, text="Supprimer produit", command=self.supprimerProduit)
        self.supprimer_produit.place(x=350, y=50)

        # listes des produits
        self.liste_produits = tkinter.Listbox(self.fenetre, width=150, height=30)
        self.liste_produits.place(x=50, y=100)

    def afficherProduit(self):
        # lire produit du store
        allProducts = self.store.readProduit()
        for allProduct in allProducts:
            self.liste_produits.insert(tkinter.END, allProduct)

    def ajouterProduit(self):
        self.fenetre.destroy()
        import Ajouter_Produit


    def modifierProduit(self):
        self.fenetre.destroy()
        import Modifier_Produit

    def supprimerProduit(self):
        self.fenetre.destroy()
        import Supprimer_Produit
        
    def run(self):
        self.afficherProduit()
        self.fenetre.mainloop()


if __name__ == "__main__":
    main = Main()
    main.run()


