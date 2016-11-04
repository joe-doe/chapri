from setuptools import setup

version = '0.1'

setup(
    name='chapri',
    version=version,
    url='http://github.com/',
    license='MIT',
    author='Joe Doe',
    author_email='joe.doe@engineer.com',
    description='Chat Prive',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'python-socketio>=1.5.0',
        'python-engineio>=1.0.0',
        'eventlet',
        'gunicorn',
        'flask-socketio',
        'pymongo'
    ],
    test_suite='tests'
)
