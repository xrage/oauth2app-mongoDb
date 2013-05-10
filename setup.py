from setuptools import setup, find_packages

requirements = [l.strip() for l in open('requirements.txt').readlines()]


setup(
    name="oauth2app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,

    # metadata for upload to PyPI
    author="Dharmendra Verma",
    author_email="dkverma.vit@gmail.com",
    description="Django OAuth 2.0 Server App based MongoDb powered app",
    license="MIT License",
    keywords="django oauth2 mongodb oauth app server django nonrel",
    url="https://github.com/dkvermavit/oauth2app-mongoDb",
)
