#!/usr/bin/python

from optparse import OptionParser
import os
from crif.utils import (options_from_file, deep_search_path)
import time
import getpass

def file_handler_wrap(options):
	def file_handler(filepath):
		if os.path.isfile(filepath):
			contents = []
			with open(filepath, 'r') as fread:
				for line in fread.readlines():
					line = line.replace('{{projectname}}', options.projectname)\
					.replace('{{organizationname}}', options.organizationname)\
					.replace('{{prefix}}', options.prefix)\
					.replace('{{date}}', options.date)\
					.replace('{{author}}', options.author)
					contents.append(line)
			with open(filepath+'__w', 'w') as fwrite:
				fwrite.writelines(contents)
			os.chmod(filepath+'__w', os.stat(filepath).st_mode)
			os.remove(filepath)
			os.rename(filepath+'__w', filepath)
			pass
		if filepath.find('{{projectname}}') != -1:
			new_path = filepath.replace('{{projectname}}', options.projectname)
			os.rename(filepath, new_path)
			pass
	return file_handler

def main():
	parser = OptionParser() 

	parser.add_option(
		"-f", 
		"--file", 
		dest="filepath",
		help="choose config file to create framework"
		)
	parser.add_option(
		"-n",
		"--name",
		dest="projectname",
		help="name of the framework project"
		)
	parser.add_option(
		"-p",
		"--prefix",
		dest="prefix",
		help="bundle id prefix"
		)
	parser.add_option(
		"--organization",
		dest="organizationname",
		help="organization name"
		)

	(options, args) = parser.parse_args()

	if options.filepath:
		options_from_file(options.filepath, options)

	if options.projectname == None:
		options.projectname = raw_input('project name:')

	if options.prefix == None:
		options.prefix = raw_input('bundle id prefix:')

	if options.organizationname == None:
		options.organizationname = raw_input('organization name:')

	options.date = time.strftime('%Y/%m/%d',time.localtime(time.time()))
	options.author = getpass.getuser()
	print options.author

	projectname = options.projectname

	os.system("git clone https://github.com/epingwang/iOSFrameworkTemplate.git -b name-replace")
	# rename root directory
	os.rename("iOSFrameworkTemplate", projectname)

	deep_search_path(projectname, file_handler_wrap(options), ['.git', '.DS_Store', '.xcuserdatad'])

	os.chdir(projectname+'/'+projectname+'Demo')
	os.system('pod install')

if __name__ == '__main__':
  main()