import tkinter
from tkinter import messagebox
from Store import Store


class Main:
    def __init__(self):
        self.store = Store()
        self.fenetre = tkinter.Tk()
        self.fenetre.geometry("1000x600")
        self.fenetre.title("Gestion de stock")
        self.bg = tkinter.PhotoImage(file="images/bgMag.png")

        # mettre fond ecran
        self.bg_label = tkinter.Label(self.fenetre, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # bouton ajouter produit
        self.ajouter_produit = tkinter.Button(self.fenetre, text="Ajouter produit", command=self.ajouterProduit)
        self.ajouter_produit.place(x=250, y=50)

        # bouton modifier produit
        self.modifier_produit = tkinter.Button(self.fenetre, text="Modifier produit", command=self.modifierProduit)
        self.modifier_produit.place(x=400, y=50)

        # bouton supprimer produit
        self.supprimer_produit = tkinter.Button(self.fenetre, text="Supprimer produit", command=self.supprimerProduit)
        self.supprimer_produit.place(x=550, y=50)

        # listes des produits
        self.liste_produits = tkinter.Listbox(self.fenetre, width=110, height=30)
        self.liste_produits.place(x=150, y=100)


    def afficherProduit(self):
        # lire produit du store
        allProducts = self.store.readProduit() 
        espace_avant_id = " " 
        # afficher produit dans la liste
        for allProduct in allProducts:
            self.liste_produits.insert("end",espace_avant_id, allProduct)
            if allProduct['id_categorie'] == 1:
                self.liste_produits.itemconfig("end", {'bg': 'red'})
            elif allProduct['id_categorie'] == 2:
                self.liste_produits.itemconfig("end", {'bg': 'blue'})
            elif allProduct['id_categorie'] == 3:
                self.liste_produits.itemconfig("end", {'bg': 'green'})
            
            

    def ajouterProduit(self):
        

        # Créer une nouvelle fenêtre pour ajouter le produit
        self.fenetre_ajout = tkinter.Toplevel()
        self.fenetre_ajout.geometry("300x400")
        self.fenetre_ajout.title("Ajouter produit")

        # Label nom
        self.label_nom = tkinter.Label(self.fenetre_ajout, text="Nom")
        self.label_nom.place(x=50, y=50)
        self.nom = tkinter.Entry(self.fenetre_ajout)
        self.nom.place(x=150, y=50)

        # Label description
        self.label_description = tkinter.Label(self.fenetre_ajout, text="Description")
        self.label_description.place(x=50, y=100)
        self.description = tkinter.Entry(self.fenetre_ajout)
        self.description.place(x=150, y=100)

        # Label prix
        self.label_prix = tkinter.Label(self.fenetre_ajout, text="Prix")
        self.label_prix.place(x=50, y=150)
        self.prix = tkinter.Entry(self.fenetre_ajout)
        self.prix.place(x=150, y=150)

        # Label quantité
        self.label_quantite = tkinter.Label(self.fenetre_ajout, text="Quantité")
        self.label_quantite.place(x=50, y=200)
        self.quantite = tkinter.Entry(self.fenetre_ajout)
        self.quantite.place(x=150, y=200)

        # Label id_categorie
        self.label_id_categorie = tkinter.Label(self.fenetre_ajout, text="Id catégorie")
        self.label_id_categorie.place(x=50, y=250)
        self.id_categorie = tkinter.Entry(self.fenetre_ajout)
        self.id_categorie.place(x=150, y=250)

        # Bouton confirmer ajout
        self.bouton_confirmer_ajout = tkinter.Button(self.fenetre_ajout, text="Confirmer Ajout", command=self.confirmerAjout)
        self.bouton_confirmer_ajout.place(x=150, y=300)
        self.fenetre_ajout.mainloop()

    def confirmerAjout(self):
        try:
            prix = int(self.prix.get())
            quantite = int(self.quantite.get())
        except ValueError:
            messagebox.showerror("Erreur", "Le prix doit être un nombre et la quantité doit être un entier.")
            return

        # Appel à la méthode createProduit de l'objet store pour ajouter le produit à la base de données
        self.store.createProduit(
            self.nom.get(),
            self.description.get(),
            prix,
            quantite,
            self.id_categorie.get()
        )

        # Mise à jour de la liste des produits après l'ajout
        self.liste_produits.delete(0, "end")
        self.afficherProduit()

        # Fermeture de la fenêtre d'ajout
        self.fenetre_ajout.destroy()

    def modifierProduit(self):
        
        self.fenetre= tkinter.Toplevel()
        self.fenetre.geometry("300x400")
        self.fenetre.title("Modifier produit")

        # label id pour recuperer le produit a modifier
        self.label_id = tkinter.Label(self.fenetre, text="Id")
        self.label_id.place(x=50, y=10)
        self.id = tkinter.Entry(self.fenetre)
        self.id.place(x=150, y=10)

        # Label nom
        self.label_nom = tkinter.Label(self.fenetre, text="Nom")
        self.label_nom.place(x=50, y=50)
        self.nom = tkinter.Entry(self.fenetre)
        self.nom.place(x=150, y=50)

        # Label description
        self.label_description = tkinter.Label(self.fenetre, text="Description")
        self.label_description.place(x=50, y=100)
        self.description = tkinter.Entry(self.fenetre)
        self.description.place(x=150, y=100)

        # Label prix
        self.label_prix = tkinter.Label(self.fenetre, text="Prix")
        self.label_prix.place(x=50, y=150)
        self.prix = tkinter.Entry(self.fenetre)
        self.prix.place(x=150, y=150)

        # Label quantité
        self.label_quantite = tkinter.Label(self.fenetre, text="Quantité")
        self.label_quantite.place(x=50, y=200)
        self.quantite = tkinter.Entry(self.fenetre)
        self.quantite.place(x=150, y=200)

        # Label id_categorie
        self.label_id_categorie = tkinter.Label(self.fenetre, text="Id catégorie")
        self.label_id_categorie.place(x=50, y=250)
        self.id_categorie = tkinter.Entry(self.fenetre)
        self.id_categorie.place(x=150, y=250)
        
        # Bouton confirmer modification
        self.bouton_confirmer_modification = tkinter.Button(self.fenetre, text="Confirmer Modification", command=self.confirmerModification)
        self.bouton_confirmer_modification.place(x=150, y=300)
        
        # mise a jour de afficher produit
        self.afficherProduit()


    def confirmerModification(self):
        try:
            prix = int(self.prix.get())
            quantite = int(self.quantite.get())
        except ValueError:
            messagebox.showerror("Erreur", "Le prix doit être un nombre et la quantité doit être un entier.")
            return

        # Appel à la méthode updateProduit de l'objet store pour modifier le produit dans la base de données
        self.store.updateProduit(
            self.id.get(),
            self.nom.get(),
            self.description.get(),
            prix,
            quantite,
            self.id_categorie.get()
        )

        # Mise à jour de la liste des produits après la modification
        self.liste_produits.delete(0, "end")
        self.afficherProduit()

        # Fermeture de la fenêtre de modification
        self.fenetre.destroy()

        # mise a jour de afficher produit
        self.afficherProduit()

    def supprimerProduit(self):
        self.fenetre= tkinter.Toplevel()
        self.fenetre.geometry("300x400")
        self.fenetre.title("Supprimer produit")

        # label id pour recuperer le produit a supprimer
        self.label_id = tkinter.Label(self.fenetre, text="Id")
        self.label_id.place(x=50, y=10)
        self.id = tkinter.Entry(self.fenetre)
        self.id.place(x=150, y=10)

        # Bouton confirmer suppression
        self.bouton_confirmer_suppression = tkinter.Button(self.fenetre, text="Confirmer Suppression", command=self.confirmerSuppression)
        self.bouton_confirmer_suppression.place(x=150, y=100)
        self.fenetre.mainloop()

    def confirmerSuppression(self):
        # Appel à la méthode deleteProduit de l'objet store pour supprimer le produit de la base de données
        self.store.deleteProduit(self.id.get())

        # Mise à jour de la liste des produits après la suppression
        self.liste_produits.delete(0, "end")
        self.afficherProduit()

        # Fermeture de la fenêtre de suppression
        self.fenetre.destroy()

    
        

    def run(self):
        self.afficherProduit()
        self.fenetre.mainloop()


if __name__ == "__main__":
    main = Main()
    main.run()
