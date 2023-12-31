from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from capa_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log


class PersonaDAO:
    """
    DAO significa: Data Access Object
    CRUD:
        -Create: Insertar,
        -Read: Seleccionar,
        -Update: Actualizar,
        -Delete: Eliminar.
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

#Definimos los metodos de clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = [] #Creamos una lista
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            log.debug(f'Persona a insertar: {persona}')
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            log.debug(f'Persona a actualizar: {persona}')
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            log.debug(f'Persona eliminada: {persona}')
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount


if __name__ == '__main__':
    # Insertar un registro
    #persona1 = Persona(nombre='Mateo', apellido='Torres', email='tmateo@mail.com')
    #personas_insertadas = PersonaDAO.insertar(persona1)
    #log.debug(f'Personas insertadas: {personas_insertadas}')

    # # Selleccionar objetos
    # personas= PersonaDAO.seleccionar()
    # for persona in personas:
    #     #log.debug(persona)
    #     print(persona)
    #

    # #eliminar un registro
    # persona1 = Persona(id_persona=2)
    # personas_eliminadas = PersonaDAO.eliminar(persona1)
    # log.debug(f'Personas eliminadas {personas_eliminadas}')

    # #Actualizar un registro
    # persona1 = Persona(id_persona=14, nombre='Mario', apellido='Torres', email='tmateo@mail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # print(personas_actualizadas)
    # #log.debug(f'Personas actualizadas: {personas_actualizadas}')

    persona1 = PersonaDAO.eliminar(Persona(id_persona=13))
    print(persona1)

    personas = PersonaDAO.seleccionar()


