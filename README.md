# Python sample package with data

How to distribute a Python package with data.

https://stackoverflow.com/questions/3596979/manifest-in-ignored-on-python-setup-py-install-no-data-files-installed/60735402#60735402

Tested on Ubuntu 19.10, Python 3.7.5, wheel==0.32.3, setuptools==41.1.0, twine==3.1.1.

How end users use the package from <https://pypi.org/project/python-sample-package-with-data/>:

```
python3 -m pip install --user python-sample-package-with-data
python-sample-package-with-data
```

Expected output:

```
hello data
```

which are the contents of our test data file [python_sample_package_with_data/mydata.txt](python_sample_package_with_data/mydata.txt) that was distributed with `pip`.

How maintainers publish it:

```
# One time setup.
python3 -m pip install --user setuptools wheel twine

# Every time you want to publish.
python setup.py sdist bdist_wheel
twine upload dist/*
rm -rf build dist *.egg-info
```

Bibliography:

- https://stackoverflow.com/questions/47577762/how-do-i-distribute-my-pip-package-with-data-files-correctly
- https://stackoverflow.com/questions/47817944/python-pkg-resources-and-file-access-in-packages
- https://stackoverflow.com/questions/39104/finding-a-file-in-a-python-module-distribution
- https://stackoverflow.com/questions/14211575/any-python-function-to-get-data-files-root-directory
- https://stackoverflow.com/questions/14422340/manifest-in-package-data-and-data-files-clarification
- https://stackoverflow.com/questions/11235820/setup-py-not-installing-data-files
