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
v1 = Voiture("ty111", "mazda", "Rouge")
v2 = Voiture("wy333", "toyota", "Blanche")
v3 = Voiture("dy222", "honda", "verte")
parc1.entrerVoiture(v1)
parc1.entrerVoiture(v2)
parc1.entrerVoiture(v3)
parc1.sortirVoiture(v2)
print("Places libres :", parc1.calculerNbrPlacesLibres())







