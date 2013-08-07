from setuptools import setup

setup(
    name = "cfping",
    version = "0.2.0",
    description = "Test the performance and availability of the Rackspace cloudfiles or Openstack swift service.",
    author = "Clay McClure",
    author_email = "clay@daemons.net",
    url = "https://github.com/claymation/cfping",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Monitoring',
    ],
    scripts = ['cfping'],
    install_requires = [
        'python-cloudfiles',
    ],
)
