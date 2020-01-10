from setuptools import setup, find_packages

setup(name='temphost',
    version='0.1.0',
    scripts=['temphost'],
    data_files = [
            ('share/temphost', ['index.html.template', 'style.css'])
            ],
    #packages=find_packages(),
    #include_package_data=True,
    )
