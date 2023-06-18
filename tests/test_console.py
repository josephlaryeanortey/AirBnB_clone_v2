#!/usr/bin/python3
"""Unittest modlue for Airbnb clone console"""

from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
import unittest
import console
import tests
import pep8
import os


class TestConsole(unittest.TestCase):
    """Class to test console"""

    @classmethod
    def setUpClass(cls_instance):
        """Function to set variable for console instance"""

        cls_instance.console = HBNBCommand()

    @classmethod
    def teardown(cls_instance):
        """Function that removes setup variables"""

        del cls_instance.console
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_doc_strings(self):
        """Function to test if doctrings are present"""

        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
        self.assertIsNotNone(HBNBCommand.update_dict.__doc__)

    def test_emptyline(self):
        """Function to test emptyline command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual(f.getvalue(), '')

    def test_quit(self):
        """Function that tests the quit command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_console_style(self):
        """Function to check if file is pep8"""

        f_style = pep8.StyleGuide(quiet=True)
        style = f_style.check_files(['console.py'])
        self.assertEqual(style.total_errors, 0, "not pep8")

    def test_test_console_style(self):
        """Function to check if file is pep8"""

        f_style = pep8.StyleGuide(quiet=True)
        style = f_style.check_files(['tests/test_console.py'])
        self.assertEqual(style.total_errors, 0, "not pep8")

    def test_create(self):
        """Function to test create command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Mando")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.all()")
            self.assertEqual('[]\n', f.getvalue()[:7])

    def test_all(self):
        """Function to test all command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all something")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Place")
            self.assertEqual("[]\n", f.getvalue())

    def test_destroy(self):
        """Function to test destroy command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy lgbt")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 419")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.destroy('419')")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_update(self):
        """Function to test update command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update phone")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 419")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 13")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_show(self):
        """Test cmd output: show"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("ShitClass.show()")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Review")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show('419')")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_cmd(self):
        """Function to test cmd"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.count()")
            self.assertEqual(int, type(eval(f.getvalue())))


if __name__ == "__main__":
    unittest.main()
