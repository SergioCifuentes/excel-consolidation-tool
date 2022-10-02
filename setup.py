from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    
requirements = []
    
setup(
    name="excel-consolidation-tool",
    version="0.0.1",
    author="Sergio Cifuentes",
    author_email="sergiocifuentes1485@gmail.com",
    description="Excel consolidation tool with a folder watcher",
    url="https://github.com/SergioCifuentes/excel-consolidation-tool/",
    install_requires=requirements,
)