cfping
======

Test the performance and availability of the Rackspace cloudfiles or Openstack swift service.


Example
-------

    $ cfping
    Pinging storage (sending request every 1 seconds with 81.0 bytes ):
        seq. #    connect  container     create      write       read     delete      total
             1      0.100      0.061      0.041      0.286      0.009      0.034      0.532
             2      0.068      0.059      0.031      0.168      0.010      0.014      0.351
             3      0.067      0.058      0.027      0.085      0.009      0.013      0.260
             4      0.066      0.059      0.012      0.090      0.009      0.014      0.251
             5      0.066      0.061      0.044      0.052      0.010      0.014      0.247
    ^C
    5 requests


Usage
-----

    usage: cfping [-h] [-u USERNAME] [-k KEY] [-a AUTHURL] [-c CONTAINER] [-s]
                  [-i PING_INTERVAL] [-r PING_REPETITIONS] [-t TEST_DATA_SIZE]

    Test the performance and availability of the Rackspace cloudfiles or Openstack swift service.

    optional arguments:
    -h, --help            show this help message and exit
    -u USERNAME, --username USERNAME
                          Storage service username (default: CFUSER)
    -k KEY, --key KEY     Storage service API key (default: CFKEY)
    -a AUTHURL, --authurl AUTHURL
                          Storage service auth URL (default:
                          https://auth.api.rackspacecloud.com/v1.0)
    -c CONTAINER, --container CONTAINER
                          Use the specified container (default: use the first
                          container [index 0])
    -s, --service-net     Use the Rackspace service network (default: use public
                          network)
    -i PING_INTERVAL, --interval PING_INTERVAL
                          Seconds to wait between ping requests (default: 1
                          seconds)
    -r PING_REPETITIONS, --repetitions PING_REPETITIONS
                          Number of repetitions (default: infinite)
    -t TEST_DATA_SIZE, --test-data-size TEST_DATA_SIZE
                          Test data size in Bytes (default: 81 Bytes)
    -m, --machinereadable
                          Output results with no headers
    -d, --data            Output statistics for the tests, min, max, and average
                          (mean)


Environment
-----------

`cfping` accepts the following environment variables:

* `CFUSER`, the account username. The `-u` option, if provided, takes precedence.
* `CFKEY`, the account key. The `-k` option, if provided, takes precedence.
* `CFAUTHURL`, the authentication endpoint. The `-a` option, if provided, takes precedence.

Installation
------------

`cfping` is a Python program and can be installed with `pip` (or `easy_install`):

    $ pip install cfping


Contributing
------------

`cfping` is open-source software and your contributions are welcome.

Open an [issue](https://github.com/claymation/cfping/issues) on GitHub to report a bug or suggest an enhancement,
or better yet, fork the repo and send a [pull request](https://github.com/claymation/cfping/pulls).
