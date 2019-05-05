class Noeud:
    def __init__(self, v):
        self.gauche = None
        self.droit = None
        self.valeur = v
        self.parent = None

class Arbre:
    def __init__(self):
        self.racine = None
        self.resultat_recherche = None

    def ajouter(self, val):
        if self.racine == None:
            self.racine = Noeud(val)
        else:
            self._ajouter(val, self.racine)

    def _ajouter(self, val, node):
        if val < node.valeur:
            if node.gauche is not None:
                self._ajouter(val, node.gauche)
            else:
                node.gauche = Noeud(val)
                node.gauche.parent = node
        else:
            if node.droit is not None:
                self._ajouter(val, node.droit)
            else:
                node.droit = Noeud(val)
                node.droit.parent = node

    def rechercher(self, val):
        self.resultat_recherche = None
        if self.racine == None:
            print("Impossible de rechercher la valeur demandée car l'arbre est vide.")
        elif self.racine.valeur == val:
            self.resultat_recherche = self.racine
        else:
            self._rechercher(val, self.racine)
        return self.resultat_recherche

    def _rechercher(self, val, node):
        if val < node.valeur:
            if node.gauche is not None:
                if node.gauche.valeur == val:
                    self.resultat_recherche = node.gauche
                else:
                    self._rechercher(val, node.gauche)
        else:
            if node.droit is not None:
                if node.droit.valeur == val:
                    self.resultat_recherche = node.droit
                else:
                    self._rechercher(val, node.droit)

    def parcourir(self):
        print("Parcours de l'arbre:")
        if self.racine is not None:
            self._parcourir(self.racine)

    def _parcourir(self, node):
        if node is not None:
            self._parcourir(node.gauche)
            print(node.valeur)
            self._parcourir(node.droit)

    def supprimer(self, val):
        node = self.rechercher(val)

        if node is None:
            print("Valeur impossible à supprimer car n'existant pas dans l'arbre.")

        else:

            # Cas où noeud est une feuille (suppression simple)
            if node.gauche is None and node.droit is None:
                if node.parent.gauche.valeur == node.valeur:
                    node.parent.gauche = None
                else:
                    node.parent.droit = None

            # Cas où noeud a un seul enfant (remplacement par lui)
            elif node.gauche is None and node.droit is not None:
                if node.parent.gauche.valeur == node.valeur:
                    node.parent.gauche = node.droit
                else:
                    node.parent.droit = node.droit

            # Cas où noeud a un seul enfant (remplacement par lui)
            elif node.gauche is not None and node.droit is None:
                if node.parent.gauche.valeur == node.valeur:
                    node.parent.gauche = node.gauche
                else:
                    node.parent.droit = node.gauche

            # Cas où noeud a deux enfants (remplacement par le node le plus proche)
            elif node.gauche is not None and node.droit is not None:
                a = node.gauche
                b = node.droit

                while a.droit is not None:
                    a = a.droit

                while b.gauche is not None:
                    b = b.gauche

                if node.valeur - a.valeur >= b.valeur - node.valeur:
                    if node.parent.gauche.valeur == node.valeur:
                        node.parent.gauche = b
                    else:
                        node.parent.droit = b

                else:
                    if node.parent.gauche.valeur == node.valeur:
                        node.parent.gauche = a
                    else:
                        node.parent.droit = a



arbre = Arbre()
arbre.ajouter(1)
arbre.ajouter(2)
arbre.ajouter(4)
arbre.ajouter(100)
arbre.ajouter(88)
arbre.ajouter(24)
arbre.ajouter(12)
arbre.ajouter(26)

arbre.parcourir()

arbre.supprimer(88)

arbre.parcourir()