var resultat1="Resolu\n";
var tmp1=resultat1+"Time\n";
var tmp2=tmp1+"x[0,0]=1.0\n";
var tmp1=tmp2+"x[1,0]=-0.0\n";
var tmp2=tmp1+"x[0,1]=1.0\n";
var tmp1=tmp2+"x[1,1]=1.0\n";
var tmp2=tmp1+"x[0,2]=-0.0\n";
var tmp1=tmp2+"x[1,2]=1.0\n";
var tmp2=tmp1+"x[0,3]=0.0\n";
var tmp1=tmp2+"x[1,3]=-0.0\n";
//var tmp1=tmp2+"x[1,4]=-0.0\n";
var resultat1=tmp1

/* creation d'une variable de tests*/

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

//function couleur

function coloriage(value){
    if (value==1){
        return "red"
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

//alert(resultat);