<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title id="my1">PNLE SOLVE</title>
    <link href='../css/1italic.css' rel='stylesheet' type='text/css'>

    <link rel="stylesheet" href="../css/bootstrap.min.css" integrity="sha384-AysaV+vQoT3kOAXZkl02PThvDr8HYKPZhNT5h/CXfBThSRXQ6jW5DO2ekP5ViFdi" crossorigin="anonymous">

    <link rel="stylesheet" href="../css/awesome.css">
    <link rel="stylesheet" href="../css/css_styles.css" />
</head>

<body >
<nav class="navbar navbar-default navbar-fixed-top">
    <div class="container">
        <a class="navbar-brand page-scroll" href="index.php">
			<span class="fa fa-anchor" style="font-size:18px;"></span>
		</a>
        <div class="collapse navbar-toggleable-sm" id="collapsingNavbar">
            <ul class="nav navbar-nav">
                <li class="nav-item">
                    <a class="facebook">'     '</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link page-scroll" href="../index.php"> RETOUR </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link page-scroll" > </a>
                </li>
            </ul>
			<ul class="nav navbar-nav float-xs-right">
                <li class="nav-item">
                    <a class="nav-link page-scroll" data-toggle="modal" title="Information sur le site" href="#aboutModal"> </a>
                </li>
			</ul>
        </div>
    </div>
</nav>
<!-- bar de menu    -->
<aside class="bg-faded">
    <div class="container text-xs-center">
        <div class="row">
            <div class="col-md-4 col-sm-6 col-xs-12 text-xs-center">
                <h3>Toujours en construction</h3>
                <i class="fa fa-cogs fa-4x"></i>
                <p class="text-primary">Mise à jour fréquente</br>
					Amélioration continue</p>
            </div>
            <div class="col-md-4 col-sm-6 col-xs-12 text-xs-center">
                <h3>Toujours en contact</h3>
                <i class="fa fa-comments fa-4x"></i>
                <p class="text-primary">Des commentaires sous chaque tutoriel</br>
					Contact par mail réactif</h2>
            </div>
            <div class="col-md-4 col-sm-6 col-xs-12 text-xs-center">
                <h3>Toujours plus</h3>
                <i class="fa fa-bolt fa-4x"></i>
                <p class="text-primary">Vous avez une idée de tutoriel,</br>
					Quelque chose que vous ne parvenez pas à faire,</br>
					Prenez contact avec nous !</p>
            </div>
        </div>
    </div>
</aside>



<section>
<form method="post" enctype="multipart/form-data">     
<input type="hidden" name="MAX_FILE_SIZE" value="2097152">     
<input type="file" name="nom_du_fichier">    
<input type="submit" value="Envoyer" name="Envoyer" id='sub1'>    
</form>
<input type="submit"  id="PNLE" value="PNLE_Resolution"> 
<!--<input type="submit"  id="Dynamic" value="Programmation Dynamique"> -->
</section>
<?php
$position=substr(strval($_SERVER['DOCUMENT_ROOT']),0, -9);

if(!empty($_POST['Envoyer'])) {
$chemin_destination = $position."newfile";
$name='/newinstance.txt'; 
try {
unlink($chemin_destination.$name);
} catch (Exception $e) {
    echo "run";
};
try {    
move_uploaded_file($_FILES['nom_du_fichier']['tmp_name'], $chemin_destination.$name);     
} catch (Exception $e) {
    echo "run";    
};

//mettre a jour si tu faire la même astuce pour les instances deja presents dans le repertoire instance
$chemin_srcipt=$position."src";
$command_1 = escapeshellcmd('python '.$chemin_srcipt.'/command_line.py '.$chemin_destination.$name);
$output_1 = shell_exec($command_1);
}else{
    $output_1='';
};
?> 

<section>
<div class="row centered">
<p id="demo"></p>

<p id="outputDiv">This is a test.</p>
</div>
</section>

<script type="text/javascript">

var resut =<?php echo json_encode($output_1); ?>;
var res = resut.split(",");
/* a mettre dans un javascript proprement*/
var lectu= document.getElementById("sub1");

/*var test="<svg width='120' height='120' viewBox='0 0 120 120'"
var test=test+"xmlns='http://www.w3.org/2000/svg'>"
var test=test+"<rect x='10' y='10' width='20' height='20'/>"
var test=test+"<rect x='35' y='35' width='20' height='20'/>"
var test=test+"</svg>"
document.getElementById("demo").innerHTML =test
*/

if (res.length>2){
var M1=res[0].split("{'M':")[1];
var N1=res[1].split("'N':")[1];
var toto="";//(res[7].split(":")[0]==" 'line'");

//var toto=(res[3].split(":")[0]==" 'li'");
for (i=2;i<res.length;i++){
    if (res[i].split(":")[0]==" 'line'"){
        var a1=i;
    }
    if (res[i].split(":")[0]==" 'colonne'"){
        var a2=i;
    }
    if (res[i].split(":")[0]==" 'filename'"){
        var a3=i;
    }
};
var colon='';
var lign='';
for (i=parseInt(a2);i<parseInt(a1);i++){
    var colon=colon+res[i];
}
for (i=parseInt(a1);i<parseInt(a3);i++){
    var lign=lign+res[i];
};
var lign=lign.split("'line': ")[1].split("[")[1].split("]")[0];
var colon=colon.split("'colonne': ")[1].split("[")[1].split("]")[0];

var elemt1=colon.split("'");
var colonne=[];
for (i=0;i<(elemt1.length-1)/2;i++){
    colonne.push(elemt1[2*i+1])
};
var elemt2=lign.split("'");
var ligne=[];
for (i=0;i<(elemt2.length-1)/2;i++){
    ligne.push(elemt2[2*i+1])
};



var N=parseInt(N1);
var M=parseInt(M1);
/*
var largeur=500;
var hauteur=500;
var mar=(largeur/100)-1;
var element=mar*N ;//l'espace entre les colonnes
var element1=(largeur-element)/(N+1) ;// le largeur des bloc
var element2=hauteur;

var el3=(hauteur-element)/(M+1);

var HTML ="<svg width="+largeur+"'px' "+"height="+hauteur+"'px'  color=black>";
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
*/

/*pour remplir la casup*/
var casesup=1;
for (i=0;i<colonne.length;i++){
    if (colonne[i].split(' ').length>casesup){
        var casesup=colonne[i].split(' ').length+1;
    }
};
for (i=0;i<ligne.length;i++){
    if (ligne[i].split(' ').length>casesup){
        var casesup=ligne[i].split(' ').length+1;
    }
};
var casesup=casesup+1;


var larg1=40;
var haut1=40;
var espace=2;

var HTML1="";
var k=1;
var j=1;
for (k=1;k<=N+casesup-1;k++)
{
    if (k==1){
    var positionx1=0;
}
    var j=1;
    for(j=1;j<=M+casesup-1;j++)
{
var positiony1;
var ident="'"+(k-casesup)+"_"+(j-casesup)+"'";
if (j==1){
    var positiony1=0;
}
//color
var nb='';
var text='';


function get_posi(je,maxle,taille){
    var posi=taille-maxle+je;
    return posi
};    



if ((k-casesup)<=-1 || (j-casesup)<=-1)
{
    var coloria1='gray';
    var text='';
    if (k-casesup<=-1)
    {
        if (j-casesup>=0){
            if (get_posi(k,casesup,colonne[j-casesup].split(' ').length)>=0){
            var text=colonne[j-casesup].split(' ')[get_posi(k,casesup,colonne[j-casesup].split(' ').length)];
            } else{
                var text='';   
            }            
        }
    
    }
    if(j-casesup<=-1)
    {
            if (k-casesup>=0){
                if (get_posi(j,casesup,ligne[k-casesup].split(' ').length)>=0){
                var text=ligne[k-casesup].split(' ')[get_posi(j,casesup,ligne[k-casesup].split(' ').length)];
                } else{
                    var text='';   
                }            
            }
        
    }

    //    
    //    {
    //        if(colonne[j-casesup].split(' ').length>1)
    //        {
    //            var nb='toto';
            //if (colonne[j-casesup].split(' ').length<=k){
    //         var nb=colonne[j-casesup].split(' ')[k-2];
    //        }
    /*        else
            {
                var nb='toto1';//colonne[j-casesup];//colonne[j-casesup].split(' ').length;
            };

            //if (colonne[j-casesup].split(' ').length==1){
            //    if (k-casesup==-1){
            //    var nb=colonne[j-casesup]
            //    } ;
            //    
        }
            //var text=nb;
            //var orient="writing-mode='tb' text-anchor='start'  transform='rotate(0)' ";//"transform", "translate(150,0) rotate(90)"    vertical-rl' glyph-orientation-vertical='45' alignment-baseline='central'
        
    } 
    else 
    {
        if (j-casesup<=-1)
        {
            if(k-casesup>=0) {
                var text=ligne[k-casesup];
                var orient=" text-anchor='start' alignment-baseline='central'  ";//"transform", "translate(150,0) rotate(90)"    vertical-rl' glyph-orientation-vertical='45' alignment-baseline='central'
                //var orient=0;
            } 
        }
        else
        {
            var text='';    
        }
    }*/
} 
else
{
    var coloria1='white';
    var text='';
    var orient='';
};

/*
try{
    if(orient){
        var orient=0;
    }
}catch(err)
{
    var orient=0;    
};
*/

//writing-mode='tb' glyph-orientation-vertical='90'

HTML1 += "<rect id="+ident+"y='"+positionx1+"' x='"+positiony1+"'width='"+larg1+"'height='"+haut1+"' style='fill:"+coloria1+";stroke:black;stroke-width:5;fill-opacity:1;stroke-opacity:0.9' />";
HTML1 +="<text y='"+(positionx1+espace+15)+"' x='"+(positiony1+espace+15)+"' fill='blue' "+orient+" >"+text+"</text>"
var positiony2=positiony1+larg1+espace;
var positiony1=positiony2;

//"<rect x='"+(element1*(j-1)+(mar*j))+"' y='"+(te+(marg+ts)*(k-1))+"' width='"+element1+"'height='"+marg+"' fill='blue' />"; //longeur
}

var positionx2=positionx1+haut1+espace;
var positionx1=positionx2;

};

var HTML ="<svg width="+(positiony1+10)+" height="+(positionx1+10)+"  color=gray>";
HTML+=HTML1;
HTML += "</svg>";

document.getElementById("outputDiv").innerHTML = HTML;
}

</script>

<!---<script type="text/javascript" src="../../js/script1.js">
myFunction(parseInt(M1),parseInt(N1));
</script>
-->
<!--exceution du script python sur le fichier new-->
<?php
//echo substr(strval($_SERVER['DOCUMENT_ROOT']),0, -9);
$command_2 = escapeshellcmd('python '.$chemin_srcipt.'/modele.py '.$chemin_destination.$name);
$output_2 = shell_exec($command_2);

?>

<script type="text/javascript">
var resultat1 =<?php echo json_encode(substr($output_2,102,strlen($output_2))); ?>;
/*var resultat1="Resolu\n";*/

/* creation d'une variable de tests
Changed value of parameter TimeLimit to 120.0\n   Prev: 1e+100  Min: 0.0  Max: 1e+100  Default: 1e+100\n
*/

try {
var res=resultat1.split('\n');
var tmp1=res.length;

var resultat=Array();
if (res.length>2 && res[0]=="Resolu")//verification de succes dans le message 
    {
    for (i=2;i<res.length-1;i++){
        // tmp2 le nom de la var x et tmp3 la valeur (0,-0,1)
        var tmp2=res[i].split("=")[0].split(",")
        var tmpi=tmp2[0].split("[")[1]//i 
        var tmpj=tmp2[1].split("]")[0]//j       
        var tmp3=parseInt(res[i].split("=")[1])//value 
        resultat.push(tmpi);
        resultat.push(tmpj);
        resultat.push(tmp3);
        }
    }
}
catch(err) {    
    err;
}

//function couleur

function coloriage(value){
    if (value==1){
        return "blue"
    }else{
        return "white"
    }
};    

var clic1= document.getElementById("PNLE");

clic1.addEventListener("click", function(event) {
    for (i=0;i<resultat.length/3;i++){
        tp1=resultat[i*3];
        tp2=resultat[i*3+1];
        tmps=tp1+"_"+tp2;
        var recttmp = document.getElementById(tmps);
        recttmp.style.fill=coloriage(resultat[i*3+2]);
        //bah=i*3+2;
        
    }
});

</script>

<!--  foot -->
<footer  class="bg-faded" id="contact">
    <div class="container">
		<div class="row centered">
			<h2 class="m-t-0 text-primary">MERCI</h2>
			<hr class="primary">
		</div>
        <div class="row centered">
            <div class="col-lg-6">
				<h3>Contact</h3>
				<p>
					<span class="fa fa-envelope"></span> <a href="mailto:bachiroufr2002@yahoo.fr">bachiroufr2002@yahoo.fr</a> <br>
				</p>
			</div>
			<div class="col-lg-6">
				<h3>Support</h3>
				<p>Informations.</p>
			</div>
        </div>
    </div>
</footer>	
</body>
<!--<script type="text/javascript" src="js/script.js"> </script>-->
</html>    