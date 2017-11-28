//alert("toto");

//try innherHTML
//Question 1
//////var a=prompt("Veuillez saisir votre nom");
//////document.getElementById("my1").innerHTML=a;


// exercice 3
/*
var a=prompt("Veuillez saisir votre X");

var table = document.getElementById("myTable");
// Create an empty <tr> element and add it to the 1st position of the table:
var row = table.insertRow(0);
// Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);
var cell3 = row.insertCell(2);
cell1.innerHTML = "X";
cell2.innerHTML = "Y";
cell3.innerHTML = "Resultat";
for (i=1;i<=a;i++){
var k=a-i    
var row1 = table.insertRow(1);
var cell4 = row1.insertCell(0);
var cell5 = row1.insertCell(1);
var cell6 = row1.insertCell(2);
// Add some text to the new cells:
cell4.innerHTML = a;
cell5.innerHTML = k;
cell6.innerHTML = a*k;
}

*/

/*
4 Exercice
Ecrire en javascript le jeu (( devine )). 
Le programme choisit un nombre au hasard entre 0 et 100 que l’utilisateur doit deviner en un nombre minimum de coups. 
Pour cela, il propose des nombres et à chaque proposition le programme répond si la valeur à trouver est plus petite ou plus grande. 
Quand la valeur est trouvée, on aﬃche dans une fenêtre le nombre de tentatives eﬀectuées. 
Veillez à bien découper votre script en fonctions et à utiliser le bon format de boite de dialogue en fonction des cas. 
Pour la génération aléatoire, vous utiliserez la fonction :
*/

/*===============================Devinette=============================================*/

//renvoie un nombre pseudo-aléatoire entre min et max
function nbAlea(min, max) {   
    var nb = min + (max - min + 1) * Math.random();   
    return Math.floor(nb);
    }
    

/*=== deviner*/

function verification(nbrs,cpt,value){
    var cpt1=cpt+1;
    if (value>nbrs)
    {
        alert("s'est plus");    
    } else if (value<nbrs) 
    {
        alert("s'est moins");    
    } else {
    alert("Cool");
    cpt1=0    
    };
    return cpt1
}

var minn=prompt("Veuillez saisir votre le min"); 
var maxim=prompt("Veuillez saisir votre le maxim");

var data=[];
var dataglobal=[];
var quite="oui";
function run(minn,maxim){
    var nobrs1=nbAlea(parseInt(minn),parseInt(maxim));
    alert(minn);
    alert(maxim);    
    var cpt=1;
    alert(nobrs1);    
    while (cpt!=0){
        var a=prompt("Veuillez saisir le nombre");
        cpt=verification(a,cpt,nobrs1);
        if (cpt!=0){
        alert(cpt);
        };
        if (quite=="oui"){
            data.push([minn,maxim,cpt,nobrs1]);                
            cpt=0;           
        };    
    };
};

//var minn=10;
//var maxim=100;

//var p=document.getElementById("my1");

run(minn,maxim);
alert(data);
//var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};

/*Vous devez ensuite améliorer le jeu en laissant l’utilisateur choisir l’intervalle de la valeur,
 en permettant d’eﬀectuer plusieurs parties avec le même intervalle,

en ajoutant une gestion du meilleur score obtenu dans la série de parties et 
en permettant au joueur de quitter une partie en cours. 
==========creation d'une variable pour stocker les informations et la reprendre ======
besoin d'un object partie{minn,maxim,le nombre de tentative, et le resultat lorsqu'il quitta la partie }
======================================================================================
Pour ﬁnir, vous utiliserez vos connaissances en html et css pour améliorer la mise en page et gérer l’aﬃchage,
dans un tableau par exemple, des 5 meilleurs scores.*/