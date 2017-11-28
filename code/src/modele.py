#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:11:33 2017

@author: traoreb
"""



from command_line import learnfile
#from gurobipy import * 
from gurobipy import *

import sys

try:
   if len(sys.argv[1].split("instances/"))>1:
       filenames=sys.argv[1].split("instances/")
       filename=filenames[1]#"16.txt"
       director=filenames[0]+'instances/'
   else:
       filenames=sys.argv[1].split("newfile/")
       filename=filenames[1]#"16.txt"
       director=filenames[0]+'newfile/'
except:
    print "pass de bon fichier"
g=learnfile(filename,director)


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




"=================================================="

m=g['M']
n=g['N']
line=g['line']
colone=g['colonne']


"============================================================================"


"======Initialisation des variables===="
try:
    model=Model("PLNE")
    x = {}
    for j in range(m):
        for i in range(n):
            x[i,j] = model.addVar(obj=1,vtype="B", name="x[%s,%s]"%(i,j)) #pour definir les xij
    model.update()  
except:
    print ("errorpass")

##
#for i in range(n):
#    "somme xij=sum(li)"
#    model.addConstr(quicksum(x[i,j] for j in range(m)),"=",sum(sequenceline(line,i)),name="xj[%s]"%(i)) 
##
#for j in range(m):
#    "somme xij=sum(li)"
#    model.addConstr(quicksum(x[i,j] for i in range(n)),"=",sum(sequenceline(colone,j)),name="xi[%s]"%(j)) 
#
"=====sous modèle suffisant pour placé mes elements sur la case , maintenant equilibront les positions"

"decalaration des yijk et zijk (en autres des projectes de cordonnées x sur l'axes des abscisses , et des ordonnées , mais avec une variante de k pour definir le numeros du bloc"

y = {}
z={}
for j in range(m):
    for i in range(n):
        "declaration de la variable y tel que y[i,j,t]"         
        for t in range(len(sequenceline(line,i))):
            y[i,j,t+1]=model.addVar(vtype="B", name="y[%s,%s,%s]"%(i,j,t+1))
        "declaration de la variable z tel que z[i,j,t]"
        for t2 in range(len(sequenceline(colone,j))):
            z[i,j,t2+1]=model.addVar(vtype="B", name="z[%s,%s,%s]"%(i,j,t2+1))
    #####on definir les yijt########    
    model.update()  

"contraintre 1 xij=sum"

for j in range(m):
    for i in range(n):
         model.addConstr(quicksum(y[i,j,k+1] for k in range(len(sequenceline(line,i))))*quicksum(z[i,j,k1+1] for k1 in range(len(sequenceline(colone,j)))),"=",x[i,j],name="xi[%s,%s]"%(i,j))
model.update()  

#
#for i in range(n):
#    for t1 in range(len(sequenceline(line,i))):
#        model.addConstr(quicksum(y[i,j,t1+1] for j in range(m)),"=",int(sequenceline(line,i)[t1]),name="t1[%s,%s]"%(i,t1))
#
#for j in range(m):
#    for t2 in range(len(sequenceline(colone,j))):
#        model.addConstr(quicksum(z[i,j,t2+1] for i in range(n)),"=",int(sequenceline(colone,j)[t2]),name="t2[%s,%s]"%(j,t2))

model.update()  



"Q9"


for i in range(n):
      model.addConstr(quicksum(y[i,j,t1+1] for j in range(m) for t1 in range(len(sequenceline(line,i))) ),"=",sum(sequenceline(line,i)),name="t1_1[%s]"%(i))

for j in range(m):
      model.addConstr(quicksum(z[i,j,t2+1] for i in range(n) for t2 in range(len(sequenceline(colone,j))) ),"=",sum(sequenceline(colone,j)),name="t2_1[%s]"%(j))

model.update()  



"Q10"
a=1
b=1
c=0

kl=0
for j in range(m):
    for i in range(n):
        for t3 in range(len(sequenceline(line,i))):
            kl=kl+1
            st=int(sequenceline(line,i)[t3])
            if len(clean_list(m,j,j+st+c))>=st:
                model.addConstr(quicksum(y[i,k,t3+1] for k in clean_list(m,j,j+st+a)[0:st+b]),"<=",int(sequenceline(line,i)[t3]),name="t3[%s,%s,%s]"%(kl,j,t3))
            else:
               model.addConstr(quicksum(y[i,k,t3+1] for k in clean_list(m,j,j+st+a)),"<=",int(sequenceline(line,i)[t3]),name="t3[%s,%s,%s]"%(kl,j,t3))                
            st=0
"Q10b colonne "

#model.addConstr(y[3,4,1],"=",1,name="PAPA")
#model.addConstr(y[3,3,1],"=",1,name="PAPA2")

kl=0
for j in range(m):
    for i in range(n):
        for t4 in range(len(sequenceline(colone,j))):
            kl=kl+1
            st=int(sequenceline(colone,j)[t4])
            if len(clean_list(m,i,i+st+c))>=st:
                model.addConstr(quicksum(z[k1,j,t4+1] for k1 in clean_list(n,i,i+st+a)[0:st+b]),"<=",int(sequenceline(colone,j)[t4]),name="t4[%s,%s,%s]"%(kl,j,t4))
            else:
                model.addConstr(quicksum(z[k1,j,t4+1] for k1 in clean_list(n,i,i+st+a)),"<=",int(sequenceline(colone,j)[t4]),name="t4[%s,%s,%s]"%(kl,j,t4))                
            st=0
#
#
#print range(len(sequenceline(line,3)))
#print len(sequenceline(line,3))
#print sequenceline(line,3)
"contraintre sur le debut de la sequence (Q11)"


kl=0
for j in range(m):
    for i in range(n):
        for t5 in range(len(sequenceline(line,i))):
            kl=kl+1
            st=int(sequenceline(line,i)[t5])
            try:
                if j+st+1<m:
                    model.addConstr(y[i,j+st,t5+2],"<=",y[i,j,t5+1],name="t5[%s,%s,%s]"%(kl,j,t5))                
            except:
                pass
            st=0
            

#
kl=0
for j in range(m):
    for i in range(n):
        for t6 in range(len(sequenceline(colone,j))):
            kl=kl+1
            st=int(sequenceline(colone,j)[t6])
            try:
                if i+st+1<n:
                    model.addConstr(z[i+st,j,t6+2],"<=",z[i,j,t6+1],name="t6[%s,%s,%s]"%(kl,j,t6))                
            except:
                pass
            st=0





#
#
#for j in range(m):
#        for i in range(n):
#            try:
#                if len(sequenceline(line,i))>=0:
#                    for t in range(len(sequenceline(line,i))): 
#                        model.addConstr(y[i,j,t+1]+y[i,j+int(sequenceline(line,i)[t])+1,t+2],"<=",1, name="Qline[%s,%s,%s]"%(i,j,t+1))
#            except:
#                pass
#            try:
#                if len(sequenceline(colone,j))>=0:
#                    for t1 in range(len(sequenceline(colone,j))): 
#                        model.addConstr(z[i,j,t1+1]+z[i+int(sequenceline(colone,j)[t1])+1,j,t1+2],"<=",1, name="Qcolon[%s,%s,%s]"%(i,j,t1+1))
#            except:
#                pass
#            #for t2 in range(len(sequenceline(line,i))-1)
"contrainte sur les sequences occupées"
#
#for j in range(m):
#        for i in range(n):
#            st=int(sequenceline(line,i)[t])
#            model.addConstr(quicksum(y[i,j,t+1] for k in range(i,i+st-1)),"=",st,name="q10[%s,%s,%s]"%(i,j,t)) 
#
#            
#            #if len(sequenceline(line,i))>1:
#            #        for t in range(len(sequenceline(line,i))-1):
#            #            st=int(sequenceline(line,i)[t])
#            #            model.addConstr(quicksum(y[k,j,t+1] for k in range(i,i+st-1)),"=",st,name="q10[%s,%s,%s]"%(i,j,t)) 

model.update()  

  
obj = LinExpr()
obj += quicksum(quicksum(x[i,j] for j in range(m)) for i in range(n))
model.setObjective(obj, GRB.MAXIMIZE)
#Set           a           2           second           time           limit
model.Params.timeLimit=2*60
model.Params.OutputFlag=0
model.update()  
model.write("22.lp")
model.optimize()    
#
#for v in model.getVars():
#    if str(v.varName[0:2])=='x[':
#        print(v.varName,v.x)
#    else:
#        pass
"====pour printer la solution finale========="
message=[]
if   model.status==GRB.Status.OPTIMAL:
     message.append("Resolu")
     message.append("Time")
     for v in model.getVars():
         if str(v.varName[0:2])=='x[':
             message.append((v.varName,v.x))
elif model.status!=GRB.Status.OPTIMAL:
     message.append("Non Resolut")   
     #exit(0)

with open(filenames[0]+"solution/PLNE/"+filename,'w') as writeur:
    for j in range(len(message)):
        if j<2:
            writeur.writelines(str(message[j]))
	    print str(message[j])
        else :
            writeur.writelines(str(message[j][0]))
            writeur.writelines(str("="))
            writeur.writelines(str(message[j][1]))
	    print str(message[j][0])+"="+str(message[j][1])
        writeur.writelines("\n")
	#print "\n"
    writeur.close()
            
    
#print "attet"    
#for v in model.getVars():
#    if str(v.varName[0:3])=='x[2':
#        print(v.varName,v.x)
#    else:
#        pass
#
#nSolutions = model.SolCount
#
## Print objective values of solutions
#for e in range(nSolutions):
#    model.setParam(GRB.Param.SolutionNumber, e);
#    print e
#    for v in model.getVars():
#        if str(v.varName[0:3])=='x[0':
#            print(v.varName,v.x)
#        else:
#            pass
#    print str("=========suivant======")
##
#nSolutions = model.SolCount
#print('Number of solutions found: ' + str(nSolutions))
## Limit how many solutions to collect
#model.setParam(GRB.Param.PoolSolutions, 1024)
##model.setParam(SolutionNumber, 3);
