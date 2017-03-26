#!/usr/bin/perl
print "Content-Type: text/html\n\n";

use CGI;
use XML::LibXML;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );
use strict;

my $session = CGI::Session->load();

#Permesso negato.
if($session->is_expired or $session->is_empty)
{
print <<ENDHTML;
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
	  <title>Error Sign In</title>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	  <meta http-equiv="Content-Script-Type" content="text/javascript" />
	  <meta name="title" content="Error Login page - Associazione calcistica dilettantistica Camponogarese" />
	  <meta name="description" content="Pagina error login A.C.D. Camponogarese" />
	  <meta name="keywords" content="Camponogarese,login" />
	  <meta name="language" content="italian it" />
	  <meta name="author" content="Daniel De Gaspari, Davide Santimaria, Emanuele Carraro, Jordan Gottardo" />
	  <link rel="stylesheet" type="text/css" href="../css/style.css" media="screen and (min-width: 650px)" />
	  <link rel="stylesheet" type="text/css" href="../css/print.css" media="print" />
	  <link rel="stylesheet" type="text/css" href="../css/small-devices.css" media="screen and (max-width: 650px)" />
	  <link rel="icon" href="../immagini/logo.png" type="image/png" />
	</head>
<body>
	<div id="header">
		<span id="logo"></span>
		<h1><abbr title="Associazione calcistica dilettantistica">A.C.D.</abbr> Camponogarese</h1>
	</div>
  <div id="path"><p>Ti trovi in: <span xml:lang="en"><a href="../index.html">Home</a></span>&gt Error Login</p></div>
  <div id="fail"> <img src="../immagini/failLog.jpg" ></img></div>
	<div id="section">
	<h1>La sessione e' scaduta o non hai effettuato l'accesso!</h1>
	<p>Effettuare nuovamente il login.</p>
		<form action="accesso.cgi" method="post">
			<fieldset>
				<legend>Login amministratore</legend>
				<label for="username">Username</label>
				<input class="casella_input" name="username" id="user" value="user" maxlength="20" />
				<label for="password">Password</label>
				<input class="casella_input" type="password" name="pwd" id="password" value="pwd" maxlength="20" />
				<input type="submit" value="Accedi"></input>
			</fieldset>
		</form>
</div>
</body>
</html>

ENDHTML
}
else { #Accesso consentito;

#input
my $input= new CGI;

#Se arrivo dalla pagina di disambiguazione;
if ($input->param("aggiungiPersonale")) {

print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
	  <title>Inserimento personale</title>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	  <meta http-equiv="Content-Script-Type" content="text/javascript" />
	  <meta name="title" content="Inserimento personale - Associazione calcistica dilettantistica Camponogarese" />
	  <meta name="description" content="Pagina inserimento personale A.C.D. Camponogarese" />
	  <meta name="keywords" content="Camponogarese,personale" />
	  <meta name="language" content="italian it" />
	  <meta name="author" content="Daniel De Gaspari, Davide Santimaria, Emanuele Carraro, Jordan Gottardo" />
	  <link rel="stylesheet" type="text/css" href="../css/style.css" media="screen and (min-width: 650px)" />
	  <link rel="stylesheet" type="text/css" href="../css/print.css" media="print" />
	  <link rel="stylesheet" type="text/css" href="../css/small-devices.css" media="screen and (max-width: 650px)" />
	  <link rel="icon" href="../immagini/logo.png" type="image/png" />
		<script type="text/javascript" src="../script/adminScript.js"></script>
	 </head>
	 <body onload="caricamento(form_personale); hideRuolo(); hideDati();">
	 <div id="header">
		<span id="logo"></span>
		<h1><abbr title="Associazione calcistica dilettantistica">A.C.D.</abbr> Camponogarese</h1>
	</div>
		<div id="path"><p>Ti trovi in: <span xml:lang="en"><a href="log.cgi">Control Panel</a></span>&gt Inserimento personale</p></div>
 	<div id="menu">
	<ul>
			<li> 
				<form action="log.cgi" method="post">
				<input type="submit" value="Control panel" name="Accedi"></input>
				</form>
			</li>
			<li> 
				<form action="aggiungiPartita.cgi" method="post">
				<input type="submit" value="Aggiungi partita" name="aggiungiPartita"></input>
				</form>
			</li>
			<li> 
				<form action="logout.cgi" method="post">
				<input type="submit" value="logout" name="Logout"></input>
				</form>
			</li>
			
		</ul>
	</div>
	<div id="section">
	<form id="formPersonale" action="aggiungiPersonale.cgi" method="post" class="styleForm">
			<fieldset>
				<legend>Aggiungi personale</legend>
				<fieldset>
					<legend>Scegli grado societario</legend>
					<label for="amministratore">Amministratore</label>
					<input type="radio" name="grado" id="amministratore" value="amministratore" onclick="cbCheck();"/>
					 <label for="dipendente">Dipendente</label>
					 <input type="radio" name="grado" id="dipendente" value="dipendente" onclick="cbCheck();" />
				</fieldset>
				<div id="sceltaRuolo">
					<fieldset>
						<legend>Scegli ruolo</legend>
						<div id="mangerHide">
							<label for="manager">Manager</label>
							<input type="radio" name="ruolo" id="manager" value="manager" onclick="cbCheck1();" />
						</div>
						<div id="allenatHide">	
							<label for="allenatori">Allenatori</label>
							<input type="radio" name="ruolo" id="allenatori" value="allenatori" onclick="cbCheck1();"/>
						</div>
					</fieldset>
				</div>
				<div id="listaDati">
					<fieldset>
						 <legend>Dati</legend>
						 <label for="nome">Nome</label>
						 <span><input type="text" id="nome" name="nome" maxlength="20" /></span>
						 <br />
						 <label for="cognome">Cognome</label>
						 <span><input type="text"  id="cognome" name="cognome" maxlength="20" /></span>
						 <br />
						 <label for="data">Data</label>
						 <span><input type="text" id="data" name="data" maxlength="10" /></span>
						 <br />
						 <label for="telefono">Telefono</label>
						 <span><input type="telefono" id="telefono" name="telefono" maxlength="20" /></span>
						 <br />
						 <input type="submit" value="Invia">
					</fieldset>
				
			</div>
			</fieldset>
			
	 </form>
	 </div>
	</body>
</html>
EOF

}

else #Ho provato ad inserire un dato;
{

my $grado=$input->param("grado");
$grado =~ s/[<>&]//g;
chomp($grado);

my $ruolo=$input->param("ruolo");
$ruolo =~ s/[<>&]//g;
chomp($ruolo);

my $nome=$input->param("nome");
$nome =~ s/[<>&]//g;

my $cognome=$input->param("cognome");
$cognome =~ s/[<>&]//g;

my $data=$input->param("data");
$data =~ s[<>&]//g;

my $telefono=$input->param("telefono");
$telefono =~ s/[<>&]//g;


my $filepath="../public_html/organizzazione.xml";

my $errore=0;
my $mismatch;
my $errNome;
my $errCognome;
my $errData;
my $errTelefono;

#Controllo ruolo-grado;
if  (( $grado eq 'amministratore' && $ruolo eq 'allenatori') || ($grado eq 'dipendente' && $ruolo eq 'manager')) {
	$errore=1;
	$mismatch="Mismatch grado-ruolo";
}

#Controllo dati letti
#controllo coerenza dati letti
if ($nome!~/^[A-Z][a-z]+$/ || length($nome)>100 || $nome eq "Inserire nome"){
	$errore=1;
	$errNome="Inserire un nome lungo almeno 2, prima lettera maiuscola";
}

if ($cognome!~/^[A-Z][a-z]+(\s([A-Z][a-z]+))?$/ || length($cognome)>100 || $cognome eq "Inserire cognome"){
	$errore=1;
	$errCognome="Inserire un cognome lungo almeno 2, prima lettera maiuscola (cognomi con spazio consentiti)";
}

#modificare: aggiungere controllo per il valore di default dato da JavaScript
if ($data!~/^([0-3]{1}[0-9]{1}\/[0,1]{1}[0-9]{1}\/[0-9]{4})|([0-3]{1}[0-9]{1}\-[0,1]{1}[0-9]{1}\-[0-9]{4})$/ || $data eq "Inserire data") {
	$errore=1;
	$errData="Inserire data, formati consentiti DD/MM/AAAA oppure DD-MM-AAAA";
}

#modificare: aggiungere controllo per il valore di default dato da JavaScript (e aggiungere trattino sul numero
#controllare se funziona  il trattino dopo l'aggiunta dell'escaping
if ( $telefono!~/^(0?[0-9]{2,3}\-[0-9]+)|(0?[0-9]{2,3}[0-9]+)$/ || length($telefono)>15 || $telefono eq "Inserire telefono") {
	$errore=1;
	$errTelefono="Inserire numero di telefono valido, formati consentiti 111-111111 oppure 111111111";
}


#aggiungere lock?
if ($errore==0)
{
	#creo l'oggetto parser;
	my $parser=XML::LibXML->new();

	#apertura file + lettura input
	my $doc=$parser->parse_file($filepath);

	#estrazione elemento radice;
	my $radice=$doc->getDocumentElement;

	#definisco il nuovo elemento da inserire;
	my $elemento =
	"
		<$ruolo>
			<nome>$nome</nome>
			<cognome>$cognome</cognome>
			<dataNascita>$data</dataNascita>
			<telefono>$telefono</telefono>
		</$ruolo>
	";

	#creo un nuovo nodo + controllo;
	my $fragment = $parser->parse_balanced_chunk($elemento);

	#se è un'admin, memorizzo tra gli amministratori
	if ($grado eq 'amministratore')
	{
		if ($ruolo eq 'manager')
		{
			my @manager = $radice->getElementsByTagName('amministratori');
			$manager[0]->appendChild($fragment);
		}
	}

	if ($grado eq 'dipendente')
	{
		if ($ruolo eq 'allenatori')
		{
			my @allenatori = $radice->getElementsByTagName('dipendenti');
			$allenatori[0]->appendChild($fragment);
		}
	}



	#apro il file su cui serializzare
	open(OUT, ">$filepath") or die ("Errore nel salvataggio del file");
	#scrivo sul file
	print OUT $doc->toString;
	#chiudo il file
	close(OUT) or die("Errore nella chiusura file");



	#Ristampo la form
	print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
	  <title>Inserimento personale</title>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	  <meta http-equiv="Content-Script-Type" content="text/javascript" />
	  <meta name="title" content="Inserimento personale - Associazione calcistica dilettantistica Camponogarese" />
	  <meta name="description" content="Pagina inserimento personale A.C.D. Camponogarese" />
	  <meta name="keywords" content="Camponogarese,personale" />
	  <meta name="language" content="italian it" />
	  <meta name="author" content="Daniel De Gaspari, Davide Santimaria, Emanuele Carraro, Jordan Gottardo" />
	  <link rel="stylesheet" type="text/css" href="../css/style.css" media="screen" />
	  <link rel="stylesheet" type="text/css" href="../css/print.css" media="print" />
	  <link rel="icon" href="../immagini/logo.png" type="image/png" />
	 <script type="text/javascript" src="../script/adminScript.js"></script>
	 </head>
	 <body onload="caricamento(form_personale); hideRuolo(); hideDati();">
	 <div id="header">
		<span id="logo"></span>
		<h1><abbr title="Associazione calcistica dilettantistica">A.C.D.</abbr> Camponogarese</h1>
	</div>
		<div id="path"><p>Ti trovi in: <span xml:lang="en"><a href="log.cgi">Control Panel</a></span>&gt Inserimento personale</p></div>
 	<div id="menu">
	<ul>
			<li> 
				<form action="log.cgi" method="post">
				<input type="submit" value="Control panel" name="Accedi"></input>
				</form>
			</li>
			<li> 
				<form action="aggiungiPartita.cgi" method="post">
				<input type="submit" value="Aggiungi partita" name="aggiungiPartita"></input>
				</form>
			</li>
			<li> 
				<form action="logout.cgi" method="post">
				<input type="submit" value="logout" name="Logout"></input>
				</form>
			</li>
			
		</ul>
	</div>
	<div id=section>
		<div id="successo">Inserimento avvenuto con successo!</div>
		<form id="formPersonale" action="aggiungiPersonale.cgi" method="post" class = "styleForm">
			<fieldset>
				<legend>Aggiungi personale</legend>
				<fieldset>
					<legend>Scegli grado societario</legend>
					<label for="amministratore">Amministratore</label>
					<input type="radio" name="grado" id="amministratore" value="amministratore" onclick="cbCheck();"/>
					 <label for="dipendente">Dipendente</label>
					 <input type="radio" name="grado" id="dipendente" value="dipendente" onclick="cbCheck();" />
				</fieldset>
				<div id="sceltaRuolo">
					<fieldset>
						<legend>Scegli ruolo</legend>
						<div id="mangerHide">
							<label for="manager">Manager</label>
							<input type="radio" name="ruolo" id="manager" value="manager" onclick="cbCheck1();" />
						</div>
						<div id="allenatHide">	
							<label for="allenatori">Allenatori</label>
							<input type="radio" name="ruolo" id="allenatori" value="allenatori" onclick="cbCheck1();"/>
						</div>
					</fieldset>
				</div>
				<div id="listaDati">
					<fieldset>
						 <legend>Dati</legend>
						 <label for="nome">Nome</label>
						 <span><input type="text" id="nome" name="nome" maxlength="20" /></span>
						 <br />
						 <label for="cognome">Cognome</label>
						 <span><input type="text"  id="cognome" name="cognome" maxlength="20" /></span>
						 <br />
						 <label for="data">Data</label>
						 <span><input type="text" id="data" name="data" maxlength="10" /></span>
						 <br />
						 <label for="telefono">Telefono</label>
						 <span><input type="telefono" id="telefono" name="telefono" maxlength="20" /></span>
						 <br />
						 <input type="submit" value="Invia">
					</fieldset>

				</div>
			</fieldset>
			
	 </form>
	 </div>
	</body>
</html>
EOF
}
else #Stampa la form con gli errori (wizard javascript disabilitato volutamente)
{
	print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
	  <title>Inserimento personale</title>
	  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	  <meta http-equiv="Content-Script-Type" content="text/javascript" />
	  <meta name="title" content="Inserimento personale - Associazione calcistica dilettantistica Camponogarese" />
	  <meta name="description" content="Pagina inserimento personale A.C.D. Camponogarese" />
	  <meta name="keywords" content="Camponogarese,personale" />
	  <meta name="language" content="italian it" />
	  <meta name="author" content="Daniel De Gaspari, Davide Santimaria, Emanuele Carraro, Jordan Gottardo" />
	  <link rel="stylesheet" type="text/css" href="../css/style.css" media="screen and (min-width: 650px)" />
	  <link rel="stylesheet" type="text/css" href="../css/print.css" media="print" />
	  <link rel="stylesheet" type="text/css" href="../css/small-devices.css" media="screen and (max-width: 650px)" />
	  <link rel="icon" href="../immagini/logo.png" type="image/png" />
	 <script type="text/javascript" src="../script/adminScript.js"></script>
	 </head>
	 <body onload="caricamento(form_personale);">
	<div id="header">
		<span id="logo"></span>
		<h1><abbr title="Associazione calcistica dilettantistica">A.C.D.</abbr> Camponogarese</h1>
	</div>
		<div id="path"><p>Ti trovi in: <span xml:lang="en"><a href="log.cgi">Control Panel</a></span>&gt Inserimento personale</p></div>
 	<div id="menu">
	<ul>
			<li> 
				<form action="log.cgi" method="post">
				<input type="submit" value="Control panel" name="Accedi"></input>
				</form>
			</li>
			<li> 
				<form action="aggiungiPartita.cgi" method="post">
				<input type="submit" value="Aggiungi partita" name="aggiungiPartita"></input>
				</form>
			</li>
			<li> 
				<form action="logout.cgi" method="post">
				<input type="submit" value="logout" name="Logout"></input>
				</form>
			</li>
			
		</ul>
	</div>
	 <div id="section">
	 <ul>
EOF
	if (length($mismatch)>0)
	{
		print "<li>$mismatch</li>";
	}
	
	if (length($errNome)>0)
	{
		print "<li>$errNome</li>";
	}
	if (length($errCognome)>0)
	{
		print "<li>$errCognome</li>";
	}
	if (length($errData)>0)
	{
		print "<li>$errData</li>";
	}
	if (length($errTelefono)>0)
	{
		print  "<li>$errTelefono</li>";
	}

	print <<EOF;
	 </ul>
	
	 <form id="formPersonale" action="aggiungiPersonale.cgi" method="post" class="styleForm">
	 <fieldset>
	 <legend>Aggiungi personale</legend>
EOF
	if ($grado eq 'amministratore')
	{
		print <<EOF;
		 <fieldset>
		 <legend>Scegli grado societario</legend>
		 <label for="amministratore">Amministratore</label>
		 <input type="radio" name="grado" id="amministratore" value="amministratore" checked="true" />
		 <label for="dipendente">Dipendente</label>
		 <input type="radio" name="grado" id="dipendente" value="dipendente" />
		 </fieldset>
EOF
	}
	
	if ($grado eq 'dipendente')
	{
		print <<EOF;
		 <fieldset>
		 <legend>Scegli grado societario</legend>
		 <label for="amministratore">Amministratore</label>
		 <input type="radio" name="grado" id="amministratore" value="amministratore" />
		 <label for="dipendente">Dipendente</label>
		 <input type="radio" name="grado" id="dipendente" value="dipendente" checked="true" />
		 </fieldset>
EOF
	}
	
		if ($ruolo eq 'manager')
	{
		print <<EOF;
		 <fieldset>
		 <legend>Scegli ruolo</legend>
		 <label for="manager">Manager</label>
		 <input type="radio" name="ruolo" id="manager" value="manager"  checked="true" />
		 <label for="allenatori">allenatori</label>
		 <input type="radio" name="ruolo" id="allenatori" value="allenatori" />
		 </fieldset>
EOF
	}
	
	if ($ruolo eq 'allenatori')
	{
		print <<EOF;
		 <fieldset>
		 <legend>Scegli ruolo</legend>
		 <label for="manager">Manager</label>
		 <input type="radio" name="ruolo" id="manager" value="manager"  />
		 <label for="allenatori">allenatori</label>
		 <input type="radio" name="ruolo" id="allenatori" value="allenatori" checked="true" />
		 </fieldset>
EOF
	}
	print <<EOF;
	<div id="listaDati">
	 <fieldset>
	 <legend>Dati</legend>
	 <label for="nome">Nome</label>
	 <span><input type="text" id="nome" name="nome" maxlength="20" value="$nome" /></span>
	 <br />
	 <label for="cognome">Cognome</label>
	 <span><input type="text" id="cognome" name="cognome" maxlength="20" value="$cognome" /></span>
	 <br />
	 <label for="data">Data</label>
	 <span><input type="text" id="data" name="data" maxlength="10" value="$data" /></span>
	 <br />
	 <label for="telefono">Telefono</label>
	 <span><input type="telefono" id="telefono" name="telefono" maxlength="10" value="$telefono" /></span>
	 <br />
	 </fieldset>
	 <input type="submit" value="Invia">
	 </div>
	 </fieldset>
	 
	 </form>
	 </div>
	 </body>
	 </html>
EOF
}
}
}
