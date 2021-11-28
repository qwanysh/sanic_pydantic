from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='sanicpydantic',
    version='0.0.3',
    description='Pydantic validation for Sanic framework',
    url='https://github.com/qwanysh/sanic_pydantic',
    author='Kuanysh Beisembayev',
    author_email='kuanysh.beisembayev@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['sanic_pydantic'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'sanic',
        'pydantic',
    ],
)
