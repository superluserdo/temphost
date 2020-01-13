from setuptools import setup, find_packages

setup(name='temphost',
    version='0.2.0',
    scripts=['temphost'],
    data_files = [
            ('share/temphost', ['index.html.template', 'style.css'])
            ],
    )
