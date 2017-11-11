from setuptools import setup, find_packages

setup(name='home-assistant-frontend',
      version='20171110.0',
      description='The Home Assistant frontend',
      url='https://github.com/home-assistant/home-assistant-polymer',
      author='The Home Assistant Authors',
      author_email='hello@home-assistant.io',
      license='Apache License 2.0',
      packages=find_packages(include=['hass_frontend', 'hass_frontend_es5', 'hass_frontend.*', 'hass_frontend_es5.*']),
      include_package_data=True,
      zip_safe=False)