from setuptools import setup

exec(open('gremlin/__version__.py').read())

# Use the README as the long_description
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='gremlin',
    version=__version__,
    packages=['gremlin'],
    scripts=['gremlin/gremlin.py'],
    # entry_points={
    #     'console_scripts': [
    #         'gremlin = gremlin.gremlin:client'
    #     ],
    # },
    url='https://github.com/markcoletti/gremlin',
    license='MIT License',
    author='Mark Coletti',
    author_email='colettima@ornl.gov',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description=('Adversarial evolutionary algorithm for'
                 'training data optimization')
)
