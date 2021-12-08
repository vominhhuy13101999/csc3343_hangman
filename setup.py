from distutils.core import setup, Extension
# import setuptools 
# description='hang man game',
# author='Huy Vo',
# author_email='huy.vo@student.fairfield.edu',
setup(name='search', version='1.0',  \
      ext_modules=[Extension('search', ['python.cpp'])],
      install_requires=[
        # 'wheel',
        'pandas',
        'pygame',
        
        
    ])

# setup(name='spam', version='1.0',  \
#       ext_modules=[Extension('spam', ['hello.cpp'])])

# setuptools.setup(
#     name='hangman',
#     version='0.0.1',
    
#     packages=setuptools.find_packages(),
#     install_requires=[
#         # 'wheel',
#         'pandas',
#         'pygame',
        
        
#     ],
# )