from setuptools import setup 

with open("requirements.txt") as f : 
    requirements = f.read().splitlines()

setup(
        name="pubsub-pytoolbox",
        version="0.0.1",
        packages=["pubsub", "pubsub.op"],
        install_requires=requirements
        )

