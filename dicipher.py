import sys

#recup le texte et l'affiche dans une liste
def recuptexte(nomSEC):
    
    texte = []
    with open(nomSEC,'r') as fichier:
        for ligne in fichier:
            texte.append(ligne)
    for k in range(len(texte)):
        texte[k] = texte[k][:-1]
    
    return texte

#Fonction permettant d'analyser le texte et d'utiliser le decalage de Cesar 
def cesar(texte):
    
    end = []
    cle = 9
    for ligne in texte:
        cont = ''
        for caractere in ligne:
            x = ord(caractere) - cle
            if 65 <= ord(caractere) <= 90:
                if x < 65:
                    x += 26
            if 97 <= ord(caractere) <= 122:
                if x < 97:
                    x +=26
            if caractere in '0123465789':
                x = ord(caractere)
            cont += chr(x)
        end.append(cont)
    return end

#fonction de chiffrage par subsitution
def substitution(texte):
   
    
    entree = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789;-'
    sortie = 'C6IE548YWwplbSD71tVrmeNi9FcLsBOKGyQPRZAq-gfXkz3oM2u;U0havjndJTxH'    
    resultat = []
    temp = ''
    for ligne in texte:
        for caractere in ligne:
            xcaractere = sortie.index(caractere)
            carac = entree[xcaractere]
            temp += carac
        resultat.append(temp)
        temp = ''
    return resultat

#affichage du texte correctement
    
def ecriture(texte, nomCSV):
    texte = '\n'.join(texte)
    if nomCSV == "None":
        print(texte)
    else:
        with open(nomCSV,'w')as fichier:
            fichier.write(texte)

nomSEC, nomCSV = sys.argv[1:3]
Texte = recuptexte(nomSEC)
dechiffrecesar = cesar(Texte)
chiffragesubs = substitution(dechiffrecesar)
ecriture(chiffragesubs, nomCSV)

#ouvrir le terminal est ecrire : python3 dicipher.py note1.sec wasef
