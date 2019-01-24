import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='imap_tools',
    version='0.5',
    packages=setuptools.find_packages(),
    url='https://github.com/ikvk/imap_tools',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author='v.kaukin',
    author_email='workkvk@gmail.com',
    description='Effective working with email messages using IMAP protocol.',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['typing>=3.6.2'],
)
