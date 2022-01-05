from setuptools import setup

setup(name='cbpi4-MashHoldStep',
      version='0.0.1',
      description='CraftBeerPi Plugin',
      author='Wobbly',
      author_email='neil@milne.com',
      url='',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-MashHoldStep': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-MashHoldStep'],
     )