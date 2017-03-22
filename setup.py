
from setuptools import setup
import re

def get_version():
  """Retrieves package version from the file."""
  with open('crif/_version.py') as fh:
    m = re.search("'([^']*)'", fh.read())
  if m is None:
    raise ValueError("Unrecognized version in 'crif/_version.py'")
  return m.groups()[0]

setup(name='create-ios-framework',
      version=get_version(),
      description='a tool to create iOS framework',
      url='http://github.com/epingwang/createiosframework',
      author='Wang YiPing',
      author_email='me@epingwang.me',
      license='MIT',
      packages=['crif'],
      zip_safe=False,
      entry_points={
      	'console_scripts': [
      		'create-ios-framework=crif:main',
      	],
      })