<html>
 <head>
   <title>Exemple de DOM Event</title>
   <style type="text/css">
     #t { border: 1px solid red }
     #t1 { background-color: pink; }
   </style>
   <script type="text/javascript">
   // fonction pour modifier le contenu de t2
   function modifieTexte() {
     var t2 = document.getElementById("t2");
     t2.firstChild.nodeValue = "trois";    
   }
   // fonction pour ajouter un écouteur à t
   function load() { 
     var el = document.getElementById("t"); 
     el.addEventListener("click", modifieTexte, false); 
   } 
   </script> 
 </head> 
 <body onload="load();"> 
 <table id="t"> 
   <tr><td id="t1">un</td></tr> 
   <tr><td id="t2">deux</td></tr> 
 </table> 



<p id="outputDiv">This is a test.</p>









<script>

var M=10;
var N=10;
var largeur=400;
var hauteur=300;
var mar=(largeur/100)-1;
var element=mar*N ;//l'espace entre les colonnes
var element1=(largeur-element)/(N+1) ;// le largeur des bloc
var element2=hauteur;

var el3=(hauteur-element)/(M+1);

var HTML = "<svg width="+largeur+"'px'"+"height="+hauteur+"'px' viewBox = '0 0 1000 500' color=black>";
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

</script>




 </body> 
 </html>

<!---
<!DOCTYPE HTML>
<html>
<head>
<style type="text/css">
p {
background: gray;
color: white;
padding: 10px;
margin: 5px;
border: thin solid black
}
</style>
</head>
<body>
<p>This is a test.</p>
<p id="block2">This is a test.</p>
<button id="pressme">Press Me</button>
<script type="text/javascript">
var pElems = document.getElementsByTagName("p");
for ( var i = 0; i < pElems.length; i++) {
pElems[i].addEventListener("mouseover", handleMouseOver);
pElems[i].addEventListener("mouseout", handleMouseOut);
}
document.getElementById("pressme").onclick = function() {
document.getElementById("block2").removeEventListener("mouseout",handleMouseOut);
}
function handleMouseOver(e) {
e.target.innerHTML += "mouseover";
e.target.style.background = 'red';
e.target.style.color = 'black';
}
function handleMouseOut(e) {
e.target.innerHTML += "mouseout";
e.target.style.removeProperty('color');
e.target.style.removeProperty('background');
}
</script>
</body>
</html> -->
