#!/usr/bin/python3
import inspect
import models

available_classes = {
	name: cls
	for name, cls in inspect.getmembers(models, inspect.isclass)
}
print(available_classes)
