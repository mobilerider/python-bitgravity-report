from distutils.core import setup
from os.path import dirname, join as path_join


def filepath_from_pkg(filepath):
    # return path_join(dirname(__file__), filepath)
    return path_join('./', filepath)


def filecontent_from_pkg(filepath):
    with open(filepath_from_pkg(filepath), 'r') as f:
        return f.read()


setup(
    name='bitgravity',
    version='0.1dev',
    author='Armando Perez Marques',
    author_email='gmandx@gmail.com',
    packages=['bitgravity', ],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=filecontent_from_pkg('README.txt'),
    install_requires=[l for l in filecontent_from_pkg('requirements.txt').splitlines() if l.strip()],
)
