import gevent


def _iter():
    while True:
        gevent.sleep(1)
        yield 1


def test():
    for i in _iter():
        print(i)


gevent.joinall([
    gevent.spawn(test)
])
