<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
	<head>
		<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
		<title>${titulo_pagina}</title>
	</head>
	<body>
		<a href="${tg.url('/')}">Regresar a la agenda</a><br/>
		<form method="POST" action="${accion_post}">
			<input py:if="id" type="hidden" name="id" value="${id}"/>
			Asunto<br/>
			<input type="text" name="asunto" value="${asunto}"/><br/>
			Persona<br/>
			<select name="persona">
				<option py:for="persona in personas"
						py:content="persona['nombre']" value="${persona['id']}"
						selected="${(None,'')[persona['id']==cita_persona]}"/>
			</select><br/>
			Fecha Inicio<br/>
			<input type="text" name="inicio" value="${inicio}"/><br/>
			Duracion<br/>
			<select name="duracion">
				<option py:for="i in range(15,360,15)" py:content="i"
						selected="${(None,'')[duracion==i]}"/>
			</select> minutos<br/>
			<input type="submit" value="${texto_boton}"/>
		</form>
	</body>
</html>
