from turbogears import controllers, expose, flash, redirect
import time
from datetime import datetime
from model import *

# import logging
# log = logging.getLogger("agenda.controllers")

class Root(controllers.RootController):
    @expose(template="agenda.templates.indice")
    def index(self):
        # Recuperar todas las personas, la vista requiere su identificador y nombre.
        personas = [ { "id" : persona.id, "nombre" : persona.nombre }
                     for persona in Persona.select() ]
        # Recuperar todas las citas, la vista requiere su identificador, titulo y nombre. 
        citas = [ { "id" : cita.id, "asunto" : cita.asunto, "inicio" : cita.inicio,
                    "persona_nombre" : cita.persona.nombre }
                   for cita in Cita.select() ]
        # Enviamos los datos a la vista.
        return dict( personas = personas, citas = citas )
    
    @expose(template="agenda.templates.persona")
    def editar_persona( self, id = None ):
        if id:
            # Si existe un identificador (id) de persona, debemos actualizar
            # la persona, por tanto la recuperamod de la base de datos.
            persona = Persona.get( id )
            # Establecer los parametros de la vista (Valores del formulario).
            return dict( id = persona.id, nombre = persona.nombre,
                         telefono = persona.telefono, email = persona.email,
                         titulo_pagina = "Actualizar Persona", texto_boton = "actualizar",
                         accion_post = "actualizar_persona" )
        else:
            # No existe un identificador, establecer valores por defecto para la vista.
            return dict( id = id, nombre = "", telefono = "", email = "",
                         titulo_pagina = "Insertar Persona", texto_boton = "insertar",
                         accion_post = "insertar_persona" )
            
    @expose()
    def insertar_persona( self, nombre, telefono, email ):
        # Instanciar una nueva persona equivale a insertarla en la base de datos.
        persona = Persona( nombre = nombre, telefono = telefono, email = email )
        # Ir a la pagina de edicion de personas, enviar el identificador de la nueva persona.
        raise redirect( "/editar_persona", id = persona.id )

    @expose()
    def actualizar_persona( self, id, nombre, telefono, email ):
        # Recuperar la persona de la base de datos mediante su identificador.
        persona = Persona.get( id )
        # El metodo set actualiza los atributos de una persona en una sola operacion.
        persona.set( nombre = nombre, telefono = telefono, email = email )
        # Volvemos a editar la persona, enviamos su identificador.
        raise redirect( "/editar_persona", id = id )
    
    @expose()
    def eliminar_persona( self, id ):
        # Eliminar la persona de la base de datos, mediante el metodo estatico delete.
        Persona.delete( id )
        # Retornar a la pagina principal.
        raise redirect( "/" )
    
    @expose(template="agenda.templates.cita")
    def editar_cita( self, id = None, cita_persona = None ):
        # Recuperar todas las personas, mostraremos una lista en la vista.
        personas = [ { "id" : persona.id, "nombre" : persona.nombre }
                    for persona in Persona.select() ]
        if id:
            # Si existe un identificador, recuperar la cita de la base de datos.
            cita = Cita.get( id )
            # Establecer los parametros de la vista
            return dict( id = cita.id, asunto = cita.asunto, inicio = self.escribe_fecha( cita.inicio ),
                         duracion = cita.duracion, cita_persona = cita.persona.id,
                         personas = personas, titulo_pagina = "Actualizar Cita",
                         texto_boton = "actualizar", accion_post = "actualizar_cita" )
        else:
            # No existe un identificador, establecer valores por defecto para la vista.
            return dict( id = None, asunto = "", inicio = self.escribe_fecha(),
                         duracion = 60, cita_persona = int( cita_persona ), personas = personas, 
                         titulo_pagina = "Insertar Cita", texto_boton = "insertar",
                         accion_post = "insertar_cita" )
           
    def escribe_fecha(self, fecha=None ):
        if not fecha:
            return time.strftime("%d-%m-%Y %H:%M")
        return fecha.strftime("%d-%m-%Y %H:%M")
    
    def lee_fecha( self, fecha ):
        return datetime( *time.strptime( fecha, "%d-%m-%Y %H:%M" )[0:6] )

    @expose()
    def insertar_cita( self, asunto, inicio, duracion, persona ):
        # Recuperar la persona citada
        persona = Persona.get( persona )
        # Instanciar una cita, se insertara en la base de datos.
        cita = Cita( asunto = asunto, persona = persona,
                     inicio = self.lee_fecha( inicio ), duracion = int( duracion ) )
        # Ir a la pagina de edicion de citas, enviar el identificador de la nueva cita.
        #raise redirect( "/editar_cita", cita.id )
        raise redirect( "/editar_cita", id=cita.id )
        
    @expose()
    def actualizar_cita(self, id, asunto, inicio, duracion, persona ):
        # Recuperar la persona citada
        persona = Persona.get( persona )        
        # Recuperar la cita de la base de datos.
        cita = Cita.get( id )
        # Actualizar los datos de la cita.
        cita.set( asunto = asunto, inicio = self.lee_fecha( inicio ),
                  persona = persona, duracion = int( duracion ) )
        # Volvemos a editar la cita, enviamos su identificador.
        raise redirect( "/editar_cita", id=id )
    

    @expose()
    def eliminar_cita( self, id ):
        # Eliminar la cita de la base de datos.
        Cita.delete( id )
        # Retornar a la pagina principal.
        raise redirect( "/" )
    