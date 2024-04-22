import io


class MeteredFile(io.BufferedRandom):
    """
    Measure I/O operations performed on files.

    Attributes:
        _read_ops (int): Number of read operations.
        _write_ops (int): Number of write operations.
        _read_bytes (int): Number of bytes read.
        _write_bytes (int): Number of bytes written.
    """

    def __init__(self, *args, **kwargs):
        """Initialize MeteredFile."""
        super().__init__(*args, **kwargs)
        self._read_ops = 0
        self._write_ops = 0
        self._read_bytes = 0
        self._write_bytes = 0

    def __enter__(self):
        """Enter context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager."""
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        """Iterator."""
        return self

    def __next__(self):
        """Next iterator."""
        line = super().readline()
        self._read_ops += 1
        self._read_bytes += len(line)
        if line:
            return line
        raise StopIteration()

    def read(self, size=-1):
        """Read from file."""
        buf = super().read(size)
        self._read_ops += 1
        self._read_bytes += len(buf)
        return buf

    @property
    def read_bytes(self):
        """Get number of bytes read."""
        return self._read_bytes

    @property
    def read_ops(self):
        """Get number of read operations."""
        return self._read_ops

    def write(self, b):
        """Write to file."""
        bytes_written = super().write(b)
        self._write_ops += 1
        self._write_bytes += bytes_written
        return bytes_written

    @property
    def write_bytes(self):
        """Get number of bytes written."""
        return self._write_bytes

    @property
    def write_ops(self):
        """Get number of write operations."""
        return self._write_ops


class MeteredSocket:
    """
    Measure I/O operations performed on sockets.

    Attributes:
        _recv_ops (int): Number of receive operations.
        _send_ops (int): Number of send operations.
        _recv_bytes (int): Number of bytes received.
        _send_bytes (int): Number of bytes sent.
        _socket: The underlying socket object.
    """

    def __init__(self, socket):
        """Initialize MeteredSocket."""
        self._recv_ops = 0
        self._send_ops = 0
        self._recv_bytes = 0
        self._send_bytes = 0
        self._socket = socket

    def __enter__(self):
        """Enter context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager."""
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        """Receive data from the socket."""
        self._recv_ops += 1
        received_data = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(received_data)
        return received_data

    @property
    def recv_bytes(self):
        """Get number of bytes received."""
        return self._recv_bytes

    @property
    def recv_ops(self):
        """Get number of receive operations."""
        return self._recv_ops

    def send(self, data, flags=0):
        """Send data through the socket."""
        self._send_ops += 1
        bytes_sent = self._socket.send(data, flags)
        self._send_bytes += bytes_sent
        return bytes_sent

    @property
    def send_bytes(self):
        """Get number of bytes sent."""
        return self._send_bytes

    @property
    def send_ops(self):
        """Get number of send operations."""
        return self._send_ops
