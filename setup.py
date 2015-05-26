from setuptools import setup, find_packages
import os
import generic


def file_name(rel_path):
    dir_path = os.path.dirname(__file__)
    return os.path.join(dir_path, rel_path)


def readlines(rel_path):
    with open(file_name(rel_path)) as f:
        ret = f.readlines()
    return ret


setup(
    author="My Name",
    name="generic",
    version=generic.__version__,
    packages=find_packages(exclude=["tests*", ]),
    url="https://github.com/hangarunderground/generic",
    description="This app does something. I tell you about it here.",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords=['django'],
    install_requires=readlines('requirements.txt'),
    include_package_data=True
)
