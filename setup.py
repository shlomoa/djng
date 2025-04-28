import os
import re
import shutil
import sys
from io import open

from setuptools import find_packages, setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 11)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================

This version of djng requires Python {}.{}, but you're trying
to install it on Python {}.{}.

This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:

    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install djng

This will install the latest version of djng which works on
your version of Python. If you can't upgrade your pip (or Python), request
an older version of djng:

    $ python -m pip install "djng<3.10"
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)


def read(f):
    with open(f, 'r', encoding='utf-8') as file:
        return file.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('djng')


if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    if os.system("twine check dist/*"):
        print("twine check failed. Packages might be outdated.")
        print("Try using `pip install -U twine wheel`.\nExiting.")
        sys.exit()
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('djng.egg-info')
    sys.exit()


setup(
    name='djng',
    version=version,
    url='https://www.lightmoneysw.com/',
    license='BSD',
    description='Django Angular integration.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Shlomo Anglister',
    author_email='shlomoa@lightmoneysw.com',  # SEE NOTE BELOW (*)
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=["django>=5.1", 'djangorestframework>=3.15', 'django-filter', "drf_spectacular>=0.28", 'backports.zoneinfo;python_version<"3.9"'],
    python_requires=">=3.11",
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5.0',
        'Framework :: Django :: 5.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    project_urls={
        'Funding': 'https://www.lightmoneysw.com/',
        'Source': 'https://github.com/shlomoa/djng',
        'Changelog': 'https://www.github.com/shlomoa/djng/CHANGELOG.md',
    },
)

