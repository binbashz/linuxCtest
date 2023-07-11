#!/usr/bin/python3
"""
BaseModel module for AirBnB clone project.
"""


import uuid
from datetime import datetime
from models import storage
# Importación de los módulos y clases necesarios para el proyecto desde los archivos correspondientes.

class BaseModel:
    """
    Base class for all models.
    """
    # Definicion de la clase BaseModel, que sirve como clase base para todos los modelos.

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        """
        # Metodo de inicializacion de una nueva instancia de BaseModel.

        # Verifica si se proporcionaron argumentos con nombre.
        if kwargs:
            # Itera sobre los argumentos con nombre proporcionados.
            for key, value in kwargs.items():
                # Verifica si la clave no es '__class__'.
                if key != '__class__':
                    # Establece el atributo correspondiente en la instancia con el valor proporcionado.
                    setattr(self, key, value)
                # Verifica si la clave es 'created_at' o 'updated_at'.
                if key == 'created_at' or key == 'updated_at':
                    # Establece el atributo correspondiente en la instancia como un objeto datetime creado a partir de la cadena de fecha proporcionada.
                    setattr(
                        self,
                        key,
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    )
        else:
            # Genera un ID único para la instancia.
            self.id = str(uuid.uuid4())
            # Establece el atributo 'created_at' como la fecha y hora actual.
            self.created_at = datetime.now()
            # Establece el atributo 'updated_at' como la fecha y hora actual.
            self.updated_at = self.created_at
            # Agrega la instancia al diccionario de almacenamiento.
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        # Método que devuelve una representación en cadena de la instancia de BaseModel.

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        # Método que actualiza el atributo 'updated_at' con la fecha y hora actual.

        self.updated_at = datetime.now()
        # Guarda los cambios en el diccionario de almacenamiento.
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        # Método que devuelve una representación de diccionario de la instancia de BaseModel.

        obj_dict = self.__dict__.copy()
        # Agrega el nombre de la clase al diccionario.
        obj_dict['__class__'] = self.__class__.__name__
        # Convierte la fecha y hora a una cadena en formato ISO y agrega los atributos 'created_at' y 'updated_at' al diccionario.
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
