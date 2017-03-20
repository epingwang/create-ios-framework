import ConfigParser
import os
import types

def options_from_file(filePath, options):
	cf = ConfigParser.ConfigParser()
	cf.read(filePath)
	if (cf.options("create_framework_config")):
		for attr in cf.options("create_framework_config"):
			setattr(options, attr, cf.get("create_framework_config", attr))
	return options

def deep_search_path(root, handler, exception):
	if type(exception) is types.StringType:
		if root.find(exception) != -1:
			return
	if type(exception) is types.ListType:
		for exception_path in exception:
			if (root.find(exception_path) != -1):
				return
			pass
	if type(exception) is types.FunctionType:
		if exception(root):
			return
		pass
	if os.path.isdir(root):
		os.chdir(root)
		for subpath in os.listdir('.'):
			deep_search_path(subpath, handler, exception)
			pass
		os.chdir('../')
		pass
	handler(root)