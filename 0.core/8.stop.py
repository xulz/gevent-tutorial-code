import gevent
import signal

def run_forever():
    gevent.sleep(1000)

if __name__ == '__main__':
    # # seems gevent.shutdown has been removed
    gevent.signal(signal.SIGQUIT, gevent.shutdown)
    thread = gevent.spawn(run_forever)
    thread.join()
