import setuptools

setuptools.setup(name='reconn',
                 version='0.0.1',
                 description='Stack based toy language',
                 # url='',
                 author='nexustix',
                 author_email='[email protected]',
                 packages=setuptools.find_packages(),
                 scripts=['reconn/reconn'],
                 zip_safe=False)
