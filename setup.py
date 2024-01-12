from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='RankGPT',
    version='0.1.0',
    description='A Python package for RankGPT',
    url='https://github.com/farazkh80/RankGPT',
    author='Faraz Khoubsirat',
    author_email='fkhoubsi@uwaterloo.ca',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements,  # Include the dependencies from requirements.txt
    classifiers=[
        # Classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
