//creo array associativo
var form_personale=
{
	"nome": ["Inserire nome", /^[A-Z][a-z]+$/, "Inserire un nome lungo almeno 2, prima lettera maiuscola"],
	"cognome": ["Inserire cognome", /^[A-Z][a-z]+(\s([A-Z][a-z]+))?$/, "Inserire un cognome lungo almeno 2, prima lettera maiuscola (cognomi con spazio consentiti)"],
	"data":["Inserire data", /^([0-3]{1}[0-9]{1}\/[0,1]{1}[0-9]{1}\/[0-9]{4})|([0-3]{1}[0-9]{1}\-[0,1]{1}[0-9]{1}\-[0-9]{4})$/, "Inserire data, formati consentiti DD/MM/AAAA oppure DD-MM-AAAA"],
	"telefono":["Inserire telefono", /^(0?[0-9]{2,3}\-[0-9]+)|(0?[0-9]{2,3}[0-9]+)$/, "Inserire numero di telefono valido, formati consentiti 111-111111 oppure 111111111"]
	
}

var form_partite=
{
	"casa": ["Inserire squadra di casa", /^[A-Z][a-z]+( ([A-Z][a-z]+))?$/, "Inserire nome squadra di casa, almeno due lettere e prima lettera maiuscola, nomi con spazio consentiti"],
	"trasferta": ["Inserire squadra in trasferta", /^[A-Z][a-z]+( ([A-Z][a-z]+))?$/, "Inserire nome squadra in trasferta, almeno due lettere e prima lettera maiuscola, nomi con spazio consentiti"],
	"data":["Inserire data", /^([0-3]{1}[0-9]{1}\/[0,1]{1}[0-9]{1}\/[0-9]{4})|([0-3]{1}[0-9]{1}\-[0,1]{1}[0-9]{1}\-[0-9]{4})$/, "Inserire data, formati consentiti DD/MM/AAAA oppure DD-MM-AAAA"],
	"goalCasa": ["Inserire goal della squadra di casa", /^[0-9]{1,2}$/, "Inserire goal squadra di casa, 0-99"],
	"goalTrasf": ["Inserire goal della squadra in trasferta", /^[0-9]{1,2}$/, "Inserire goal squadra di casa, 0-99"]
	
}

function caricamento(array) //carica i dati nei campi
{
for (var key in array)
	{
		var input=document.getElementById(key);
		campoDefault(array, input);

		input.onfocus=function(){campoPerInput(array, this);}; //toglie l'aiuto
		input.onblur=function(){validazioneCampo(array, this);}; //fa la validazione del campo
	}
}






function campoDefault(array, input)
{
	if (input.value=="")
	{
		input.className="default-text";
		input.value=array[input.id][0];
	}
}


function campoPerInput(array, input)
{
	if (input.value==array[input.id][0])
	{
		input.value="";
		input.className="";
	}
}


function validazioneCampo(array, input)
{
	var p=input.parentNode; //prende lo span

var errore=document.getElementById(input.id+"errore");

if (errore)
{
	p.removeChild(errore)
}

	var regex=array[input.id][1];
	var text=input.value;
	if ((text==array[input.id][0]) || text.search(regex)!=0) //occhio! controllo che l'input sia diverso dal placeholder (con il primo check)
	{
		mostraErrore(array, input);
		return false;
	}
	return true;
}


function mostraErrore(array, input)
{
	console.log(input);
	var p=input.parentNode;
	var e=document.createElement("strong");
	e.className="errorSuggestion";
	e.id=input.id+"errore";
	//
	//input.id="errore";

	e.appendChild(document.createTextNode(array[input.id][2]));
	p.appendChild(e);
}





// serie di funzioni per rendere visibili le varie opzioni in base ai checkbox selezionati
/* Dopo aver scelto il grado societario mette a disposizione la scelta del ruolo */
function cbCheck(){
	var elem = document.getElementById("sceltaRuolo");
	var grados1 = document.getElementById("amministratore");
	var grados2 = document.getElementById("dipendente");
	var ruolo1 = document.getElementById("mangerHide");
	var ruolo2 = document.getElementById("allenatHide");
if ((grados1.checked) || (grados2.checked)) {
	elem.style.display = "block";

	if (grados1.checked){
		ruolo1.style.display = "block";
		ruolo2.style.display = "none";		
		}

		else{
		ruolo2.style.display = "block";
		ruolo1.style.display = "none";
		}
	}
};
/* Dopo aver scelto il ruolo mette a disposizione la compilazione dei campi dati */
function cbCheck1(){
	var elem = document.getElementById("listaDati");
	var ruolo1 = document.getElementById("manager");
	var ruolo2 = document.getElementById("allenatori");

if ((ruolo1.checked) || (ruolo2.checked)) {
	elem.style.display = "block";

	}
};
function hideRuolo () {
     document.getElementById("sceltaRuolo").style.display = "none";
};

function hideDati () {
     document.getElementById("listaDati").style.display = "none";
};


/* Dopo aver scelto la categoria delle partite, mette a disposizione la compilazione dei campi dati */
function cbCheckPartite(){
	var elem = document.getElementById("listaDati");
	var ruolo1 = document.getElementById("piccoliAmici");
	var ruolo2 = document.getElementById("esordienti");
	var ruolo3 = document.getElementById("giovanissimi");

if ((ruolo1.checked) || (ruolo2.checked) || (ruolo3.checked)) {
	elem.style.display = "block";

	}
};

