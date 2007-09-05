from turbogears.database import PackageHub
from sqlobject import *

hub = PackageHub('agenda')
__connection__ = hub

class Persona(SQLObject):
    nombre = StringCol()
    telefono = StringCol()
    email = StringCol()
    citas = MultipleJoin( 'Cita', joinColumn = 'cita_id' )
    
class Cita(SQLObject):
    asunto = StringCol()
    inicio = DateTimeCol()
    duracion = IntCol()
    persona = ForeignKey( 'Persona' )

# Crear las tablas (Si no existen), al cargar este modulo
for table in [ Persona, Cita ]:
    table.createTable( ifNotExists = True )
