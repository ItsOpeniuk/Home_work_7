from setuptools import setup, find_namespace_packages

setup(
    name='sort_package',
    version='1.0.1',
    url='https://github.com/ItsOpeniuk/Home_work_7',
    author='Openiuk',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': ['clean-folders = sort_package.sort_script:main']
    }
)