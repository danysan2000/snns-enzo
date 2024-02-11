#!/usr/bin/python3

from distutils.core import setup, Extension, extension_keywords

#print extension_keywords

module1 = Extension('krui',
                    sources = ['snns/krui.c'],
		    include_dirs = ['../kernel/sources'],
		    library_dirs = ['../kernel/sources'],
		    libraries = ['kernel','func','fl'])

setup (name = 'snns-kernel',
       ext_package='snns',
       version = '0.2',
       author='DanySan',
       author_email='danysanuru@gmail.com',
       description = 'SNNS kernel functions',
       packages = ['snns'],
       ext_modules = [module1],
       py_modules = ['snns.util'])

