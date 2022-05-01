from setuptools import setup
setup (
    name = 'package_name',
    version = '0.0',
    py_modules = ['module'],
    install_requires = [
        'setuptools'
    ],
    entry_points = '''
        [console_scripts]
        module=module:__init__
    '''
)