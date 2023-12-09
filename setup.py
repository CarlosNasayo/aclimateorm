from setuptools import setup, find_packages

setup(
    name="aclimate_orm",
    version='0.0.0',
    author="stevensotelo",
    author_email="h.sotelo@cgiar.com",
    description="orm for aclimate",
    url="https://github.com/CIAT-DAPA/aclimate_orm",
    download_url="https://github.com/CIAT-DAPA/aclimate_orm",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='mongodb orm aclimate',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "mongoengine==0.26.0"
    ]
)
