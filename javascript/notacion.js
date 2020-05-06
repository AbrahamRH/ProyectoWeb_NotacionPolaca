var formulario = document.getElementById('aplicacion');
formulario.addEventListener('submit', function(e){e.preventDefault()});

function notacionPrefija()
{
	var string = document.getElementById('operacion').value;
	if (string == '');
	else
		document.getElementById('resultado').value = "Nada por el momento";
}

function notacionPostfija()
{
	var string = document.getElementById('operacion').value;
	if (string == '');
	else
		document.getElementById('resultado').value = "Nada por el momento";
}