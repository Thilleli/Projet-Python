import csv
import itertools
import sys


def moyenne_dune_matiere_sans_leng(i):

    x = list()
    with open('notes1.csv', "r") as text_file:
        for line in itertools.islice(text_file, 2, numberlines()):
            note_etudiant = line.split(";")
            x.append(note_etudiant[i])
    
    somme = 0
    for i in range(0, len(x)):
        if (x[i]== "-"):
            somme += 0
        else :
            number = int(x[i])
            somme = somme + number
    sommme = int(somme)
    return sommme

def moyenne_dune_matiere(i):

    x = list()
    with open('notes1.csv', "r") as text_file:
        for line in itertools.islice(text_file, 2, numberlines()):
            note_etudiant = line.split(";")
            x.append(note_etudiant[i])
    
    somme = 0
    for i in range(0, len(x)):
        if (x[i]== "-"):
            somme = somme +  0
        else :
            number = int(x[i])
            somme = somme + number
    sommme = int(somme)/len(x)
    return sommme
def moyennes_tt_matiere():
    x = list()
    moyenne_fra = moyenne_dune_matiere(1)
    moyenne_anglais =  moyenne_dune_matiere(2)
    moyenne_math =  moyenne_dune_matiere(3)
    moyenne_info =  moyenne_dune_matiere(4)
    moyenne_sport =  moyenne_dune_matiere(5)
    moyenne_hist =  moyenne_dune_matiere(6)
    moyenne_geo =  moyenne_dune_matiere(7)
    moyenne_phy =  moyenne_dune_matiere(8)
    moyenne_eco =  moyenne_dune_matiere(9)
    '''moyenne_droi =  moyenne_dune_matiere(10)'''
    x.append(moyenne_fra)
    x.append(moyenne_anglais)
    x.append(moyenne_math)
    x.append(moyenne_info )
    x.append(moyenne_sport)
    x.append(moyenne_hist)
    x.append(moyenne_geo)
    x.append(moyenne_phy)
    x.append(moyenne_eco)
    '''x.append(moyenne_droi)'''
    print ( "la moyenne de francais "+ str(moyenne_fra)  )
    print ( "la moyenne de anglais  "+ str(moyenne_anglais)  )
    print ( "la moyenne de mathematiques  "+ str(moyenne_math)  )
    print ( "la moyenne de informatique  "+ str(moyenne_info)  )
    print ( "la moyenne de sport  "+ str(moyenne_sport)  )
    print ( "la moyenne de histoir  "+ str(moyenne_hist)  )
    print ( "la moyenne de geographie  "+ str(moyenne_geo)  )
    print ( "la moyenne de physique  "+ str(moyenne_phy)  )
    print ( "la moyenne de economie  "+ str(moyenne_eco)  )
    '''print ( "la moyenne de droit  "+ str(moyenne_droi)  )'''




def sommecoef():
    x = list()
    with open('notes1.csv', "r") as text_file:

            for line in itertools.islice(text_file, 1, 2):
                x = line.split(";")

    length = len(x)
    sommecoeff =  0
    for i in range(1,length):
        nombreCof = int(x[i])
        sommecoeff = sommecoeff + nombreCof
    return sommecoeff



def moyenne_pandree_tt_classe():
    somme_de_coef = int(sommecoef())

    listCoffff = ListCofie()
    coeffFra = int(listCoffff[1])
    coeffangl = int(listCoffff[2])
    coeffmath = int(listCoffff[3])
    coeffinfo = int(listCoffff[4])
    coeffsport = int(listCoffff[5])
    coeffhist = int(listCoffff[6])
    coeffgeo = int(listCoffff[7])
    coeffphy = int(listCoffff[8])
    coeffeco = int(listCoffff[9])
    coeffdroi = int(listCoffff[10])
    
    somme = 0 
    somme = somme + moyenne_dune_matiere(1)*coeffFra + moyenne_dune_matiere(2)*coeffangl 
    somme +=  moyenne_dune_matiere(3)*coeffmath + moyenne_dune_matiere(4)*coeffinfo 
    somme +=  moyenne_dune_matiere(5)*coeffsport + moyenne_dune_matiere(6)*coeffhist 
    somme +=  moyenne_dune_matiere(7)*coeffgeo + moyenne_dune_matiere(8)*coeffphy 
    somme +=   moyenne_dune_matiere(9)*coeffeco 
    #somme +=  moyenne_dune_matiere(10)*coeffdroi
    
    somme = somme / somme_de_coef
    print ("moyenne pandree de tous la  classe est : " + str(somme))
    
 

def moyenne_poduree_dun_module(module_nombre_colonne,coef):
    somme_de_coef = int(sommecoef())
    listCoffff = ListCofie()
    coeffFra = int(listCoffff[coef])
    x = int(moyenne_dune_matiere_sans_leng(module_nombre_colonne))
    somme = x * coeffFra
    somme = somme / somme_de_coef
    return somme 

def moyenne_poduree_de_tt_les_module ():
    print("La moyenne pondérée de francais est: "+ str(moyenne_poduree_dun_module(1,1))) 
    print("La moyenne pondérée d'anglais est: "+ str(moyenne_poduree_dun_module(1,2)))
    print("La moyenne pondérée de maths est: "+ str(moyenne_poduree_dun_module(1,3)))
    print("La moyenne pondérée d'informatique est: "+ str(moyenne_poduree_dun_module(1,4)))
    print("La moyenne pondérée de sport est: "+ str(moyenne_poduree_dun_module(1,5)))
    print("La moyenne pondérée d'histoire est: "+ str(moyenne_poduree_dun_module(1,6)))
    print("La moyenne pondérée de geo est: "+ str(moyenne_poduree_dun_module(1,7)))
    print("La moyenne pondérée de physique est: "+ str(moyenne_poduree_dun_module(1,8)))
    print("La moyenne pondérée d'economie est: "+ str(moyenne_poduree_dun_module(1,9)))
    print("La moyenne pondérée de droit est: "+ str(moyenne_poduree_dun_module(1,10)))

def numberlines():
    i = 0
    with open('notes1.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            i = i + 1
    return i 



def ListCofie():
    x = list()
    with open('notes1.csv', "r") as text_file:
        for line in itertools.islice(text_file, 0, 2):
            
            x = line.split(";")
            
    return x



somme_de_coef = int(sommecoef())
note_etudiant = list()

listCoffff = ListCofie()
coeffFra = int(listCoffff[1])
coeffangl = int(listCoffff[2])
coeffmath = int(listCoffff[3])
coeffinfo = int(listCoffff[4])
coeffsport = int(listCoffff[5])
coeffhist = int(listCoffff[6])
coeffgeo = int(listCoffff[7])
coeffphy = int(listCoffff[8])
coeffeco = int(listCoffff[9])
coeffdroi = int(listCoffff[10])
sys.tracebacklimit=0
with open('notes1.csv', "r") as text_file:
    for line in itertools.islice(text_file, 2, numberlines()):
        #print(line)
        note_etudiant = line.split(";")

        fran =  note_etudiant[1]
        if fran == '-':
            fran = 0
        else:
            fran = int(note_etudiant[1])

        angl = note_etudiant[2]
        if angl == '-':
            angl = 0
        else:
            angl = int(note_etudiant[2])

        math = note_etudiant[3]
        if math == '-':
            math = 0
        else:
            math = int(note_etudiant[3])

        info = note_etudiant[4]
        if info == '-':
            info = 0
        else:
            info = int(note_etudiant[4])

        sport = note_etudiant[5]
        if sport == '-':
            sport = 0
        else:
            sport = int(note_etudiant[5])

        hist = note_etudiant[6]
        if hist == '-':
            hist = 0
        else:
            hist = int(note_etudiant[6])

        geo = note_etudiant[7]
        if note_etudiant[7] == '-':
            geo = 0
        else:
            geo = int(note_etudiant[7])

        phy = note_etudiant[8]
        if phy == '-':
            
            phy = 0
        else:
            phy = int(note_etudiant[8])

        eco = note_etudiant[9]
        if eco == '-':
            eco = 0
        else:
            eco = int(note_etudiant[9])

        droi = note_etudiant[10]

        if droi == '-\n':
            droi = 0
        else:
            droi = int(note_etudiant[10])
      
        moyenn_etu = coeffFra*fran  #+  +  + +  +  +  +  +
        moyenn_etu += coeffangl*angl
        moyenn_etu += coeffmath*math
        moyenn_etu += coeffinfo*info
        moyenn_etu += coeffsport*sport
        moyenn_etu += coeffhist*hist
        moyenn_etu += coeffgeo*geo
        moyenn_etu += coeffphy*phy
        moyenn_etu += coeffeco*eco
        moyenn_etu += coeffdroi*droi




        vrai_moyen = moyenn_etu / somme_de_coef
    
        print("la moyenne pondérée de : "+ note_etudiant[0] + "  est egale = " + " " + str(vrai_moyen))
    

#♦---------------------------------------------------------------------------------------------------------------------------------------------
    print("---------------------------------------------------")
moyennes_tt_matiere()    
print("---------------------------------------------------")
    
moyenne_poduree_de_tt_les_module()
print("---------------------------------------------------")
moyenne_pandree_tt_classe()
    
    
    
print ("------------------------------------- MAX MIN----------------------------------- -----------")

 

    














