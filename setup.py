#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Vladimir Vilimaitis",
    author_email='vladimirvilimaitis@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    description="A beginner-friendly decorator alternative to if __name__ == '__main__': main() idiom.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='main_function',
    name='main_function',
    packages=find_packages(include=['main_function', 'main_function.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/vovavili/main_function',
    version='1.0.5',
    zip_safe=False,
)
