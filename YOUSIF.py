=== stderr ===

Traceback (most recent call last):
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/connection.py", line 200, in _new_conn
    sock = connection.create_connection(
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/usr/local/python-3.8.1/lib/python3.8/socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -3] Temporary failure in name resolution

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/connectionpool.py", line 790, in urlopen
    response = self._make_request(
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/connectionpool.py", line 491, in _make_request
    raise new_e
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/connectionpool.py", line 467, in _make_request
    self._validate_conn(conn)
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/connectionpool.py", line 1092, in _validate_conn
    conn.connect()
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/connection.py", line 604, in connect
    self.sock = sock = self._new_conn()
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/connection.py", line 207, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
urllib3.exceptions.NameResolutionError: <urllib3.connection.HTTPSConnection object at 0x7f6410390940>: Failed to resolve 'raw.githubusercontent.com' ([Errno -3] Temporary failure in name resolution)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/requests/adapters.py", line 486, in send
    resp = conn.urlopen(
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/connectionpool.py", line 844, in urlopen
    retries = retries.increment(
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/urllib3/util/retry.py", line 515, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='raw.githubusercontent.com', port=443): Max retries exceeded with url: /Ramxantanha/data/main/strings.txt (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7f6410390940>: Failed to resolve 'raw.githubusercontent.com' ([Errno -3] Temporary failure in name resolution)"))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "script.py", line 29, in <module>
    xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/requests/sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/requests/sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/python-3.8.1/lib/python3.8/site-packages/requests/adapters.py", line 519, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='raw.githubusercontent.com', port=443): Max retries exceeded with url: /Ramxantanha/data/main/strings.txt (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7f6410390940>: Failed to resolve 'raw.githubusercontent.com' ([Errno -3] Temporary failure in name resolution)"))


=== message ===

Exited with error status 1
