import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

_version_="0.0.0"

REPO_NAME = "satellite_image_classification"
AUTHOR_USER_NAME = "manishiitmandi"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "kmanish1773@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small python package for cnn app",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)