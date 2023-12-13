class Carte: #je créé la classe CARTE avec ses différents attributs
    def __init__(self,cost,name,description):
        self.__cost=cost
        self.__name=name
        self.__description=description
    
    def getCost(self):
        return self.__cost
    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__description
    
class Crystal(Carte): #je créé la carte CRISTAL qui hérite de CARTE
    def __init__(self,name,cost,description,value):
        super().__init__(name,cost,description)
        self.__value=value

    def getValue(self):
        return self.__value
    
    def augmenterMana(self,manaMaxJoueur): #je créé sa méthode qui permet d'augmenter la MANA MAX du joueur
        manaMaxJoueur = manaMaxJoueur + self.__value
        print("Vous augmentez votre mana maximum de",self.__value,"! Vous avez désormais",manaMaxJoueur,"points de mana.")
    
class Creature(Carte): #je créé la carte CREATURE qui hérite de CARTE
    def __init__(self,name,cost,description,hp,atk):
        super().__init__(name,cost,description)
        self.__hp=hp
        self.__atk=atk

    def getHp(self):
        return self.__hp
    def getAtk(self):
        return self.__atk
    
    def attaquer(self,cible):
        cible.getHp() == cible.getHp() - self.__atk
        print(cible.getHp()) #ne fonctionne pas, les PV ne baissent pas
    
class Blast(Carte): #je créé la carte BLAST qui hérite de la classe CARTE
    def __init__(self,name,cost,description,value):
        super().__init__(name,cost,description)
        self.__value=value

    def getValue(self):
        return self.__value
    
    def attaquer(self,cible): #je créé sa méthode qui permet de faire des DEGATS à une CIBLE
        cible.gethp() == cible.gethp() - self.__value
        print("Vous attaquez la cible ! Il lui reste",cible.gethp(),"points de vie.") #ne fonctionne pas, les PV ne baissent pas

class Mage: #je créé la classe MAGE qui représente le joueur avec tout les attributs qui lui correspondent
    def __init__(self,name,hp,mana,hand):
        self.__name=name
        self.__hp=hp
        self.__mana_max=10
        self.__mana=mana
        self.__hand=hand
        self.__discarded =[]
        self.__board =[]

    def getName(self):
        return self.__name
    def getHp(self):
        return self.__hp
    def getManaMax(self):
        return self.__mana_max
    def getMana(self):
        return self.__mana
    def getHand(self):
        return self.__hand
    def getDiscarded(self):
        return self.__discarded
    def getBoard(self):
        return self.__board
    
    def jouerCarte(self,cardCost,cardPlayed,playerHand,playerboard): #je créé une méthode qui permet de JOUER une CARTE et de changer la MAIN du JOUEUR
        if(self.__mana < cardCost):
            print("Vous n'avez pas assez de mana pour jouer cette carte.")
        else:
            self.__mana -= cardCost
            playerBoard.append[cardPlayed] #pas terminé


    def rechargeMana(self): #je créé une méthode qui permet au JOUEUR de remonter sa MANA MAX au MAXIMUM
        self.__mana=self.__mana_max
        print("Vous rechargez votre mana ! Vous avez à nouveau",self.__mana_max,"points de mana.")

#je créé un DICTIONNAIRE regroupant les différentes CARTES de mon jeu
cartes = {1:Crystal("Cristal des Sentinelles",3,"Augmente votre mana maximum de 5. Un cristal ancien déterré dans les mines du désert de Girn.",5),
          2:Blast("Arcane de feu",3,"Inflige 3 dégats à la cible souhaitée. Manifeste des flammes destructrices.",3),
          3:Creature("Disciple de Talfanar",5,"15PV 6ATK : Un disciple de Talfanar venant des contrées d'Edénia",15,6)}

#je créé mes PERSONNAGES
personnage1 = Mage("JOUEUR 1",100,5,[{1:cartes[1],2:cartes[2],3:cartes[2],4:cartes[3],5:cartes[3]}])
personnage2 = Mage("JOUEUR 2",100,10,[{1:cartes[1],2:cartes[2],3:cartes[2],4:cartes[3],5:cartes[3]}])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ TESTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# cartes[1].augmenterMana(personnage1.getManaMax)


#ATTAQUE BLAST
# cartes[2].attaquer(personnage2.getHp())
# print(personnage2.getHp())

#ATTAQUE CREATURE
# cartes[3].attaquer(personnage2)

#FONCTIONNEL
# print(personnage1.getMana())
# personnage1.rechargeMana()
