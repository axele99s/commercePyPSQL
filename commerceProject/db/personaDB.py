from py.Persona import Persona  # Asegúrate de que la ruta sea correcta

class PersonaDB:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def cargar_personas(self):
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT * FROM persona')
        rows = cursor.fetchall()

        personas = []
        for row in rows:
            idPersona, idLocalidad, nombre, apellido, dni, tipoDNI = row
            personas.append(Persona(idPersona, nombre, apellido, dni, tipoDNI, idLocalidad))

        cursor.close()
        return personas

    def agregarPersona(self, persona: Persona):
        cursor = self.db_connection.cursor()
        try:
            # Concatenar valores directamente en la consulta (no recomendado)

            cursor.execute(
                'INSERT INTO persona (idLocalidad, nombre, apellido, dni, tipoDNI) VALUES (%s, %s, %s, %s, %s)',
                (persona.idLocalidad, persona.nombre, persona.apellido, persona.dni, persona.tipoDNI)
            )

            # Confirmar los cambios en la base de datos
            self.db_connection.commit()  # Necesario para guardar el nuevo registro
        except Exception as e:
            print(f"Error al agregar persona: {e}")
          # Revertir cambios si ocurre un error
        finally:
            cursor.close()  # Asegúrate de cerrar el cursor
