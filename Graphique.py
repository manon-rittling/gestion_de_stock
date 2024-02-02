import pygame
from pygame.locals import *
from Store import Store


pygame.init()

class Graphique:
    def __init__(self):
        self.store = Store()
        self.clock = pygame.time.Clock()

        # Crée la fenêtre
        self.fenetre = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Gestion de stock")

        # chargement des images, cadre de texte, police
        self.bg = pygame.image.load("images/bgMag.png").convert()
        self.cadre = pygame.image.load("images/cadre.png").convert_alpha()
        self.font = pygame.font.SysFont(None, 17)

        # crée bouton ajouter produit
        self.ajouter_produit = self.font.render("Ajouter", True, (0, 0, 0))
        self.ajouter_produit_rect = self.ajouter_produit.get_rect()
        self.ajouter_produit_rect.x = 200
        self.ajouter_produit_rect.y = 100

        # cree  bouton modifier produit
        self.modifier_produit = self.font.render("Modifier ", True, (0, 0, 0))
        self.modifier_produit_rect = self.modifier_produit.get_rect()
        self.modifier_produit_rect.x = 400
        self.modifier_produit_rect.y = 100

        # cree bouton supprimer produit
        self.supprimer_produit = self.font.render("Supprimer", True, (0, 0, 0))
        self.supprimer_produit_rect = self.supprimer_produit.get_rect()
        self.supprimer_produit_rect.x = 600
        self.supprimer_produit_rect.y = 100


        # position des produits
        self.positions = {
            "id": (160 , 150),
            "nom": (200, 150),
            "description": (320, 150),
            "prix": (600, 150),
            "quantite": (680, 150),
            "id_categorie": (780, 150)
        }

    
    def afficherProduit(self):
        

        # boucle pour afficher les produits
        
            self.fenetre.blit(self.bg, (0, 0))
            self.fenetre.blit(self.cadre, (150, 100))
            

            # lire produit du store
            allProducts = self.store.readProduit()

            y = 150
            for allProduct in allProducts:
                # x = 160
            
                # afficher les info de chaque colonne
                for colonne, position in self.positions.items():
                    info_texte = f"{colonne}: {allProduct[colonne]}"
                    texte = self.font.render(info_texte, True, (0, 0, 0))
                    self.fenetre.blit(texte, (position[0], y))

                y += 30

                
            
            pygame.display.update()
            
            
            # gestion des événements
            running = True
            while running:
                 
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                        pygame.quit()
                        exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                            pygame.quit()
                            exit()
                        if event.key == K_RETURN:
                            running = False
                            pygame.quit()
                            exit()
                self.clock.tick(60)

    def afficher_boutons (self):
        
        if self.ajouter_produit_rect.collidepoint(pygame.mouse.get_pos()):
            self.ajouter_produit = self.font.render("Ajouter", True, (255, 255, 255))
        else:
            self.ajouter_produit = self.font.render("Ajouter", True, (0, 0, 0))
        self.fenetre.blit(self.ajouter_produit, self.ajouter_produit_rect)
        if self.modifier_produit_rect.collidepoint(pygame.mouse.get_pos()):
            self.modifier_produit = self.font.render("Modifier", True, (255, 255, 255))
        else:
            self.modifier_produit = self.font.render("Modifier", True, (0, 0, 0))
        self.fenetre.blit(self.modifier_produit, self.modifier_produit_rect)
        if self.supprimer_produit_rect.collidepoint(pygame.mouse.get_pos()):
            self.supprimer_produit = self.font.render("Supprimer", True, (255, 255, 255))
        else:
            self.supprimer_produit = self.font.render("Supprimer", True, (0, 0, 0))
        self.fenetre.blit(self.supprimer_produit, self.supprimer_produit_rect)
        pygame.display.flip()


        
        

    

graphique = Graphique()
graphique.afficherProduit()
graphique.afficher_boutons()

            



        



        



    
    


        

                    
    

 


        

    



