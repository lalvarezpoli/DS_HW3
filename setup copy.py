try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import Library_hm3_repo


def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='Library_hm3_repo',
    version=Library_hm3_repo.__version__,
    description='First library',
    author='Mikel, Luis, Rui',
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='https://github.com/lalvarezpoli/DS_HW3',
    classifiers=[
        'Programming Language :: Python :: 3.7.1'
    ]
)
