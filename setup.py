from setuptools import setup

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(name                 ='SIAC',
      version              ='2.0.0',
      description          = 'A sensor invariant Atmospheric Correction (SIAC)',
      long_description     = readme,
      author               = 'Feng Yin',
      author_email         = 'ucfafyi@ucl.ac.uk',
      classifiers          = ['Development Status :: 4 - Beta',
                              'Programming Language :: Python :: 2.7',
                              'Programming Language :: Python :: 3.6'],
      install_requires     = ['gdal>=2.1, <2.3', 'numpy>=1.13', 'scipy>=1.0', 'psutil','six',
                              'lightgbm>=2.1.0','requests', 'scikit-learn', 'scikit-image', 'gp_emulator>=1.6.0'],
      url                  = 'https://github.com/MarcYin/SIAC',
      license              = "GNU Affero General Public License v3.0",
      include_package_data = True,
      packages             = ['SIAC'],
     )