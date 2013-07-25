#!/usr/bin/env python -u

"""
cloudfiles-ping: Test the performance and availability of the Rackspace cloudfiles service.
"""

import argparse
import contextlib
import time
import uuid

import cloudfiles


DEFAULT_PING_INTERVAL = 1
TEST_DATA = 'The quick brown fox jumps over the lazy dog.'


@contextlib.contextmanager
def timer():
    """
    Time an operation.
    """
    start_time = time.time()
    yield
    end_time = time.time()

    elapsed_time = end_time - start_time

    print '%10.3f' % (elapsed_time),

    
def ping(username, api_key, container=None, use_service_net=False):
    """
    Ping the Rackspace cloudfiles service, printing the elapsed time for a connection, a write, and a read.
    """

    try:
        with timer():

            with timer():
                conn = cloudfiles.get_connection(username, api_key, servicenet=use_service_net)

            with timer():
                if container is None:
                    # Get first container
                    container = conn.get_all_containers()[0]
                else:
                    container = conn.get_container(container)

            obj_name = str(uuid.uuid4())

            with timer():
                obj = container.create_object(obj_name)

            with timer():
                obj.write(TEST_DATA)

            with timer():
                result = obj.read()

        if result != TEST_DATA:
            print '%10s' % ('NOMATCH'),

    except KeyboardInterrupt:
        raise
    except Exception, e:
        print '%10s (%s)' % ('*', e),

    print


def ping_forever(username, api_key,
                 container=None, use_service_net=False, ping_interval=DEFAULT_PING_INTERVAL):
    """
    Continually ping the Rackspace cloudfiles service, sleeping for `ping_interval` seconds between requests.
    """
    print 'Pinging Rackspace cloudfiles (sending request every %d seconds):' % ping_interval
    print '%10s %10s %10s %10s %10s %10s %10s' % ('seq. #', 'connect', 'container', 'create', 'write', 'read', 'total')

    request_count = 0

    try:

        while True:
            print '%10d' % (request_count + 1), 
            ping(username, api_key, container=container, use_service_net=use_service_net)
            request_count += 1
            time.sleep(ping_interval)

    except KeyboardInterrupt:
        print
        print '%d requests' % request_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test the performance and availability of the Rackspace cloudfiles service.')

    parser.add_argument('username', help='Rackspace cloudfiles username')
    parser.add_argument('api_key', help='Rackspace cloudfiles API key')

    parser.add_argument('-c', '--container',
                       help='Use the specified container (default: use the first container [index 0])')
    parser.add_argument('-s', '--service-net', dest="use_service_net", action='store_true',
                       help='Use the Rackspace service network (default: use public network)')
    parser.add_argument('-i', '--interval', dest='ping_interval', type=int, default=DEFAULT_PING_INTERVAL,
                       help='Seconds to wait between ping requests (default: %d seconds)' % DEFAULT_PING_INTERVAL)

    args = parser.parse_args()

    ping_forever(args.username, args.api_key,
                 container=args.container,
                 use_service_net=args.use_service_net,
                 ping_interval=args.ping_interval)
