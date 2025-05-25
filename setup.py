from setuptools import setup, find_packages

setup(
    name='my_stats_lib',
    version='0.1.0',
    author='Fatma had',
    author_email='fa.hadjebe@gmail.com',
    description='Une bibliothèque pour le calcul des intervalles de confiance',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)