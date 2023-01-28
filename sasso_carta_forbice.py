import random

mossa_utente = ""
utente = 0
computer = 0
mosse = [1, 2, 3];

while mossa_utente != 0 :
    

    print("\nFai la tua mossa");
    mossa_utente = int(input("Scegli tra:\n 1) sasso\n 2) carta\n 3) forbice\n 0) smetti di giocare\n"));
    mossa_computer = random.choice(mosse);

    if mossa_utente == 1 and mossa_computer == 1 :
        print("pareggio")
        print(f"utente: {utente} \ncomputer: {computer}")

    elif mossa_utente == 1 and mossa_computer == 2 :
        computer += 1
        print("Hai perso")
        print(f"utente: {utente} \ncomputer: {computer}")

    elif mossa_utente == 1 and mossa_computer == 3 :
        utente += 1
        print("Hai vinto")
        print(f"utente: {utente} \ncomputer: {computer}")

    elif mossa_utente == 2 and mossa_computer == 1 :
        utente += 1
        print("Hai vinto")
        print(f"utente: {utente} \ncomputer: {computer}")

    elif mossa_utente == 2 and mossa_computer == 2 :
        print("pareggio")
        print(f"utente: {utente} \ncomputer: {computer}")

    elif mossa_utente == 2 and mossa_computer == 3 :
        computer += 1
        print("Hai perso")
        print(f"utente: {utente} \ncomputer: {computer}")

    elif mossa_utente == 3 and mossa_computer == 1 :
        computer += 1
        print("Hai perso")
        print(f"utente: {utente} \ncomputer: {computer}")

    elif mossa_utente == 3 and mossa_computer == 2 :
        utente += 1
        print("Hai vinto")
        print(f"utente: {utente} \ncomputer: {computer}")

    elif mossa_utente == 3 and mossa_computer == 3 :
        print("pareggio")
        print(f"utente: {utente} \ncomputer: {computer}")

print("\nGrazie per aver giocato");
print(f"utente: {utente} \ncomputer: {computer}");
input("Premi invio per chiudere");






