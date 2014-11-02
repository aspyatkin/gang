from setuptools import setup, find_packages


setup(
    name='gang',
    version='0.0.6',
    description='Python dictionary with dot-style access',
    author='Alexander Pyatkin',
    author_email='asp@thexyz.net',
    packages=find_packages('.'),
    data_files=[],
    install_requires=['setuptools>=5.4'],
    url='https://github.com/aspyatkin/gang',
    license='MIT',
    test_suite='nose.collector',
    extras_require={'test': ['nose', 'unittest2']},
    tests_require=['nose'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities'
    ]
)
