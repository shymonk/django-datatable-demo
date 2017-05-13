#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages


setup(
    name='django-datatable-demo',
    version='0.1.0',
    author='shymonk',
    author_email='hellojohn201@gmail.com',
    url='https://github.com/shymonk/django-datatable-demo',
    description='A simple demo for django-datatable',
    packages=find_packages('django_datatable_demo'),
    package_dir={
        '': 'django_datatable_demo',
    },
    include_package_data=True,
    zip_safe=False,
    scripts=[
        'django_datatable_demo/manage.py'
    ],
    entry_points={
        'console_scripts': [
            'django_datatable_demo = manage:main',
        ],
    },
    install_requires=[
        "django>=1.5",
        "supervisor",
        "gunicorn",
        "gevent",
    ],
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
)
