from setuptools import setup

setup(name='app',
      version='0.1',
      description='An example Braintree integration for Flask',
      url='http://github.com/braintree/braintree_flask_example',
      author='Braintreeps',
      author_email='code@getbraintree.com',
      license='MIT',
      install_requires=[
          'flask',
          'braintree',
      ],
      zip_safe=False,
)
