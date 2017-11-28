<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/xhtml1-strict.dtd">
<html lang="fr">
	<head>
		<title>Projet MOGPL</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<style type="text/css"><!--
			/***********************************/
			/*  Méthode des portes coulissantes  */
			/**********************************/
			#nav {
				list-style: none ;
				margin: 0 ;
				padding: 0 ;
				overflow: hidden ;		/* Création du contexte de formatage */
				}
			#nav li {
				float: left ;
				width: 150px ;
				border: 1px solid #600 ;
				margin-right: 1px ;
				color: #fff ;
				background: #c00 ;
				}
			#nav li a {
				display: block ;
				background: #900 url(other/link.jpg) left top no-repeat ;
				color:#fff;
				font: 1em "Trebuchet MS",Arial,sans-serif ;
				line-height: 1em ;
				padding: 4px 0 ;
				text-align: center ;
				text-decoration: none ;
				}
			br {
			background: gray;
			color: white;
			padding: 10px;
			margin: 5px;
			border: thin solid black
			}
			#nav li a:hover, #nav li a:focus, #nav li a:active {
				background: #013 url(other/link.jpg) right top no-repeat ;
				text-decoration: underline ;
				}
			--></style>
			<!--[if lt IE 7]>
			<style type="text/css">
			#nav {							/* Contexte de formatage pour IE6 */
				overflow: visible ;
				height: 1% ;
				}
				p {
			background: gray;
			color: white;
			padding: 10px;
			margin: 5px;
			border: thin solid black
			}
			</style>
			<![endif]-->
	
	</head>
	<body>  <!--onload="tableCreate();"-->

		<h1>Projet MOGPL</h1>
	
	
		<div class="span6" id="form-login">
				<form class="form-horizontal well" action="import.php" method="post" name="upload_excel" enctype="multipart/form-data">
					<fieldset>
						<legend>Importer une instance</legend>
						<div class="control-group">
							<div class="control-label">
								<label>CSV/Excel File:</label>
							</div>
							<div class="controls">
								<input type="file" name="file" id="file" class="input-large">
							</div>
						</div>
						
						<div class="control-group">
							<div class="controls">
							<button type="submit" id="submit" name="Import" class="btn btn-primary button-loading" data-loading-text="Loading...">Upload</button>
							</div>
						</div>
					</fieldset>
				</form>
		</div>
	
	
	
	
	
	
	
	
	
	
	
		<ul id="nav">
			<li><a href="Index.php" title="Aller a la description du projet">Description</a></li>
			<!--<li><a href="#" title="Reponse au Question ">Questions </a></li>
			<li><a href="Implementation.php" title="Implementation ">Implementation</a></li>
			<li><a href="#" title="Lectures d'autres instances">Instances</a></li>
			<li><a href="#" title="Conclusion">Conclusion</a></li>
			<li><a href="#" title="Rapport Final">Rapport</a></li> -->
		</ul>
        <h2>GRILLE</h2>
        <h3>Data</h3>
        <!---<section>
         Nbres Machines : <input type="text" name="Nbres Machines" size="1">
         Nbres Taches : <input type="text"name="Nbres Taches" size="1">
        </section> -->
		<form action="javascript:alert('Hello there, I am being submitted');"> 
		<table>
		<td>
		<div>Tâche 1</div>
		<div>Tâche 2</div>
		<div>Tâche 3</div>
		</td>
		<td>
		<div>
		<div>...A,..B,..C</div>
		 <input type="text" name="T1A" size="1">
		<input type="text" name="T1B" size="1">
		<input type="text" name="T1C" size="1"> </div>
		<div>
		<input type="text" name="T2A" size="1">
		<input type="text" name="T2B" size="1">
		<input type="text" name="T2C" size="1"> </div>		
		<div>
		<input type="text" name="T3A" size="1">
		<input type="text" name="T3B" size="1">
		<input type="text" name="T3C" size="1"> </div>
		</td>
		</table>
		<!--<input type="button" id="createID" value="Saisir les durées" onclick="tableCreate();" /> -->
	<br>ABDDSD</br>	
		<!--

        <h3>l’algorithme de Johnson </h3>
		<button type="submit">Johnson</button>
		</form> 

		<button id="btnTable">add empty table (invisible)</button>
		<button id="btnTableContentsAdd">add table contents</button>
		<button id="btnTableContentsRemove">remove table contents</button>
		<button id="btnTableBlueBorder">add blue table border</button>
		<button id="btnTableRedBorder">add red table border</button>
		<div id="container"></div>
		<div id="test"></div>  -->
		<!---<script>
		document.getElementById("myBtn").addEventListener("click", function(){
		alert("test");
		document.getElementById("demo").innerHTML = "Hello World";
		});
		</script>
      
	<h3>Méthode arboresante </h3>  
        <section>
		<button id="myBtn">Try it</button>
		<p id="demo"></p>
		<script src="js/query.js"> </script>	
        </section>     
		-->
 
	</body>
</html>
