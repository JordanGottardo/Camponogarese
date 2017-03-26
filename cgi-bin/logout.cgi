#!/usr/bin/perl

use CGI;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );
use CGI qw(:standard);

$session = CGI::Session->load();
$input = new CGI;
  
print $input->header(-cache_control=>"no-cache, no-store, must-revalidate");

if($session->is_empty){
    print $input->header(-cache_control=>"no-cache, no-store, must-revalidate");
	print start_html(-head=>meta({-http_equiv => 'Refresh', -content=> '5; URL=../index.html'}));
	print qq{<h3>Accesso negato!<p>Attendi il reindirizzamento alla Home Page.</p>
	o clicca qui <a href="../index.html">Home</a></h3>};
	print end_html;
}

else{
  $session->delete();
	print start_html(-head=>meta({-http_equiv => 'Refresh', -content=> '5; URL=../index.html'}));
	print qq{<h3>Logut effettuato con successo!<p>Attendi il reindirizzamento alla Home Page</p>
	o clicca qui <a href="../index.html">Home</a></h3>};
	print end_html;
}
