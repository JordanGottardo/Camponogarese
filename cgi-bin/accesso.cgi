#!/usr/bin/perl

use CGI;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session;




 #
 # Now the variable $form has your input data.
 # Create your associative array.
 #

#---lettura dei parametri
    local ($buffer, @pairs, $pair, $name, $value, %FORM);
    # Read in text
    $ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

    # Split information into name/value pairs
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs)
    {
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%(..)/pack("C", hex($1))/eg;
	$FORM{$name} = $value;
    }
    $user = $FORM{username};
    $pwd  = $FORM{pwd};


		
#---se i campi sono corretti
    if($user eq "user" and $pwd eq "pwd") {
        
        my $session = new CGI::Session();
#modificare: session->param("user", $user);
#print $session->header(-type => "text/plain", -charset => "utf-8", -location=>"log.cgi");
    print $session->header(-location=>"log.cgi");
    
    #print $session->header("Redirect: log.cgi");
    }
else{     
 #---apertura pagina-----

print "Content-type:text/html\r\n\r\n";
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

  <div id="path">
    <p>Ti trovi in: <span xml:lang="en"><a href="../index.html">Home</a></span>&gt Error Login</p>
  </div>
ENDHTML
#-----tutte le condizioni di errato accesso----
print <<ENDHTML;
 <div id="fail"> <img src="../immagini/failLog.jpg" ></div>
 <div id="section">
	<h1>Login Fallito!</h1>
ENDHTML
	
#----- campo username errato------
if($user ne "user" and $pwd eq "pwd" and length $user ne "0") {	
print <<ENDHTML;
	<p>Username errato.</p>
	<p>Ricompila i campi d'accesso.</p>
ENDHTML
} 

#----- campo password errato------
if($user eq "user" and $pwd ne "pwd" and length $pwd ne "0") {	
print <<ENDHTML;
	<p>Password errata.</p>
	<p>Ricompila i campi d'accesso.</p>
ENDHTML
}  

#----- entrambi i campi user errati------
if($user ne "user" and $pwd ne "pwd" and length $user ne "0" and length $pwd ne "0") {	
print <<ENDHTML;
	<p>Username e Password errati.</p>
	<p>Ricompila i campi d'accesso.</p>
ENDHTML
} 

#------se i campi sono vuoti------	
if (length $user eq '0' or length $pwd eq '0') {	  
print <<ENDHTML;
<p>Entambi i campi NON devono esser vuoti.</p>
<p>Ricompila i campi d'accesso.</p>
ENDHTML
	} 
}
	      
#---chiusura pagina-----

	
print <<ENDHTML;
		<form action="accesso.cgi" method="post">
			<fieldset>
				<legend>Login amministratore</legend>
				<label for="username">Username</label>
				<input class="casella_input" name="username" id="user" maxlength="20" />
				<label for="password">Password</label>
				<input class="casella_input" type="password" name="pwd" id="password" maxlength="20" />
				<input type="submit" value="Accedi"></input>
			</fieldset>
		</form>
</div>
</body>
</html>

ENDHTML
	      
