# setup.py
from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    required = f.read().splitlines()

constant = "-e ."
if constant in required:
    required.remove(constant)  # Remove the editable install line if it exists

setup(
    name='fssai_chatbot',
    version='1.0.0',
    author='Ketan Raj',
    author_email='ketanraj612@gmail.com',
    description='A chatbot for querying FSSAI food additive regulations.',
    long_description=open('README.md').read(), # You should have a README.md
    long_description_content_type='text/markdown',
    packages=find_packages(), # Automatically find all packages in your 'src' directory
    install_requires=required, # Use dependencies from requirements.txt
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # Choose a license
        'Operating System :: OS Independent',
    ],
    # This creates a runnable command in the terminal after installation
    entry_points={
        'console_scripts': [
            'run-fssai-ingest=ingest:main',
            'run-fssai-chatbot=app:main',
        ],
    },
)