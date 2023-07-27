import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='SharePoint_Module',
    version='0.0.1',
    author='DK-Hieu',
    author_email='dk20101995@gmail.com',
    description='module to download file from sharepoint',
    url='https://github.com/fptsdata/FTA_sourcecode/tree/main/Sharepoint_module',
    license='MIT',
    packages=['SharePoint_Module'],
    install_requires=['requests'],
)