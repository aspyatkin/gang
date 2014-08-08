from setuptools import setup, find_packages


setup(
    name='gang',
    version='0.0.3',
    description='Python dictionary with dot-style access',
    author='Alexander Pyatkin',
    author_email='asp@thexyz.net',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    data_files=[],
    install_requires=['setuptools>=5.4'],
    url='https://github.com/aspyatkin/gang',
    license='MIT',
    test_suite='nose.collector',
    extras_require={'test': ['nose']},
    tests_require=['nose']
)
