<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:x="http://www.camponogarese.it" exclude-result-prefixes="x">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'
doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"
doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" /> 

<xsl:template match="/">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
<head>
	<title>Risultati partite - Squadra Calcio Camponogarese</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="title" content="Calendario partite - Camponogarese Associazione calcistica dilettantistica" />
	<meta name="description" content="Calendario di ogni partita per categoria dell'associazione sportiva Camponogarese" />
	<!-- Aggiungere categorie? es: pulcini camponogara, esordienti camponogara... -->
	<meta name="keywords" content="Camponogarese, associazione, sport, calcio, squadra, piccoli amici camponogara, esordienti camponogara, giovanissimi camponogara, calendario, partite" />
	<meta name="language" content="italian it" />
	<!-- Come mettere più author? 1 meta con più nomi, separati da virgola, o più meta (valida)-->
	<meta name="author" content="Daniel De Gaspari, Davide Santimaria, Emanuele Carraro, Jordan Gottardo" />
	<link rel="stylesheet" type="text/css" href="css/style.css" media="screen and (min-width: 650px)" />
	<link rel="stylesheet" type="text/css" href="css/print.css" media="print" />
	<link rel="stylesheet" type="text/css" href="css/small-devices.css" media="screen and (max-width: 650px)" />
	<link rel="icon" href="immagini/logo.png" type="image/png" />
</head>

<body>
	<div id="header">
		
		<span id="logo"></span>

		<!-- link "nascosto" che porta direttamente al contenuto della pagina -->
			<a href="#contenutopagina" class="nascosto">Vai al contenuto della pagina</a>

		<h1><abbr title="Associazione calcistica dilettantistica">A.C.D.</abbr> Camponogarese</h1>
	</div>

	<div id="path">
		<p>Ti trovi in: <a href="index.html" xml:lang="en">Home</a> &gt;&gt; Risultati partite</p>
	</div>

	<!-- menu laterale sotto al logo, orientamento verticale -->
	<div id="menu">
	<!-- link "nascosto" del menù -->
		<a name="menuNascosto" class="nascosto">Menù</a>
		<ul>
			<li><a href="index.html"><span xml:lang="en">Home</span></a></li>
			<li><a href="organizzazione.xml">Chi siamo</a></li>
			<li><a href="squadre.html">Squadre</a></li>
			<li><a href="orario.html">Orari</a></li>
			<li id="CurrentLink">Risultati partite</li>
			<li><a href="photogallery.html"> <span xml:lang="en">Photo Gallery </span></a></li>
			<li><a href="dovesiamo.html">Dove siamo</a></li>
			
		</ul>
	</div>

	<div id="section">
	<h1 class="titolo">Risultati delle partite</h1>
<!-- Calendario PICCOLI AMICI -->
			<div class="linkAncore">
		<!--link ancore per i risutati delle varie categorie -->
			<ul>
				<li><a class="active" name="matchPA">Risultati della categoria piccoli amici</a></li>
				<li><a href="#matchEs">Vai ai risultati della categoria esordienti</a></li>
				<li><a href="#matchGi">Vai ai risultati della categoria giovanissimi</a></li>
			</ul>
			</div>

		<xsl:for-each select="x:calendarioPartite/x:piccoliAmici/x:partita">
			<table id="tabellapartite"  summary="Descrive i risultati di una specifica partita">	
					<caption>
						<strong>Partita del <xsl:value-of select="x:dataPartita" /></strong>
					</caption>
				
				<thead>
					<tr>
						<th scope="col">Squadra di Casa</th>
						<th scope="col">Squadra in Transferta</th>
					</tr>
				</thead>
			
				<tbody>
					<tr>
						<td><xsl:value-of select="x:squadraDiCasa" /></td>
						<td><xsl:value-of select="x:squadraInTrasferta" /> </td>
					</tr>
					
					<tr>
						<xsl:choose>	
						<!-- vittoria -->
						 <xsl:when test="x:goalSquadCasa&gt;x:goalSquadTrasf and x:squadraDiCasa='Camponogarese'">
							<td class="vittoria"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="vittoria"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>
							
						<!-- vittoria -->	
						<xsl:when test="x:goalSquadCasa&lt;x:goalSquadTrasf and x:squadraInTrasferta='Camponogarese'">
							<td class="vittoria"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="vittoria"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>

						<!-- sconfitta -->
						 <xsl:when test="x:goalSquadCasa&gt;x:goalSquadTrasf and x:squadraDiCasa!='Camponogarese'">
							<td class="sconfitta"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="sconfitta"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>
							
						<!-- sconfitta -->	
						<xsl:when test="x:goalSquadCasa&lt;x:goalSquadTrasf and x:squadraInTrasferta!='Camponogarese'">
							<td class="sconfitta"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="sconfitta"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>
						<!-- pareggio -->	
						<xsl:otherwise>
							<td class="pareggio"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="pareggio"><xsl:value-of select="x:goalSquadTrasf" /> </td>
						</xsl:otherwise>
					</xsl:choose>
	
					</tr>
				</tbody>
			</table>								
		</xsl:for-each>					
<!-- Calendario ESORDIENTI -->
		<div class="linkAncore">
		<!--link ancore per i risultati delle varie categorie -->
			<ul>
				<li><a href="#matchPA">Vai ai risultati della categoria piccoli amici</a></li>
				<li><a class="active" name="matchEs">Risultati della categoria esordienti</a></li>
				<li><a href="#matchGi">Vai ai risultati della categoria giovanissimi</a></li>
			</ul>
		</div>
				<xsl:for-each select="x:calendarioPartite/x:esordienti/x:partita">
			<table id="tabellapartite"  summary="Descrive i risultati di una specifica partita">	
					<caption>
						<strong>Partita del <xsl:value-of select="x:dataPartita" /></strong>
					</caption>
				
				<thead>
					<tr>
						<th scope="col">Squadra di Casa</th>
						<th scope="col">Squadra in Transferta</th>
					</tr>
				</thead>
			
				<tbody>
					<tr>
						<td><xsl:value-of select="x:squadraDiCasa" /></td>
						<td><xsl:value-of select="x:squadraInTrasferta" /> </td>
					</tr>

					<tr>
						<xsl:choose>	
						<!-- vittoria -->
						 <xsl:when test="x:goalSquadCasa&gt;x:goalSquadTrasf and x:squadraDiCasa='Camponogarese'">
							<td class="vittoria"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="vittoria"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>
							
						<!-- vittoria -->	
						<xsl:when test="x:goalSquadCasa&lt;x:goalSquadTrasf and x:squadraInTrasferta='Camponogarese'">
							<td class="vittoria"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="vittoria"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>

						<!-- sconfitta -->
						 <xsl:when test="x:goalSquadCasa&gt;x:goalSquadTrasf and x:squadraDiCasa!='Camponogarese'">
							<td class="sconfitta"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="sconfitta"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>
							
						<!-- sconfitta -->	
						<xsl:when test="x:goalSquadCasa&lt;x:goalSquadTrasf and x:squadraInTrasferta!='Camponogarese'">
							<td class="sconfitta"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="sconfitta"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>
						<!-- pareggio -->	
						<xsl:otherwise>
							<td class="pareggio"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="pareggio"><xsl:value-of select="x:goalSquadTrasf" /> </td>
						</xsl:otherwise>
					</xsl:choose>
	
					</tr>
				</tbody>
			</table>								
		</xsl:for-each>	
<!-- Calendario giovanissimi -->
		<div class="linkAncore">
		<!--link ancore per le match delle varie categorie -->
			<ul>
				<li><a href="#matchPA">Vai ai risultatu della categoria piccoli amici</a></li>
				<li><a href="#matchEs">Vai ai risultati della categoria esordienti</a></li>
				<li><a class="active" name="matchGi">Risultati della categoria giovanissimi</a></li>
			</ul>
		</div>
						<xsl:for-each select="x:calendarioPartite/x:giovanissimi/x:partita">
			<table id="tabellapartite"  summary="Descrive i risultati di una specifica partita">	
					<caption>
						<strong>Partita del <xsl:value-of select="x:dataPartita" /></strong>
					</caption>
				
				<thead>
					<tr>
						<th scope="col">Squadra di Casa</th>
						<th scope="col">Squadra in Transferta</th>
					</tr>
				</thead>
			
				<tbody>
					<tr>
						<td><xsl:value-of select="x:squadraDiCasa" /></td>
						<td><xsl:value-of select="x:squadraInTrasferta" /> </td>
					</tr>

					<tr>
						<xsl:choose>	
						<!-- vittoria -->
						 <xsl:when test="x:goalSquadCasa&gt;x:goalSquadTrasf and x:squadraDiCasa='Camponogarese'">
							<td class="vittoria"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="vittoria"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>
							
						<!-- vittoria -->	
						<xsl:when test="x:goalSquadCasa&lt;x:goalSquadTrasf and x:squadraInTrasferta='Camponogarese'">
							<td class="vittoria"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="vittoria"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>

						<!-- sconfitta -->
						 <xsl:when test="x:goalSquadCasa&gt;x:goalSquadTrasf and x:squadraDiCasa!='Camponogarese'">
							<td class="sconfitta"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="sconfitta"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>
							
						<!-- sconfitta -->	
						<xsl:when test="x:goalSquadCasa&lt;x:goalSquadTrasf and x:squadraInTrasferta!='Camponogarese'">
							<td class="sconfitta"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="sconfitta"><xsl:value-of select="x:goalSquadTrasf" /> </td> 
						</xsl:when>
						<!-- pareggio -->	
						<xsl:otherwise>
							<td class="pareggio"><xsl:value-of select="x:goalSquadCasa" /></td>
							<td class="pareggio"><xsl:value-of select="x:goalSquadTrasf" /> </td>
						</xsl:otherwise>
					</xsl:choose>
	
					</tr>
				</tbody>
			</table>								
		</xsl:for-each>	
	</div>

	<div id="footer">
		<img class="imgValidCode" src="immagini/valid-xhtml10.png" alt="XHTML valido" />
		<img class="imgValidCode" src="immagini/vcss.gif" alt="CSS valido" />
		<img class="imgValidCode" src="immagini/valid_wcag_aaa.gif" alt="WCAG valido" />
	</div>
	</body>
</html>

</xsl:template>
</xsl:stylesheet>
