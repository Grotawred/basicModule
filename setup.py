from setuptools import setup

with open("README.md", "r",encoding="utf-8") as file:
    long_description = file.read


setup(
    name='linux-comands',
    version=1.0,
    description="Basic linux comands",
    long_description=long_description,
    author="Grisha Vlasko",
    author_email="grishavlasko200@gmail.com",
    long_description_content_type="text/markdown",
    packages=['linux-commands'],
    url="https://github.com/Grotawred/basicModule",
    install_requires=[]
)