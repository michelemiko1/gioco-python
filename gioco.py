
import sys


#CLASSE PERSONAGGIO
class Personaggio:
    def __init__(self,nome,arma):
        self.nome = nome
        self.arma = arma
        self.vita = 10

    def scheda(self):
        print( f"SCHEDA PERSONAGGIO:\n nome: {self.nome}"
               f"\n vita: {self.vita}"
               f"\n arma: {self.arma.nome}\n")

    def add_arma(self,arma):
        self.arma = arma

    def mod_vita(self,vita):
        self.vita = vita

#LUOGHI
class Luogo:
    def __init__(self,nome):
        self.nome = nome

    def scheda(self):
        print(f"SCHEDA LUOGO:\n nome: {self.nome}\n")

class Arma:
    def __init__(self,nome,forza,resistenza):
        self.nome = nome
        self.forza = forza
        self.resistenza = resistenza

    def scheda(self):
        print(f"SCHEDA ARMA:\n nome: {self.nome}"
              f"\n forza: {self.forza}"
              f"\n resistenza: {self.resistenza}\n")




def prima_prova():
    risposta = input("Vuoi iniziare questa avventura?[si/no] ")
    if risposta != "si":
        print("GAME OVER")
        sys.exit()
    else:
        print("Che l'avventura abbia inizio!")

def crea_personaggio():
    nome = input("Scegliti un nome da vero guerriero: ")
    protagonista = Personaggio(nome,None)
    print(f"Bene, caro {protagonista.nome} "
          f"la tua avventura sta per iniziare..")
    return protagonista

def primo_oggetto(protagonista):
    oggetto = input(f"guardati un po' attorno ci sono alcuni oggetti!\n"
          f"siccome devi proprio sbrigarti hai tempo di \nraccoglierne "
          f"solo uno, quale? [1/2/3] ")
    oggetto = int(oggetto)

    while (oggetto != 1 and oggetto !=2 and oggetto !=3):
        oggetto = int(input("inserimento non valido. Scegli 1,2 o 3: "))

    if oggetto == 1: ogg1 = Arma("Spada",12,8)
    if oggetto == 2: ogg1 = Arma("Bastone",7,6)
    if oggetto == 3: ogg1 = Arma("Coltello",9,9)
    protagonista.add_arma(ogg1)

    print(f"Dai un'occhiata all'oggetto raccolto\n")

    protagonista.arma.scheda()

def loop_gioco(protag):
    print(f"Dai un'occhiata al luogo in cui ti trovi.\n"
          f"Si tratta del salone di un vecchio edificio malmesso.\n"
          f"Intravedi dalla finestra un cortile. ")

    print(f"\ntenedo saldamente a te la tua arma ( {protag.arma.nome} ) "
          f"ti dirigi verso l'esterno..")

    luogo = input("\nHai 2 possibilità. Recarti nel cortile o entrare nella vecchia cucina.\n"
          "per il momento non sembrano esserci altri luoghi interessanti lì [cortile/cucina]: ")

    while (luogo != "cortile" and luogo != "cucina" ):
        luogo = input("inserimento non valido. Scrivi cortile o cucina: ")

    if luogo == "cortile":
        cortile(protag)
    if luogo == "cucina":
        print("dai facciam finta che hai scelto cortile")
        cortile(protag)

def cortile(protag):
    esci = 0

    while esci!=1:
        azione = input("\nTi trovi in nel cortile cosa vuoi fare? [esplora/riposa/corri]: ")

        while (azione != "esplora" and azione != "riposa" and azione != "corri" ):
            azione = input("inserimento non valido. Scrivi cortile o cucina: ")

        if azione == "corri": print("\nPerchè? Spiegami perchè ti metti a correre adesso..")
        if azione == "riposa":
            print("recuperi tutti i punti vita")
            protag.mod_vita(10)
            protag.scheda()
        if azione == "esplora": print("Ebbravo il mio esploratore")

        esci = 1










prima_prova()
protag = crea_personaggio()
primo_oggetto(protag)
loop_gioco(protag)