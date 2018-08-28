#! /usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="{{ cookiecutter.package_url }}",
    download_url = "{{ cookiecutter.package_url }}.git",

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description='\n\n'.join(
        open(f, 'rb').read().decode('utf-8')
        for f in ['README.rst', 'HISTORY.rst']),

    packages=setuptools.find_packages(),

    install_requires=[],

    license='MIT License',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
