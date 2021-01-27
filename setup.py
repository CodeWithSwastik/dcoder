from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='dcoder',
  version='0.2.1',
  description='A module that can decode/encode text in various ciphers.',
  long_description=open('README.md').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/CodeWithSwastik/dcoder", 
  project_urls={
   "Documentation": "https://dcoder.readthedocs.io/en/latest/",
   "Issue tracker": "https://github.com/CodeWithSwastik/dcoder/issues",
   },
  author='Swas.py',
  author_email='cwswas.py@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='decoder,encoder,ciphers', 
  packages=find_packages(),
  install_requires=[''] 
)
