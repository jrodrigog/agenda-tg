<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
	<head>
		<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
		<title>Bienvenido a su agenda</title>
	</head>
	<body>
		<a href="${tg.url('editar_persona')}">Nueva Persona</a><br/>
		<!--  Esta es la lista de Personas -->
		<table border="1">
			<tr>
				<td>Persona</td>
				<td></td>		
				<td></td>
			</tr>
			<tr py:for="persona in personas">
				<td><a href="${tg.url('editar_persona',id=persona['id'])}"
					py:content="persona['nombre']"/></td>
				<td><a href="${tg.url('editar_cita',cita_persona=persona['id'])}">citar</a></td>
				<td><a href="${tg.url('eliminar_persona',id=persona['id'])}">eliminar</a></td>
			</tr>
		</table><br/>
		<!-- Esta es la lista de citas -->
		<table border="1">
			<tr>
				<td>Fecha</td>
				<td>Persona</td>
				<td>Asunto</td>
				<td></td>
			</tr>
			<tr py:for="cita in citas">
				<td py:content="cita['inicio']"></td>
				<td py:content="cita['persona_nombre']"></td>
				<td><a href="${tg.url('editar_cita',id=cita['id'])}" py:content="cita['asunto']"/></td>
				<td><a href="${tg.url('eliminar_cita',id=cita['id'])}">eliminar</a></td>
			</tr>	
		</table>
	</body>
</html>
