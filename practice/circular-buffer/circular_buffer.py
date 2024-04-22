class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""
    def __init__(self, message):
        """
        Initialize BufferFullException.

        Args:
            message (str): Explanation of the error.
        """
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""
    def __init__(self, message):
        """
        Initialize BufferEmptyException.

        Args:
            message (str): Explanation of the error.
        """
        self.message = message


class CircularBuffer:
    """Simulates a circular buffer data structure."""

    def __init__(self, capacity):
        """
        Initialize CircularBuffer.

        Args:
            capacity (int): The maximum capacity of the buffer.
        """
        self.capacity = capacity
        self.store = []

    def read(self):
        """
        Read data from the buffer.

        Returns:
            Any: The data read from the buffer.

        Raises:
            BufferEmptyException: If the buffer is empty.
        """
        if len(self.store) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        out = self.store[0]
        self.store.remove(out)
        return out   

    def write(self, data):
        """
        Write data to the buffer.

        Args:
            data (Any): The data to be written to the buffer.

        Raises:
            BufferFullException: If the buffer is full.
        """
        if len(self.store) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.store.append(data)

    def overwrite(self, data):
        """
        Overwrite data in the buffer.

        Args:
            data (Any): The data to overwrite in the buffer.
        """
        if len(self.store) == self.capacity:
            self.store = self.store[1:] + [data]
        else:
            self.store.append(data)

    def clear(self):
        """Clear the buffer."""
        self.store = []
