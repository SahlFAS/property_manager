from setuptools import setup, find_packages

setup(
    name='property_manager',
    version='1.0.0',
    description='Custom app for property unit management',
    author='SahlFAS',
    author_email='support@sahl-tech.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe'],
)

