#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from console import HBNBCommand

""" Unitest for command interpreter """
# Este módulo contiene pruebas unitarias para el intérprete de comandos.

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.file_storage = FileStorage()

    def tearDown(self):
        self.console = None

    def test_do_quit(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_output.getvalue(), "")
        # Prueba el método "do_quit" que maneja el comando "quit".
        # Simula la entrada y salida para capturar la salida producida por el comando.
        # Verifica que el comando devuelve True (verdadero) y que la salida está vacía.

    def test_do_EOF(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(fake_output.getvalue(), "\n")
        # Prueba el método "do_EOF" que maneja el comando "EOF".
        # Simula la entrada y salida para capturar la salida producida por el comando.
        # Verifica que el comando devuelve True (verdadero) y que la salida es un salto de línea.

    def test_do_create(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd("create BaseModel")
            output = fake_output.getvalue().strip()
            self.assertTrue(output)
        # Prueba el método "do_create" que maneja el comando "create".
        # Simula la entrada y salida para capturar la salida producida por el comando.
        # Verifica que la salida no esté vacía.

    def test_do_show(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd("show BaseModel 12345")
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "** no instance found **")
        # Prueba el método "do_show" que maneja el comando "show".
        # Simula la entrada y salida para capturar la salida producida por el comando.
        # Verifica que la salida sea igual a la cadena "** no instance found **".

    def test_do_destroy(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd("destroy BaseModel 12345")
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "** no instance found **")
        # Prueba el método "do_destroy" que maneja el comando "destroy".
        # Simula la entrada y salida para capturar la salida producida por el comando.
        # Verifica que la salida sea igual a la cadena "** no instance found **".

    def test_do_all(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd("all")
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "[]")
        # Prueba el método "do_all" que maneja el comando "all".
        # Simula la entrada y salida para capturar la salida producida por el comando.
        # Verifica que la salida sea igual a la cadena "[]".

    def test_do_update(self):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd('update BaseModel 12345 name "John Doe"')
            output = fake_output.getvalue().strip()
            self.assertEqual(output, "** no instance found **")
        # Prueba el método "do_update" que maneja el comando "update".
        # Simula la entrada y salida para capturar la salida producida por el comando.
        # Verifica que la salida sea igual a la cadena "** no instance found **".


if __name__ == "__main__":
    unittest.main()
