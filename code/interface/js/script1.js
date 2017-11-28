
//function 1
function myFunction(M,N) {
var largeur=400;
var hauteur=300;
var mar=(largeur/100)-1;
var element=mar*N ;//l'espace entre les colonnes
var element1=(largeur-element)/(N+1) ;// le largeur des bloc
var element2=hauteur;

var el3=(hauteur-element)/(M+1);

var HTML ="<svg width="+largeur+"'px'"+"height="+hauteur+"'px' viewBox = '0 0 1000 500' color=black>";
var te=0;
var ts=(hauteur/100)-1;
var marg=(hauteur-(ts+te)*(M+M))/(M+M);
for (k=1;k<=M;k++)
{
for(j=1;j<=N;j++)
{    
    HTML += "<rect x='"+(element1*(j-1)+(mar*j))+"' y='"+(te+(marg+ts)*(k-1))+"' width='"+element1+"'height='"+marg+"' fill='blue' />"; //longeur
};
}
HTML += "</svg>";
document.getElementById("outputDiv").innerHTML = HTML;
}

