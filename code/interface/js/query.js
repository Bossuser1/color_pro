/*document.addEventListener("click", myFunction);
document.addEventListener("click", someOtherFunction);

function myFunction() {
alert ("Hello World!")
}

function someOtherFunction() {
    	alert ("This function was also executed!")
}

var pElems = document.getElementsByTagName("p");
for ( var i = 0; i < pElems.length; i++) {
	pElems[i].addEventListener("mouseover", handleMouseOver);
	pElems[i].addEventListener("mouseout", handleMouseOut);
}

document.getElementById("duree").onclick = function() {
	document.getElementById("block2").removeEventListener("mouseout",handleMouseOut);
	};

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
*/
/*
function modifieTexte() {
	var t2 = document.getElementById("bouton");
	t2.firstChild.nodeValue = "Valider";    
  };
  // fonction pour ajouter un écouteur à t

function load() {
	createTable() 
	var el = document.getElementById("bouton"); 
	el.addEventListener("click", modifieTexte, false); 
  }; 


document.getElementById("btnTable").addEventListener("click", function(){
	var basicTable = '<table id="table"></table>';
  document.getElementById('container').innerHTML = basicTable;
});

// add contents to the table, ADD instead of REPLACE by using the += operator
document.getElementById("btnTableContentsAdd").addEventListener("click", function(){
	var tableContents = '<tr><td>Hello world!</td></tr>';
  document.getElementById('table').innerHTML += tableContents;
});

  function createTable()
  {
		  var obj = [1,2,3,4,5];
		  var tbl = document.createElement('table');
		  var row = tbl.insertRow(0);
		  var cell = row.insertCell(0);
		  cell.innerHTML = "Code";
		  cell = row.insertCell(1);
		  cell.innerHTML = "Size";
		  cell = row.insertCell(2);
		  cell.innerHTML = "Description";
		  cell = row.insertCell(3);
		  cell.innerHTML = "Type";
		  cell = row.insertCell(4);
		  cell.innerHTML = "Price";
		  cell.style.textAlign = "right";
		  for (var i = 0; i < obj.length; i++) {
			  row = tbl.insertRow(i + 1);
			  row.className = "results_row";
			  cell = row.insertCell(0);
			  cell.innerHTML = obj[i].Code;
			  cell = row.insertCell(1);
			  cell.innerHTML = obj[i].Size;
			  cell = row.insertCell(2);
			  cell.innerHTML = obj[i].Description;
			  cell = row.insertCell(3);
			  cell.innerHTML = obj[i].Type;
			  cell = row.insertCell(4);
			  cell.innerHTML = parseFloat(obj[i].Price).toFixed(2);
			  cell.style.textAlign = "right";
			  row.addEventListener("click", (function(){ alert('click'); }));
		  }
		  return tbl;
  }

document.getElementById('test').appendChild(createTable());
*/

function gettest(){
	alert("test");
};

function makeForm(){
	var mypara=document.getElementById("paraID");
	myform=document.createElement("form");
	mypara.appendChild(myform);
	alert(mypara);
};


function tableCreate() {
	alert();
    var body = document.getElementsByTagName('body')[0];
    var tbl = document.createElement('table');
    tbl.style.width = '100%';
    tbl.setAttribute('border', '3');
    var tbdy = document.createElement('tbody');
    for (var i = 0; i < 10; i++) {
        var tr = document.createElement('tr');
        for (var j = 0; j < 5; j++) {
            if (i == 2 && j == 1) {
                break
            } else {
                var td = document.createElement('td');
                td.appendChild(document.createTextNode('\u0020'))
                i == 1 && j == 1 ? td.setAttribute('rowSpan', '2') : null;
                tr.appendChild(td)
            }
        }
        tbdy.appendChild(tr);
    }
    tbl.appendChild(tbdy);
    body.appendChild(tbl);
};


document.getElementById("myBtn").addEventListener("click", function(){
    document.getElementById("demo").innerHTML = "Hello World";
});