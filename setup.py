#!/usr/bin/env python

import setuptools


setuptools.setup(
        name='legiosa',
        version='0.1',
        description='Generate lego mosaics',
        license='MIT',
        long_description=(open('README.rst').read()),
        author='Joshua Downer',
        author_email='joshua.downer@gmail.com',
        url='http://github.com/jdowner/legiosa',
        keywords='lego mosaic image',
        packages=['legiosa'],
        package_data={
          '': ['*.rst', 'LICENSE'],
#          '': ['share/*', '*.rst', 'LICENSE'],
        },
        data_files=[
          ('share/legiosa/', [
              'README.rst',
              'LICENSE',
              ]),
        ],
        scripts=['bin/legiosa'],
        install_requires=[
            'pep8',
            'numpy',
            ],
        platforms=['Unix'],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: MIT License',
            'Operating System :: Unix',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Artistic Software',
            'Topic :: Multimedia',
            'Topic :: Multimedia :: Graphics',
            'Topic :: Multimedia :: Graphics :: Graphics Conversion',
            'Topic :: Utilities',
            ]
        )
