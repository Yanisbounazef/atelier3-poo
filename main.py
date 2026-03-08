class Voiture:
    def __init__(self,matricule,marque,couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInformations(self):
        print("Matricule :", self.matricule)
        print("Marque :", self.marque)
        print("Couleur :", self.couleur)

class Parc:
    def __init__(self, id,adresse,capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = []

    def entrerVoiture(self, voiture):
        if voiture in self.listeVoitures:
            print("La voiture existe deja dans le parc")
        elif len(self.listeVoitures) >= self.capacite:
            print("Le parc est plein")
        else:
            self.listeVoitures.append(voiture)
            print("Voiture ajoutee au parc")

    def sortirVoiture(self, voiture):
        if voiture in self.listeVoitures:
            self.listeVoitures.remove(voiture)
            print("Voiture retiree du parc")
        else:
            print("La voiture n'est pas dans le parc")

    def calculerNbrPlacesLibres(self):
        return self.capacite - len(self.listeVoitures)
parc1 = Parc(1, "Toronto", 3)







