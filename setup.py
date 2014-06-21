from setuptools import setup, find_packages


setup(
    name='gang',
    version='0.0.0',
    description='Python dictionary with dot-style access',
    author='Alexander Pyatkin',
    author_email='asp@thexyz.net',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    data_files=[],
    install_requires=[],
    url='http://pypi.python.org/pypi/gang',
    license='LICENSE'
)
