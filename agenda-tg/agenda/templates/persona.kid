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
			Nombre<br/>
			<input type="text" name="nombre" value="${nombre}"/><br/>
			Telefono<br/>
			<input type="text" name="telefono" value="${telefono}"/><br/>
			Email<br/>
			<input type="text" name="email" value="${email}"/><br/>
			<input type="submit" value="${texto_boton}"/>
		</form>
	</body>
</html>
