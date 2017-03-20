
from setuptools import setup

setup(name='create-ios-framework',
      version='0.1.2',
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