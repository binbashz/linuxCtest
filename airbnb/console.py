#!/usr/bin/python3
"""
Console module for AirBnB clone project.
"""

import sys
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
# Importacion de los modulos y clases necesarios para el proyecto desde los archivos correspondientes.

class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}
# Diccionario que mapea los nombres de las clases a sus clases correspondientes.

class HBNBCommand(cmd.Cmd):
    """
    Command-line interpreter for AirBnB clone.
    """
    # Definicion de la clase HBNBCommand, que es una subclase de cmd.Cmd, utilizada como el interprete de linea de comandos.

    prompt = "(hbnb) "
    # Establece el indicador de comandos en el interprete de linea de comandos.

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        # Metodo que maneja el comando "quit" para salir del programa.
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        # Método que maneja el comando "EOF" (End of File) para salir del programa.
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        # Método llamado cuando se ingresa una línea vacía y no realiza ninguna acción.
        pass

    def help_quit(self):
        """ Help message for quit command """
        # Método que proporciona un mensaje de ayuda para el comando "quit".
        print("Quit command to exit the program.")
        print()

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, save it, and print the id.
        """
        # Método que maneja el comando "create". Crea una nueva instancia de la clase BaseModel o de una de sus subclases, la guarda y muestra el ID de la instancia creada.

        # Divide el argumento en una lista de palabras separadas.
        args_list = arg.split()

        # Verifica si se proporcionó al menos una palabra en la lista.
        if len(args_list) < 1:
            print("** class name missing **")
        # Verifica si la primera palabra en la lista, está en las claves del diccionario de clases.
        elif args_list[0] in class_dict.keys():
            # Crea una nueva instancia de la clase correspondiente a la primera palabra en la lista.
            new_instance = class_dict[args_list[0]]()
            # Guarda la nueva instancia.
            new_instance.save()
            # Imprime el ID de la nueva instancia.
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show the string representation of an instance based
        on the class name and id.
        """
        # Método que maneja el comando "show". Muestra la representación en cadena de una instancia basada en el nombre de la clase y el ID proporcionados.

        # Divide el argumento en una lista de palabras separadas.
        args_list = arg.split()

        # Verifica si se proporcionó al menos una palabra en la lista.
        if len(args_list) < 1:
            print("** class name missing **")
        # Verifica si la primera palabra en la lista no está en las claves del diccionario de clases.
        elif args_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        # Verifica si se proporcionaron al menos dos palabras en la lista.
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            # Combina el nombre de la clase y el ID para formar una clave.
            key = args_list[0] + "." + args_list[1]
            # Verifica si la clave existe en el diccionario de almacenamiento.
            if key in storage.all().keys():
                # Imprime la instancia correspondiente a la clave.
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy an instance based on the class name and id.
        """
        # Método que maneja el comando "destroy". Destruye una instancia basada en el nombre de la clase y el ID proporcionados.

        # Divide el argumento en una lista de palabras separadas.
        args_list = arg.split()

        # Verifica si se proporcionó al menos una palabra en la lista.
        if len(args_list) < 1:
            print("** class name missing **")
        # Verifica si la primera palabra en la lista no está en las claves del diccionario de clases.
        elif args_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        # Verifica si se proporcionaron al menos dos palabras en la lista.
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            # Combina el nombre de la clase y el ID para formar una clave.
            key = args_list[0] + "." + args_list[1]
            # Verifica si la clave existe en el diccionario de almacenamiento.
            if key in storage.all().keys():
                # Elimina la instancia correspondiente a la clave del diccionario de almacenamiento.
                del storage.all()[key]
                # Guarda los cambios en el diccionario de almacenamiento.
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print string representation of all instances based on the class name.
        """
        # Método que maneja el comando "all". Muestra la representación en cadena de todas las instancias basadas en el nombre de la clase.

        # Divide el argumento en una lista de palabras separadas.
        args = arg.split()

        # Verifica si no se proporcionaron palabras en la lista.
        if len(args) < 1:
            # Obtiene una lista de representaciones en cadena de todas las instancias en el diccionario de almacenamiento.
            instances = [str(instance) for instance in storage.all().values()]
            # Imprime la lista de representaciones en cadena.
            print(instances)
        # Verifica si la primera palabra en la lista no está en las claves del diccionario de clases.
        elif args[0] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            selected_values = []
            # Itera sobre todas las claves y valores en el diccionario de almacenamiento.
            for k, v in storage.all().items():
                # Verifica si la clave comienza con el nombre de la clase.
                if k.startswith(args[0]):
                    # Agrega la representación en cadena del valor a la lista seleccionada.
                    selected_values.append(str(v))
            # Imprime la lista de representaciones en cadena seleccionadas.
            print(selected_values)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        """
        # Método que maneja el comando "update". Actualiza una instancia basada en el nombre de la clase, el ID, el nombre del atributo y el valor proporcionados.

        # Divide el argumento en una lista de palabras separadas.
        args_list = arg.split()

        # Verifica si se proporcionó al menos una palabra en la lista.
        if len(args_list) < 1:
            print("** class name missing **")
        # Verifica si la primera palabra en la lista no está en las claves del diccionario de clases.
        elif args_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        # Verifica si se proporcionaron al menos dos palabras en la lista.
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            # Combina el nombre de la clase y el ID para formar una clave.
            key = args_list[0] + "." + args_list[1]
            # Verifica si la clave existe en el diccionario de almacenamiento.
            if key in storage.all().keys():
                # Verifica si se proporcionaron al menos tres palabras en la lista.
                if len(args_list) < 3:
                    print("** attribute name missing **")
                # Verifica si se proporcionaron al menos cuatro palabras en la lista.
                elif len(args_list) < 4:
                    print("** value missing **")
                else:
                    # Obtiene la instancia correspondiente a la clave.
                    instance = storage.all()[key]
                    # Obtiene el nombre del atributo de la lista.
                    attr_name = args_list[2]
                    # Obtiene el valor del atributo de la lista y elimina las comillas si están presentes.
                    attr_value = args_list[3].strip('"')
                    # Verifica si la instancia tiene un atributo con el nombre proporcionado.
                    if hasattr(instance, attr_name):
                        # Obtiene el tipo de datos del atributo.
                        attr_type = type(getattr(instance, attr_name))
                        # Actualiza el valor del atributo con el tipo de datos correcto.
                        setattr(instance, attr_name, attr_type(attr_value))
                        # Guarda los cambios en el diccionario de almacenamiento.
                        storage.save()
                    else:
                        print("** attribute doesn't exist **")
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
