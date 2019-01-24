from distutils.core import setup

setup(
    name='imap_tools',
    version='0.5',
    packages=['imap_tools'],
    url='https://github.com/ikvk/imap_tools',
    license='MIT',
    long_description=open("README.rst").read(),
    author='v.kaukin',
    author_email='workkvk@gmail.com',
    description='Effective working with email messages using IMAP protocol.',
    install_requires=['typing>=3.6.2'],
)
