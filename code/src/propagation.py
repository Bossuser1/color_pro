#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:56:47 2017

@author: traoreb
"""

import numpy as np
from command_line import learnfile


"pour comprendre on va faire un jeux"
"================================== "
"ligne * colonne=resultat           "
"Noir  * Noir = Noir                "
"Blanc * Noir = gris                "
"Noir  * blanc=gray                 "
"blanc * blanc=blanc                "
"juste pour comprendre et afficher  "
"Noir_ligne=3  Noir_colone=-4       "
"blanc_ligne=2  blanc_colone=-2     "
"3  * -4 = -1  (Noir)               "
"2 * -4 = -2   (gris)               "
"3  * -2=1     (gray)               "
"2 * -2=0      (blanc)              "
" * est une loi de composition      "
"interne donc je fais ce que je veux"
" ici * est l'addition              "
"pour les non encors explorer  blue plat"
"blue =10  ligne comme colonne      "
"blue*blue=20                       "
"blue*autres=20                     "
"==================================="
"mais pour les couleur finaux demander conseils"



g=learnfile("0.txt","/home/traoreb/Bureau/MOGPLPROJET/code/instances/")
"lecture de N et M dans un fichier"

def dynamicTesting(A,i,colo='noir'):
    res=colo
    res=A
    res=i
    if i==1:
        res=True
    elif i==2:
        res=False
    elif i==3:
        res=True
    elif i==4:
        res=False
    else:
        res=True
    #res=np.random.choice([True, False])
    return res

def teststatisfaction(A,i,liste_pos,option='ligne'):
    el=np.random.choice(liste_pos)
    new_liste=[]
    for el1 in liste_pos:
        new_liste.append(el1)
    if (dynamicTesting(A,i,colo='noir')==False and dynamicTesting(A,i,colo='blanc')==False):
        res=0
    elif (dynamicTesting(A,i,'Noir')==True and dynamicTesting(A,i,'blanc')==False):
        if option!='ligne':
            res=-4
        else:
            res=3
    elif (dynamicTesting(A,i,'blanc')==True and dynamicTesting(A,i,'Noir')==False):
        if option!='ligne':
            res=-2
        else:
            res=2
    else:
        res=25
    return res,el,new_liste

#
#    
#def coloration(g,LignesAVoir,ColonnesAvoir):
#    "definir un dictionnaire des elements avec leur code couleurs"
#
#    Nouveauxligne={}
#    Nouveauxcolonne={}
#    cpt=0
#    marquage=1000
#    "pour commencer de tester avec j_1"
#    while (set(LignesAVoir.values())!={marquage} or set(ColonnesAvoir.values())!={marquage}):
#        for i in LignesAVoir.keys():
#            if LignesAVoir[i]!=marquage:
#                "selection de j la nouvelle case coloriée"
#                t1_test,j_1=teststatisfaction('to',i,'ligne')
#                #if t1_test!=10:  
#                Nouveauxcolonne[j_1]=t1_test
#                ColonnesAvoir[j_1]=t1_test
#                "marquage de la ligne i car deja visité"
#                LignesAVoir[i]=marquage
#        for j in ColonnesAvoir.keys():
#            if ColonnesAvoir[j]!=marquage:
#                "selection de j la nouvelle case coloriée"
#                t2_test=teststatisfaction('to',j,'colonne')
#                i_1=i_1+1
#                #if t2_test!=10:  
#                Nouveauxligne[i_1]=t2_test
#                ColonnesAvoir[i_1]=t2_test
#                "marquage de la colonne i car deja visité"
#                ColonnesAvoir[j]=marquage
#
#        #functionjeuxcolore(LignesAVoir,ColonnesAvoir)
#        cpt=cpt+1
#        arret=(set(LignesAVoir.values())=={marquage} or set(ColonnesAvoir.values())=={marquage} )
#        print arret
#        print i_1
#        print j_1
#        if (cpt==100 or set(LignesAVoir.values())=={marquage} and set(ColonnesAvoir.values())=={marquage}):
#            j_1=0
#            i_1=0
#            break
#    
#    return LignesAVoir,ColonnesAvoir,Nouveauxligne,Nouveauxcolonne
#

#    
#def coloration2(g):
#    "definir un dictionnaire des elements avec leur code couleurs"
#    LignesAVoir={}
#    ColonnesAvoir={}
#    for j in range(0,int(g['N'])):
#        LignesAVoir[j]=10
#    for k in range(0,int(g['M'])):  
#        ColonnesAvoir[k]=10        
#    Nouveauxligne={}
#    Nouveauxcolonne={}
#    Nouveaux={}
#    cpt=0
#    liste_posj=range(0,int(g['N']))
#    liste_posi=range(0,int(g['M']))
#    #marquage=1000
#    "pour commencer de tester avec j_1"
#    while (LignesAVoir.keys()!=[] or ColonnesAvoir.keys()!=[]):
#        for i in LignesAVoir.keys():
#                "selection de j la nouvelle case coloriée"
#                t1_test,j_1,liste_posj=teststatisfaction('to',i,liste_posj,'ligne')
#                #if t1_test!=10:  
#                Nouveauxcolonne[j_1]=t1_test
#                Nouveaux[j_1]={'j':t1_test}
#                ColonnesAvoir.update(Nouveauxcolonne)
#                "marquage de la ligne i car deja visité"
#                LignesAVoir.pop(i)
#        #print "tot2"
#        #print ColonnesAvoir
#        for j in ColonnesAvoir.keys():
#                #if ColonnesAvoir[j]!=marquage:
#                "selection de j la nouvelle case coloriée"
#                t2_test,i_1,liste_posi=teststatisfaction('to',j,liste_posi,'colonne')
#                #i_1=i_1+1
#                #if t2_test!=10:  
#                Nouveauxligne[i_1]=t2_test
#                #LignesAVoir[i_1]=t2_test
#                Nouveaux[i_1]={'i':t2_test}
#                LignesAVoir.update(Nouveauxligne)
#                "marquage de la colonne i car deja visité"
#                ColonnesAvoir.pop(j)
#        #print "tot1"        
#        #print LignesAVoir
#        #functionjeuxcolore(LignesAVoir,ColonnesAvoir)
#        cpt=cpt+1
#        #arret=(LignesAVoir.keys()==[] and ColonnesAvoir.keys()==[])
#        #print arret
#        print cpt
#        print "colonne"
#        print Nouveauxcolonne
#        print "line"
#        print Nouveauxligne
#        #print Nouveaux
#        if (cpt==1000 or LignesAVoir.keys()==[] and ColonnesAvoir.keys()==[]):
#            break
#    return LignesAVoir,ColonnesAvoir,Nouveauxligne,Nouveauxcolonne
#
#
#
#
#
#LignesAVoir1,ColonnesAvoir1,Nouveauxligne1,Nouveauxcolonne1=coloration2(g)
#


" Initilisation du dictionaire                      "
"==================================================="

listej={}
for j in range(0,int(g['M'])):
    listej[j]=10    
listei={}
for i in range(0,int(g['N'])):
    listei[i]=10    


Data_stockage={}
for i in range(0,int(g['N'])):
        Data_stockage[str({"i":i})]=listej
for j in range(0,int(g['M'])):
        Data_stockage[str({"j":j})]=listei

"======================================================="
"      Test dynamique                                   " 
"======================================================="

def testold_new(Data_stockage,i,j,value,direction='ligne'):
    "test si la couleur est de la case est nouvelle"
    "pour affiner Nouveaux"
    "testold_new(Data_stockage,3,1,10,'colonne')"
    "Data_stockage etant le dictionnaire des elements i,j "
    "si nouvelle valeur il retourne faux"
    "si ancien valeur il retourne vrai"
    res=False
    if direction=="ligne":
        res=(int(Data_stockage[str({'i':i})][j])==value)
    elif direction=="colonne":
        res=(int(Data_stockage[str({'j':j})][i])==value)
    return res


def listeNouveaux(Data_stockage,i,j,value,Nouveaux_lista,direction='ligne'):    
    if direction=='ligne':
        if testold_new(Data_stockage,i,j,value,direction)==False:#Nouveau
            Nouveaux_lista[str({'j':j})]=str({'i':i})
            Data_stockage[str({'i':i})][j]=value
        elif testold_new(Data_stockage,i,j,value,direction)==True:#Ancinne
             "recharger l'ancienne liste"
             Nouveaux_lista=Nouveaux_lista
    
    elif direction=="colonne":
        if testold_new(Data_stockage,i,j,value,direction)==False:#Nouveau
            Nouveaux_lista[str({'i':i})]=str({'j':j})
            Data_stockage[str({'j':j})][i]=value
        elif testold_new(Data_stockage,i,j,value,direction)==True:#Ancinne
             "recharger l'ancienne liste"  
             Nouveaux_lista=Nouveaux_lista
    return Data_stockage,Nouveaux_lista


"donne la liste des nouveaux"
def get_Nouveaux(Nouveaux_lista,direction='ligne'):
    given_liste={}
    if direction=='ligne':
        "retuourne une liste identique a celle de colonne"
        for el in Nouveaux_lista.keys():
            if el[0:5]==str("{'j':"):
                print el[0:5]
                given_liste[int(el[5:len(el)-1])]=el 
    elif direction=="colonne":
        "retuourne une liste identique a celle de ligne"
        for el in Nouveaux_lista.keys():
            if el[0:5]==str("{'i':"):
               given_liste[int(el[5:len(el)-1])]=el
    return given_liste

def miseajour(listeA,listeB):
    try:
        res=listeA.update(listeB)
    except:
        try:
            res=listeB.update(listeA)
        except:
            if listeB!=None:
                res=listeB
            elif listeA!=None:
                res=listeA
            else:
                res=[]
    return res

    #    if listeB.keys()!=[]:
#        for key1 in listeA.keys():
#            if key1 in listeB.keys():
#               listeA[str(key1)+str("_")]=listeB[key1] 
#            else:
#                listeA[key1]=listeB[key1]
#        res=listeA
#    elif listeA.keys()!=[]:
#        for key1 in listeB.keys():
#            if key1 in listeA.keys():
#               listeB[str(key1)+str("_")]=listeA[key1] 
#            else:
#                listeB[key1]=listeA[key1]
#        res=listeB
#    else:
#        res=listeA

"==============================================================="
"==============================================================="
run=True

if run:
    Nouveaux_lista={}
    LignesAVoir={}
    ColonnesAvoir={}
    for j in range(0,int(g['N'])):
        LignesAVoir[j]=10
    for k in range(0,int(g['M'])):  
        ColonnesAvoir[k]=10        
    while (LignesAVoir!=None or ColonnesAvoir!=None or LignesAVoir.keys()!=[] or ColonnesAvoir.keys()!=[]):
        for i in LignesAVoir.keys():
            direction='ligne'
            "liste des nouveaux"
            value=np.random.choice(range(0,2))
            j=np.random.choice(range(0,int(g['M'])))
            Data_stockage,Nouveaux_lista=listeNouveaux(Data_stockage,i,j,value,Nouveaux_lista,direction)
            #Nouveaux"
            "liste des nouveaux"
            Nouveauxdire=get_Nouveaux(Nouveaux_lista,direction)
            print Nouveauxdire
            #ColonneA voir U Nouveaux#
            "colonne A voir union nomuveau"
            ColonnesAvoir=miseajour(ColonnesAvoir,Nouveauxdire)
            print ColonnesAvoir
            LignesAVoir.pop(i)
            
        for j in ColonnesAvoir.keys():
            direction='colonne'
            value=np.random.choice(range(0,5))
            
            i=np.random.choice(range(0,int(g['N'])))
            "liste des nouveaux"
            Data_stockage,Nouveaux_lista=listeNouveaux(Data_stockage,i,j,value,Nouveaux_lista,direction)
            #Nouveaux"
            "liste des nouveaux"
            Nouveauxdire=get_Nouveaux(Nouveaux_lista,direction)
            #ligneA voir U Nouveaux#
            "ligne A voir union nomuveau"
            LignesAVoir=miseajour(LignesAVoir,Nouveauxdire)
            
            ColonnesAvoir.pop(j)
            
    #listej={}
    #for j in range(0,int(g['M'])):  
    #    listej[j]=10    
    #listei={}
    #for i in range(0,int(g['N'])):
    #    listei[i]=10    
    #Newdata={}
    #if direction=="ligne":
    #    Newdata[str({"i":i})]=Data_stockage[str({"i":i})]
    #    #(int(Data_stockage[str({'i':i})][j])==value)
    #elif direction=="colonne":
    #    res=(int(Data_stockage[str({'j':j})][i])==value)
    #    

    #    for i in range(0,int(g['N'])):
    #        Data_stockage[str({"i":i})]=listej
    #    for j in range(0,int(g['M'])):
    #        Data_stockage[str({"j":j})]=listei
    
    

#if testold_new(Data_stockage,i,j,value,direction='ligne')
#
#
#listej[]=[]
#
#print testold_new(Data_stockage,3,1,5,'colonne')
#
#for i in ligneAvoir:
#    Data_stockage[str({'i':3})]    
#

#def functionjeuxcolore(LignesAVoir,ColonnesAvoir):
#    print LignesAVoir
#    print "toto"
#    print ColonnesAvoir

#
#def initialcoloration(g):
#    LignesAVoir={}
#    ColonnesAvoir={}
#    for j in range(0,int(g['N'])):
#        LignesAVoir[j]=10
#    for k in range(0,int(g['M'])):  
#        ColonnesAvoir[k]=10
#    for m in range(0,10):
#        if m==0:
#            LignesAVoir1,ColonnesAvoir1,Nouveauxligne1,Nouveauxcolonne1=coloration(g,LignesAVoir,ColonnesAvoir)
#        else:
#            LignesAVoir1,ColonnesAvoir1,Nouveauxligne1,Nouveauxcolonne1=coloration(g,Nouveauxligne1,Nouveauxcolonne1)
#    return Nouveauxligne1,Nouveauxcolonne1
#
#sol1,slo2=initialcoloration(g)