from distutils.core import setup

setup(
    name='MPyDATA',
    version='0.0.0',
    packages=[
        'MPyDATA',
        'MPyDATA/formulae',
        'MPyDATA/utils',
        'MPyDATA/arakawa_c',
        'MPyDATA/arakawa_c/impl',
        'MPyDATA/arakawa_c/boundary_conditions'
    ],
    license='GPL v3',
    long_description=''
)
