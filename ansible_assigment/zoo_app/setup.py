from setuptools import setup, find_packages

setup(
    name='Zoo app installer',
    version='0.0.0.1',
    description='Rescieve POST messages with json strings and output what are animals says',
    author='Maksim Koshelev',
    author_email='annox4uk@gmail.com',
    license='',
    packages=find_packages(),
    install_requires=[
        'flask, emoji'
    ],
    zip_safe=False
)
