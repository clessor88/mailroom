from setuptools import setup


setup(
    name='mailroom',
    description='A Auto email generate program.',
    version=0.1,
    author='Mike Harrison',
    author_email='sample@sample.com',
    license='MIT',
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    instal_requires=[],
    extra_requires={'test': ['pytest', 'pytest-watch', 'tox']},
    )