import setuptools

with open("README.rst", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='imap_tools',
    version='0.9.4',
    packages=setuptools.find_packages(),
    url='https://github.com/ikvk/imap_tools',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author='v.kaukin',
    author_email='workkvk@gmail.com',
    description='Working with email and mailbox using IMAP protocol.',
    keywords=['imap', 'imap-client', 'python3', 'email'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # install_requires=['typing>=3.6.2'],
)
