import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

pkgs = setuptools.find_packages()
print('found these packages:', pkgs)

pkg_name="ml_ms4alg"

setuptools.setup(
    name=pkg_name,
    version="0.2.1",
    author="Jeremy Magland",
    author_email="",
    description="Mountainsort v4 for MountainLab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/magland/ml_ms4alg",
    packages=pkgs,
    package_data={
        '': ['*.mp'], # Include all processor files
    },
    install_requires=
    [
        'pybind11',
        'isosplit5',
        'numpy',
#        'mountainlab_pytools',
        'h5py',
        'sklearn',
        'spikeextractors'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    )
)
