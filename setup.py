from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='patyczki',
      version='0.0.1',
      description='Simulation of Laplacian network models.',
      url='https://github.com/RadostW/patyczki',
      author='Radost Waszkiewicz & Stanislaw Zukowski',
      author_email='radost.waszkiewicz@gmail.com',
      long_description=long_description,
      long_description_content_type='text/markdown',  # This is important!
      project_urls = {
          'Documentation': 'https://patyczki.readthedocs.io',
          'Source': 'https://github.com/RadostW/patyczki'
      },
      license='MIT',
      install_requires = ['numpy'],
      packages=['patyczki'],
      zip_safe=False)
