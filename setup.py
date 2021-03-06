#!/usr/bin/env python

from setuptools import setup

setup(
    name='pyowm',
    version='2.2.1',
    description='A Python wrapper around the OpenWeatherMap web API',
    author='Claudio Sparpaglione (@csparpa)',
    author_email='csparpa@gmail.com',
    url='http://github.com/csparpa/pyowm',
    packages=['pyowm', 'pyowm.abstractions', 'pyowm.caches', 'pyowm.commons',
              'pyowm.exceptions', 'pyowm.utils', 'pyowm.webapi25',
              'pyowm.webapi25.cityids', 'pyowm.webapi25.xsd',
              'tests.unit', 'tests.functional'],
      long_description="""\
      PyOWM is a client Python wrapper library for the OpenWeatherMap web API.
      It allows quick and easy consumption of OWM weather data from Python
      applications via a simple object model and in a human-friendly fashion.
      """,
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries",
    ],
    package_data = {
        '': ['*.txt', '*.xsd']
    },
    keywords='openweathermap web api client wrapper weather forecast data OWM',
    license='MIT',
    test_suite='tests'
)
