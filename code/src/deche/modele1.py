#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:42:57 2017

@author: traoreb
"""



from command_line import learnfile
#from gurobipy import * 
from gurobipy import *


g=learnfile("0.txt","/home/traoreb/Bureau/MOGPLPROJET/code/instances/")


"=================================================="


def sequenceline(ligne,i):
    b=ligne[i]
    dt=b.split(' ')
    df=[]
    if str(dt[0])=='':
        dt=None
    else:
        for j in dt:
           df.append(int(j))
    dt=df
    return dt


def clean_list(m,deb,valadd):
    if deb+valadd<=m:
        res=range(deb,deb+valadd)
    else:
        res=range(deb,m)
    return res
"    print clean_list(6,4,5)"

#clean_list(6,4,5)


"=================================================="

m=g['M']
n=g['N']
line=g['line']
colone=g['colonne']

#Declaration des varaibles
#
try:
    model = Model("PLNE")
    #z = model.addVar(obj=1, vtype="C", name="z")
    y = {}
    x = {}
    z={}
    for j in range(m):
        for i in range(n):
            x[i,j] = model.addVar(obj=1,vtype="B", name="x[%s,%s]"%(i,j)) #pour definir les xij
            "declaration de la variable y tel que y[i,j,t]"         
            for t in range(len(sequenceline(line,i))):
                y[i,j,t+1]=model.addVar(vtype="B", name="y[%s,%s,%s]"%(i,j,t+1))
            "declaration de la variable z tel que z[i,j,t]"
            for t2 in range(len(sequenceline(colone,j))):
                z[i,j,t2+1]=model.addVar(vtype="B", name="z[%s,%s,%s]"%(i,j,t2+1))
    #####on definir les yijt########    
    model.update()  
    #model.write("PLNE.lp")
except:
    pass

#Declaration des contraintres#
#############################


"contraintres Q10 1 sur les lignes et les colonnes"
#(Q10) Formulez une contrainte qui exprime le fait que si le t ieme bloc de la ligne l i commence à la
#case (i, j), alors les cases (i, j) à (i, j + s t − 1) sont noires.    

try:
    for j in range(m):
        for i in range(n):
            for t in range(len(sequenceline(line,i))):
                model.addConstr(quicksum(y[i,j,t+1] for j in clean_list(m,j,int(sequenceline(line,i)[t])) ),"<=",int(sequenceline(line,i)[t]), name="linecontraintre[%s,%s,%s]"%(i,j,t+1))
            #contrainte sur les colonnes
            for t2 in range(len(sequenceline(colone,j))):
                model.addConstr(quicksum(z[i,j,t2+1] for i in clean_list(n,i,int(sequenceline(colone,j)[t2])) ),"<=",int(sequenceline(colone,j)[t2]), name="colonecontraintre[%s,%s,%s]"%(i,j,t2+1))
    model.update()  
    model.write("PLNE.lp")
except:
    print "errorpass"
    


"Formulez une contrainte qui exprime le décalage nécessaire entre le début des blocs s t et s t+1"
"de la ligne l i : si le t ieme bloc commence à la case (i, j), alors le (t + 1) ieme ne peut pas commencer sur les lignes et les colonnes"
#(Q10) Formulez une contrainte qui exprime le fait que si le t ieme bloc de la ligne l i commence à la
#case (i, j), alors les cases (i, j) à (i, j + s t − 1) sont noires.    
try:
    for i in range(n):
        for j in range(m):
            for t in range(len(sequenceline(line,i))):
                #model.addConstr(quicksum(y[i,j,t2+1] for i in clean_list(n,i,int(sequenceline(colone,j)[t2]))),
                print str(i)+str("app")+str(j)
                print t
                try:
                    model.addConstr(y[i,j,t+1]+y[i,j+int(sequenceline(line,i)[t]),t+2],"<=",1, name="Q12[%s,%s,%s]"%(i,j,t+1))
                    #model.addConstr(y[i,j,t+1]+y[i,j+int(sequenceline(line,i)[t])-1,t+2],"<=",1, name="Q12[%s,%s,%s]"%(i,j,t+1))
                except:
                    pass
    model.update()  
except:
    print "errorpass"

#i=2    
#print range(len(sequenceline(line,i))+1)    
#formulation d'une contraintre pour mettre xij a 1 ou a 0
#
try:
    for j in range(m):
        for i in range(n):
            model.addConstr((quicksum(y[i,j,t3+1] for t3 in range(len(sequenceline(line,i)))))*(quicksum(z[i,j,t4+1] for t4 in range(len(sequenceline(colone,j))))),"=",x[i,j], name="coloneedalitedesxi[%s,%s,%s]"%(i,j,1))
    model.update
except:
    print "attention1"#pass


#formulation d'un contraintre tel que sur une ligne i considere sum sur j et sum sur t doit etre egale a sum(st)

try:
    for i in range(n):
        model.addConstr((quicksum(y[i,j,t5+1] for t5 in range(len(sequenceline(line,i))) for j in range(m))),"=",sum(sequenceline(line,i)), name="somdeslignesyi[%s,%s,%s]"%(i,j))
        #model.addConstr(quicksum(y[i,j,t5+1] for t5 in range(len(sequenceline(line,i))) for j in in range(m)),"=",sum(sequenceline(line,i)), name="linecontraintre[%s,%s,%s]"%(i,j,t+1))
except:
    print "att"
# Setting the objective.
obj = LinExpr()
obj += quicksum(quicksum(x[i,j] for j in range(m)) for i in range(n))
model.setObjective(obj, GRB.MAXIMIZE)
model.Params.OutputFlag=0
model.update()  
model.write("PLNE.lp")
model.optimize()    
#
for v in model.getVars():
    if str(v.varName[0:3])=='x[3':#if str(v.varName[0:3])=='y[2':
        print(v.varName,v.x)
    else:
        pass

#*(quicksum(z[i,j,t4+1] for t4 in range(len(sequenceline(colonne,j)))))