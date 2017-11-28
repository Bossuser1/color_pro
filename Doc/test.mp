/opt/gurobi701/linux64/examples/data/coin.lp
file:///opt/gurobi701/linux64/docs/quickstart_linux/reading_and_optimizing_a_m.html

en mode sudo-i
mais sur l'environement voulu PS ici il est sur mon eniornement Bureau/3/
/opt/gurobi701/linux64/ 
python setup.py install

m = read('/opt/gurobi701/linux64/examples/data/coin.lp')

/opt/gurobi751/linux64/


acces refuser sur le pc le upmc

sh gurobi.sh

/opt/gurobi751/linux64/bin

/opt/gurobi751/linux64/bin

/opt/gurobi605/linux64/bin/python2.7

poste de connexion
ssh -X 3525553@ssh.ufr-info-p6.jussieu.fr
ssh -X ppti-14-302-02.ufr-info-p6.jussieu.fr
ppti-14-302-02

ouvrir son .bashrc

avec gedit ./bashrc

faire la mise a jour 
https://blog.shevarezo.fr/post/2015/06/18/personnaliser-prompt-bash-linux-terminal-bashrc
=================
NC="\[\e[0m\]"
NOIR="\[\e[30;1m\]"
VERT="\[\e[32;40m\]" #"\033[0;32;40m"
JAUNE="\[\e[33;40m\]" #"\033[0;33;40m"

export PS1="$NOIR[\t] $NC\u@\h:$JAUNE\w $VERT>$NC "
pour faire le fun ===========

et faire source .bashrc

apres cette mise a jour nous avons gurobi.sh qui apparait parmi la liste des programmes

Testons 

il marche sur spyder et la commande shell 
gurobi.sh


ecrivons un bash shell qui prend un ssh et qui refaire un ssh une fois de plus

===
% ssh -L 2012:serveur.exemple.org:80 toto@serveur.exemple.org
ssh -X 3525553:ppti-14-302-02@ssh.ufr-info-p6.jussieu.fr

ssh -X 3525553:ppti-14-302-02.ufr-info-p6.jussieu.fr@ssh.ufr-info-p6.jussieu.fr

=====Apres avoir passer un bout de temps on essayera avec Popen subprocess sur un programm python

