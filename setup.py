# -*- coding: utf-8 -*-

from setuptools import setup


DESCRIPTION = open('README.md').read()
setup(
    name='django-activity-log',
    version='1.0.5',
    description='HTTP queries logger with flexible filters.',
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Hossein SayyedMousavi',
    author_email='hossein.sayyedmousavi@gmail.com',
    keywords=[
        "django",
        "database",
        "user",
        "activity log"
    ],
    packages=[
        'activity_log',
        'activity_log.migrations',
    ],
    url='https://github.com/HosseinSayyedMousavi',
    license='MIT License',
    readme="README.md",
    install_requires=[
        'django',
    ],

    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
