cfping
======

Test the performance and availability of the Rackspace cloudfiles service.


Example
-------

    $ cfping
    Pinging Rackspace cloudfiles (sending request every 1 seconds):
        seq. #    connect  container     create      write       read      total
             1      0.448      0.369      0.121      1.331      0.047      2.317
             2      0.345      0.390      0.116      0.375      0.050      1.277
             3      0.671      0.339      0.183      0.239      0.053      1.486
             4      0.341      0.352      0.245      1.541      0.049      2.527
             5      0.360      0.342      0.116      0.900      0.047      1.764
    ^C
    5 requests


Usage
-----

	usage: cfping [-h] [-u USERNAME] [-k KEY] [-a AUTHURL] [-c CONTAINER] [-s]
	              [-i PING_INTERVAL] [-r PING_REPETITIONS]

	Test the performance and availability of the Rackspace cloudfiles service.

	optional arguments:
	  -h, --help            show this help message and exit
	  -u USERNAME, --username USERNAME
	                        Rackspace cloudfiles username (default: CFUSER)
	  -k KEY, --key KEY     Rackspace cloudfiles API key (default: CFKEY)
	  -a AUTHURL, --authurl AUTHURL
	                        Rackspace cloudfiles auth url (default: CFAUTHURL)
	  -c CONTAINER, --container CONTAINER
	                        Use the specified container (default: use the first
	                        container [index 0])
	  -s, --service-net     Use the Rackspace service network (default: use public
	                        network)
	  -i PING_INTERVAL, --interval PING_INTERVAL
	                        Seconds to wait between ping requests (default: 1
	                        seconds)
	  -r PING_REPETITIONS, --repetitions PING_REPETITIONS
	                        Number of repetitions (default: 0 repetitions) default
	                        infinite



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
