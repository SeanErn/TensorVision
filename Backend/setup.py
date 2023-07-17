from setuptools import setup

setup(name='tfForCo_Backend',
      version='0.1',
      description='Backend for tfForCo',
      setup_requires=[
        'tornado',
        'opencv-python',
        'tensorflow',
        'PyMongo'
      ]
)