import io
import os

from distutils.file_util import copy_file
from setuptools import setup

base_gh_url = 'https://github.com/sowemail/'
dir_path = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(dir_path, 'README.rst')
version_path = os.path.join(dir_path, 'VERSION.txt')

with io.open(readme_path, encoding='utf-8') as readme_file:
    readme = readme_file.read()
with io.open(version_path, encoding='utf-8') as version_file:
    version = version_file.read().strip()

copy_file(version_path,
          os.path.join(dir_path, 'sowerest', 'VERSION.txt'),
          verbose=False)


def parse_requirements(filename):
    """load requirements from a pip requirements file"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and (not line.startswith("#") and not line.startswith('-'))]


setup(
    name='sowerest',
    version=version,
    author='Fourat Zouari',
    author_email='opensource@sowemail.com',
    url='{}sowerest-python'.format(base_gh_url),
    download_url='{}sowerest-python/tarball/{}'.format(base_gh_url, version),
    packages=['sowerest'],
    include_package_data=True,
    install_requires=parse_requirements('install-requirements.pip'),
    tests_require=parse_requirements('test-requirements.pip'),
    license='MIT',
    description='HTTP REST client, simplified for SeWeMail API',
    long_description_content_type='text/x-rst',
    long_description=readme,
    keywords=[
        'REST',
        'HTTP',
        'API',
        'SOWEMAIL'],
    python_requires='>=3.4.*',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
