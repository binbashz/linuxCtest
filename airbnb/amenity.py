#!/usr/bin/python3
""" Amenity class """


from models.base_model import BaseModel
# Importacion de la clase BaseModel desde el modulo models.base_model.

class Amenity(BaseModel):
    """ Amenity class, inherits from BaseModel """
    # Definicion de la clase Amenity, que hereda de la clase BaseModel.

    name = ""
    # Declaracion de una variable de clase llamada "name" y se inicializa como una cadena vacia.
