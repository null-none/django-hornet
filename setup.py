from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="django-hornet",
    packages=["src"],
    version="0.0.1",
    description="Django Hornet Wrapper",
    url="https://github.com/null-none/django-hornet",
    keywords=["django", "hotnet", "ajax"],
    install_requires=required,
    classifiers=["Programming Language :: Python :: 3"],
    include_package_data=True,
)
