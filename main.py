import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Store import Store
import csv

class Main:
    def __init__(self):
        self.store = Store()
        self.fenetre = tk.Tk()
        self.fenetre.geometry("1000x600")
        self.fenetre.title("Gestion de stock")
        self.bg = tk.PhotoImage(file="images/bgMag.png")

        # Mettre fond ecran
        self.bg_label = tk.Label(self.fenetre, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Bouton ajouter produit
        self.ajouter_produit = tk.Button(self.fenetre, text="Ajouter produit", command=self.ajouterProduit)
        self.ajouter_produit.place(x=250, y=150)

        # Bouton modifier produit
        self.modifier_produit = tk.Button(self.fenetre, text="Modifier produit", command=self.modifierProduit)
        self.modifier_produit.place(x=400, y=150)

        # Bouton supprimer produit
        self.supprimer_produit = tk.Button(self.fenetre, text="Supprimer produit", command=self.supprimerProduit)
        self.supprimer_produit.place(x=550, y=150)

        # Bouton exporter en CSV
        self.export_csv = tk.Button(self.fenetre, text="Exporter en CSV", command=self.export_csv)
        self.export_csv.place(x=700, y=150)

        # Tableau des produits
        self.treeview = ttk.Treeview(self.fenetre, columns=("id","Nom", "Description", "Prix", "Quantité", "Id Catégorie"), show="headings")
        self.treeview.heading("id", text="Id")
        self.treeview.heading("Nom", text="Nom")
        self.treeview.heading("Description", text="Description")
        self.treeview.heading("Prix", text="Prix")
        self.treeview.heading("Quantité", text="Quantité")
        self.treeview.heading("Id Catégorie", text="Id Catégorie")
        self.treeview.place(x=150, y=250)

        # Définir la largeur des colonnes
        self.treeview.column("id", width=50)
        self.treeview.column("Nom", width=150)
        self.treeview.column("Description", width=200)
        self.treeview.column("Prix", width=100)
        self.treeview.column("Quantité", width=100)
        self.treeview.column("Id Catégorie", width=100)

        self.afficherProduit()

    def afficherProduit(self):
        # Effacer les anciennes données
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Lire les produits du store
        allProducts = self.store.readProduit()

        # Afficher chaque produit dans le Treeview
        for product in allProducts:
            self.treeview.insert("", "end", values=(product["id"],product["nom"], product["description"], product["prix"], product["quantite"], product["id_categorie"]))

    def ajouterProduit(self):
        # Créer une nouvelle fenêtre pour ajouter le produit
        self.fenetre_ajout = tk.Toplevel()
        self.fenetre_ajout.geometry("300x400")
        self.fenetre_ajout.title("Ajouter produit")

        # Label nom
        self.label_nom = tk.Label(self.fenetre_ajout, text="Nom")
        self.label_nom.place(x=50, y=50)
        self.nom = tk.Entry(self.fenetre_ajout)
        self.nom.place(x=150, y=50)

        # Label description
        self.label_description = tk.Label(self.fenetre_ajout, text="Description")
        self.label_description.place(x=50, y=100)
        self.description = tk.Entry(self.fenetre_ajout)
        self.description.place(x=150, y=100)

        # Label prix
        self.label_prix = tk.Label(self.fenetre_ajout, text="Prix")
        self.label_prix.place(x=50, y=150)
        self.prix = tk.Entry(self.fenetre_ajout)
        self.prix.place(x=150, y=150)

        # Label quantité
        self.label_quantite = tk.Label(self.fenetre_ajout, text="Quantité")
        self.label_quantite.place(x=50, y=200)
        self.quantite = tk.Entry(self.fenetre_ajout)
        self.quantite.place(x=150, y=200)

        # Label id_categorie
        self.label_id_categorie = tk.Label(self.fenetre_ajout, text="Id catégorie")
        self.label_id_categorie.place(x=50, y=250)
        self.id_categorie = tk.Entry(self.fenetre_ajout)
        self.id_categorie.place(x=150, y=250)

        # Bouton confirmer ajout
        self.bouton_confirmer_ajout = tk.Button(self.fenetre_ajout, text="Confirmer Ajout", command=self.confirmerAjout)
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
        self.afficherProduit()

        # Fermeture de la fenêtre d'ajout
        self.fenetre_ajout.destroy()

    def modifierProduit(self):
        # Créer une nouvelle fenêtre pour modifier le produit
        self.fenetre_modif = tk.Toplevel()
        self.fenetre_modif.geometry("300x400")
        self.fenetre_modif.title("Modifier produit")

        # Label id pour récupérer le produit à modifier
        self.label_id = tk.Label(self.fenetre_modif, text="Id")
        self.label_id.place(x=50, y=10)
        self.id_modif = tk.Entry(self.fenetre_modif)
        self.id_modif.place(x=150, y=10)

        # Label nom
        self.label_nom = tk.Label(self.fenetre_modif, text="Nom")
        self.label_nom.place(x=50, y=50)
        self.nom_modif = tk.Entry(self.fenetre_modif)
        self.nom_modif.place(x=150, y=50)

        # Label description
        self.label_description = tk.Label(self.fenetre_modif, text="Description")
        self.label_description.place(x=50, y=100)
        self.description_modif = tk.Entry(self.fenetre_modif)
        self.description_modif.place(x=150, y=100)

        # Label prix
        self.label_prix = tk.Label(self.fenetre_modif, text="Prix")
        self.label_prix.place(x=50, y=150)
        self.prix_modif = tk.Entry(self.fenetre_modif)
        self.prix_modif.place(x=150, y=150)

        # Label quantité
        self.label_quantite = tk.Label(self.fenetre_modif, text="Quantité")
        self.label_quantite.place(x=50, y=200)
        self.quantite_modif = tk.Entry(self.fenetre_modif)
        self.quantite_modif.place(x=150, y=200)

        # Label id_categorie
        self.label_id_categorie = tk.Label(self.fenetre_modif, text="Id catégorie")
        self.label_id_categorie.place(x=50, y=250)
        self.id_categorie_modif = tk.Entry(self.fenetre_modif)
        self.id_categorie_modif.place(x=150, y=250)

        # Bouton confirmer modification
        self.bouton_confirmer_modification = tk.Button(self.fenetre_modif, text="Confirmer Modification", command=self.confirmerModification)
        self.bouton_confirmer_modification.place(x=150, y=300)

        self.fenetre_modif.mainloop()

    def confirmerModification(self):
        try:
            prix = int(self.prix_modif.get())
            quantite = int(self.quantite_modif.get())
        except ValueError:
            messagebox.showerror("Erreur", "Le prix doit être un nombre et la quantité doit être un entier.")
            return

        # Appel à la méthode updateProduit de l'objet store pour modifier le produit dans la base de données
        self.store.updateProduit(
            self.id_modif.get(),
            self.nom_modif.get(),
            self.description_modif.get(),
            prix,
            quantite,
            self.id_categorie_modif.get()
        )

        # Mise à jour de la liste des produits après la modification
        self.afficherProduit()

        # Fermeture de la fenêtre de modification
        self.fenetre_modif.destroy()

    def supprimerProduit(self):
        # Créer une nouvelle fenêtre pour supprimer le produit
        self.fenetre_suppr = tk.Toplevel()
        self.fenetre_suppr.geometry("300x400")
        self.fenetre_suppr.title("Supprimer produit")

        # Label id pour récupérer le produit à supprimer
        self.label_id_suppr = tk.Label(self.fenetre_suppr, text="Id")
        self.label_id_suppr.place(x=50, y=10)
        self.id_suppr = tk.Entry(self.fenetre_suppr)
        self.id_suppr.place(x=150, y=10)

        # Bouton confirmer suppression
        self.bouton_confirmer_suppression = tk.Button(self.fenetre_suppr, text="Confirmer Suppression", command=self.confirmerSuppression)
        self.bouton_confirmer_suppression.place(x=150, y=100)

        self.fenetre_suppr.mainloop()

    def confirmerSuppression(self):
        # Appel à la méthode deleteProduit de l'objet store pour supprimer le produit de la base de données
        self.store.deleteProduit(self.id_suppr.get())

        # Mise à jour de la liste des produits après la suppression
        self.afficherProduit()

        # Fermeture de la fenêtre de suppression
        self.fenetre_suppr.destroy()

    def export_csv(self):

        # relier bouton export à la méthode
        self.export_csv = tk.Button(self.fenetre, text="Exporter en CSV", command=self.export_csv)
        self.export_csv.place(x=700, y=50)



        # Ouvrir un fichier en mode écriture
        with open("produits.csv", "w", newline="") as csvfile:
            # Créer une variable pour ecrire dans CSV
            writer = csv.writer(csvfile)

            # Écrire les en-têtes de colonnes
            writer.writerow(["id","Nom", "Description", "Prix", "Quantité", "Id Catégorie"])

            # Parcourir les éléments du Treeview et écrire les données
            for item in self.treeview.get_children():
                row = [self.treeview.item(item, "values")[i] for i in range(len(self.treeview["columns"]))]
                writer.writerow(row)

    def run(self):
        self.fenetre.mainloop()

if __name__ == "__main__":
    main = Main()
    main.run()
