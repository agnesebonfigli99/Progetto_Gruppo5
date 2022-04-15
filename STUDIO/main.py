class Persona:
    def __init__(self, nome, cognome, sesso):
        self.nome = nome
        self.cognome = cognome
        self.sesso = maschio

    def saluta(self):
        print("ciao sono " + self.nome)

persona1 = Persona("Luca","Rossi")

persona1.saluta()

#COSTRUTTORE DEF __INIT__

#PARAMETRO SELF CI AIUTA A CAPIRE DI CHE ISTANZA (PERSONA1, PERSONA2) STIAMO PARLANDO

#SELF PERMETTE ALLA CLASSE DI CHE PERSONA SPECIFICA STIAMO PARLANDO
#IN PYTHON VA MESSO COME PRIMO PARAMETRO IN OGNI FUNZIONE

#del persona1.nome, rimuovo il nome


