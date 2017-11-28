<!DOCTYPE html>
<html lang="fr">
    <head>
    <meta charset="utf-8">
    <title>PROJET</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Traore projet">
    <link rel="shortcut icon" href="assets/ico/favicon.ico">

    <link href='css/1italic.css' rel='stylesheet' type='text/css'>
	<!-- Not use now, see style.css for h1, h2...-->
    <!-- <link href='http://fonts.googleapis.com/css?family=Raleway:400,300,700' rel='stylesheet' type='text/css'> -->

    <link rel="stylesheet" href="css/bootstrap.min.css" integrity="sha384-AysaV+vQoT3kOAXZkl02PThvDr8HYKPZhNT5h/CXfBThSRXQ6jW5DO2ekP5ViFdi" crossorigin="anonymous">

    <link rel="stylesheet" href="css/awesome.css">
    <link rel="stylesheet" href="css/css_styles.css" />
  </head>
  
  	
  <body>
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
                    <a class="nav-link page-scroll" href="index.php">Data inside</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link page-scroll" href="index.php">Data outside</a>
                </li>
            </ul>
			<ul class="nav navbar-nav float-xs-right">
                <li class="nav-item">
                    <a class="nav-link page-scroll" data-toggle="modal" title="Information sur le site" href="#aboutModal">About</a>
                </li>
			</ul>
        </div>
    </div>
</nav>

<header id="home">
	<div class="header-content">
		<div class="inner">
			<h1>MOGPL</h1>
			<p>Projet </p>
			<a href="#last" style="color:white;">
				<span class="fa fa-chevron-circle-down fa-5x" aria-hidden="true"></span>
			</a>
		</div>
	</div>
</header>
<!---->
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


<section id="last">
	<div class="container">
		<div class="row centered">
			<h2 class="m-t-0 text-primary">Selection de l'instance</h2>
			<hr class="primary">
		</div>
		
		<div id="carousel-last" class="carousel slide" data-ride="carousel">
			<ol class="carousel-indicators">
				<li data-target="#carousel-last" data-slide-to="0" class="active"></li>
				<li data-target="#carousel-last" data-slide-to="1"></li>
				<li data-target="#carousel-last" data-slide-to="2"></li>
			</ol>
			<div class="carousel-inner" role="listbox">
				<div class="carousel-item active">
					<img class="mx-auto" src="d3js/migration-v4.jpg" alt="Instance 01" style="height:300px; display: block;">
					<div class="carousel-caption">
						<h1>Choix de l'instance</h1>
						<p>faite defiler les numeros avec les fleches pour choisier</p>
						<a class="btn btn-lg btn-primary" href="test2.php?page=migration-v4" role="button">Validé</a>
                        <?php 
                    	$command = escapeshellcmd('python /home/traoreb/Bureau/MOGPLPROJET/code/src/command_line.py /home/traoreb/Bureau/MOGPLPROJET/code/instances/0.txt');
	                    $output = shell_exec($command);
                        ?> 	
                        <script type="text/javascript">
                        var foo =<?php echo json_encode($output); ?>;
                        
                        </script>
                    </div>
				</div>
				<div class="carousel-item mx-auto">
					<img class="mx-auto" src="playing/la-crue-du-siecle.jpg" alt="Simulation de crue à Paris" style="height:300px; display: block;">
					<div class="carousel-caption">
						<h1>Simulation de crue à Paris</h1>
						<p>Google Elevation API, Leaflet et D3JS</p>
						<a class="btn btn-lg btn-primary" href="index.php?page=la-crue-du-siecle" role="button">Voir le tutoriel</a>
					</div>
				</div>
				<div class="carousel-item mx-auto">
					<img class="mx-auto" src="d3js/map-world-temperature.jpg" alt="Map - Projection orthographique" style="height:300px; display: block;">
					<div class="carousel-caption">
						<h1>Map - Projection orthographique</h1>
						<p>Projection orthographique et rotation avec la souris ou le doigt</p>
						<a class="btn btn-lg btn-primary" href="index.php?page=map-world-temperature" role="button">Voir le tutoriel</a>
					</div>
				</div>
			</div>
			<a class="left carousel-control" href="#carousel-last" role="button" data-slide="prev">
				<span class="icon-prev" aria-hidden="true"></span>
				<span class="sr-only">Previous</span>
			</a>
			<a class="right carousel-control" href="#carousel-last" role="button" data-slide="next">
				<span class="icon-next" aria-hidden="true"></span>
				<span class="sr-only">Next</span>
			</a>
		</div>
	</div>
</section>

<section id="d3js">
	<div class="container">
		<div class="row centered">
			<h2 class="m-t-0 text-primary">La grille</h2>
			<hr class="primary">
			<p class="lead">
				ci -joint la grille de l'instance que vous avez selectionnez 
			</p>
		</div>
		
        <div class="card-group">
            <div class="card">
				<a href="index.php?page=firststep">
				</a>
                <div class="card-block">
                    <b><h4 class="card-title">Raisonnement par programmation dynamique <i style="color:#dd514c;">1</i></h4></b>
                    <p class="card-text">Un raisonnement simple .</p>
                </div>
            </div>
            <div  class="card">
				<a href="index.php?page=presentation">
				</a>
				<div class="card-block">
					<b><h4 class="card-title">Présentation</h4></b>
					<p class="card-text">Un problème de tomographie discrète </p>
				</div>
			</div>
            <div class="card">
				<a href="index.php?page=map-firststep">
				</a>
                <div class="card-block">
                    <b><h4 class="card-title">La PLNE à la rescousse <i style="color:#dd514c;">2</i></h4></b>
                    <p class="card-text">Pour résoudre les grilles plus complexes, nous allons faire appel à la Pogrammation Linéaire en
Nombres Entiers (PLNE).</p>
                    
                </div>
            </div>
        </div>
		
        <div class="card-group">
            <div class="card">
				<a href="index.php?page=map-population">
				</a>
                <div class="card-block">
                    <b><h4 class="card-title">Carte choroplèthe <i style="color:#dd514c;">V4</i></h4></b>
                    <p class="card-text">Comment créer une carte dont les régions sont colorées en fonction de données statistiques et ajouter une échelle. Comment utiliser un jeu de couleurs pertinant et le rendre dynamique</p>
                </div>
            </div>
            <div class="card">
				<a href="index.php?page=map-optimization">
                <p id="outputDiv">This is a test.</p>                
                </a>
            </div>
            <div class="card">
				<a href="index.php?page=barchart">
				</a>
                <div class="card-block">
					<b><h4 class="card-title">Histogramme (Bar Chart) <i style="color:#dd514c;">V4</i></h4></b>
                    <p class="card-text">Comment réaliser un histogramme et lui associer une légende</p>
                    
                </div>
            </div>
        </div>
    </div>
</section>


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
					<span class="fa fa-twitter"></span> <a href="https://twitter.com/" target="_blank">@bass</a> <br>
				</p>
			</div>
			<div class="col-lg-6">
				<h3>Support</h3>
				<p>Le contenu de ce site est entièrement gratuit et libre de droit.</p>
			</div>
        </div>
    </div>
</footer>	
</body>
<script type="text/javascript" src="js/script1.js">	</script>
