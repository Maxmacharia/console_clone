#!/usr/bin/python3

import cmd
import sys
import inspect
import models
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
	"""simple command processer"""
	prompt = '(hbnb)'

	def do_update(self, line):
		"""update [class] [id] [attribute_name] [attribute_value]"""
		"""updates an existing instance"""
		arg = line.split()
		if len(arg) < 1:
			print("** class name missing **")
		elif len(arg) == 1:
                        available_classes = {
                                name: cls
                                for name, cls in inspect.getmembers(models, inspect.isclass)
                        }
                        class_name = arg[0]
                        if class_name not in available_classes:
                                print("** class doesn't exist **")
                                return
                        elif len(arg) < 2:
                                print("** instance id missing **")
		elif len(arg) == 2:
			class_name = arg[0]
			id = arg [1]
			key = f"{class_name}.{id}"
			objs = storage.all()
			if key not in objs:
				print("** no instance found **")

			elif len(arg) < 3:
				print("** attribute name missing **")
		elif len(arg) != 4:
			print("** value missing **")
		else:
			class_name = arg[0]
			id = arg[1]
			attribute_name = arg[2]
			attribute_value = arg[3]
			key = f"{class_name}.{id}"
			objs = storage.all()
			existing_instance = objs[key]
			updated_instance = setattr(existing_instance, attribute_name, attribute_value)
	def do_all(self, line):
		"""all [class] print all instances"""
		arg = line.split()
		if len(arg) < 1:
			print("** class name missing **")
		elif len(arg) == 1:
			class_name = arg[0]
			available_classes = {
				name: cls
				for name, cls in inspect.getmembers(models, inspect.isclass)
			}
			if class_name in available_classes:
				obj_all = storage.all()
				for obj in obj_all.values():
					if obj.__class__.__name__ == class_name:
						print(obj)
			else:
				print("** class does not exist **")

	def do_create(self, line):
		"""create [class] It create an instance and print the id"""
		arg = line.split()
		if len(arg) < 1:
			print("** class name missing ** ")
			return
		elif len(arg) == 1:
			available_classes = {
				name: cls
				for name, cls in inspect.getmembers(models, inspect.isclass)
			}
			class_name = arg[0]
			if class_name in available_classes:
				theclass = available_classes[class_name]
				return
			else:
				print("** class does not exist **")
		else:
			available_classes = {
                                name: cls
                                for name, cls in inspect.getmembers(models, inspect.isclass)
                        }
			class_name = arg[0]
			if class_name in available_classes:
				theclass = available_classes[class_name]
				new_instance = theclass()
				for i in arg:
					if '=' not in i:
						continue
					key, value = i.split('=', 1)
					value = value.strip('"').replace('_', ' ')
					setattr(new_instance, key, value)
				new_instance.save()
				print(new_instance.id)

	def do_show(self, line):
		"""show [class] [id] print the string rep of the instance"""
		arg = line.split()
		if len(arg) < 1:
			print("** class name missing **")
		elif len(arg) == 1:
			available_classes = {
                                name: cls
                                for name, cls in inspect.getmembers(models, inspect.isclass)
                        }
			class_name = arg[0]
			if class_name not in available_classes:
				print("** class doesn't exist **")
				return
			elif len(arg) < 2:
				print("** instance id missing **")

		else:
			class_name = arg[0]
			id = arg[1]
			all_objs = storage.all()
			key = f"{class_name}.{id}"
			if key in all_objs:
				obj = all_objs[key]
				print(obj)
			else:
				#print(all_objs)
				print("no instance found")
	def do_destroy(self, line):
		"""destroy [class] [id] destroys the instance of that id"""
		arg = line.split()
		if len(arg) < 1:
			print("** class name missing **")
		elif len(arg) == 1:
                        available_classes = {
                                name: cls
                                for name, cls in inspect.getmembers(models, inspect.isclass)
                        }
                        class_name = arg[0]
                        if class_name not in available_classes:
                                print("** class doesn't exist **")
                                return
                        elif len(arg) < 2:
                                print("** instance id missing **")
		else:
			class_name =arg[0]
			id = arg[1]
			all_objs = storage.all()
			key = f"{class_name}.{id}"
			if key in all_objs:
				del all_objs[key]
				BaseModel().save()
			else:
				print("** no instance found **")

	def do_quit(self, arg):
		"""Quit command to exit the program"""
		return True

	def do_EOF(self, arg):
		"""EOF (End Of File) (press ctrl + D) to exit cleanly"""
		return True

	def do_help(self, arg):
		"""provide guidance on how the functions work"""
		return super().do_help(arg)
if __name__ == '__main__':
	HBNBCommand().cmdloop()
