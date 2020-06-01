var formulario = document.getElementById('aplicacion');
formulario.addEventListener('submit', function(e){e.preventDefault()});

function notacionPrefija()
{
	var data = document.getElementById('operacion').value;
	if (data == '');
	else
		eel.Prefija(data)(setResult)(function (ret) {console.log(ret)})

}

eel.expose(callbackPosfija)
function callbackPosfija(X) {
document.getElementById('resultado').value = X
}

function notacionPostfija()
{
	var data = document.getElementById('operacion').value;
	if (data == '');
	else
		eel.Postfija(data)(setResult)(function (ret) {console.log(ret)})
}

eel.expose(callbackPrefija)
function callbackPrefija(X) {
document.getElementById('resultado').value = X
}
