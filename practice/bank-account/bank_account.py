class BankAccount:
    def __init__(self):
        """Initialize a BankAccount object.

        The balance is set to zero and the account status is closed by default.
        """
        self._balance = 0
        self._opened = False

    def _raise_error_if_not_open(self):
        """Raise ValueError if the account is closed."""
        if not self._opened:
            raise ValueError("account not open")

    def _raise_error_if_amount_less_than_0(self, amount):
        """Raise ValueError if the amount is less than zero."""
        if amount < 0:
            raise ValueError("amount must be greater than 0")

    def get_balance(self):
        """Get the current balance of the account.

        Returns:
            int: The current balance of the account.

        Raises:
            ValueError: If the account is closed.
        """
        self._raise_error_if_not_open()
        return self._balance

    def open(self):
        """Open the bank account.

        Raises:
            ValueError: If the account is already open.
        """
        if self._opened:
            raise ValueError("account already open")
        self._opened = True

    def deposit(self, amount):
        """Deposit funds into the bank account.

        Args:
            amount (int): The amount to deposit.

        Raises:
            ValueError: If the account is closed or the amount is negative.
        """
        self._raise_error_if_not_open()
        self._raise_error_if_amount_less_than_0(amount)
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw funds from the bank account.

        Args:
            amount (int): The amount to withdraw.

        Raises:
            ValueError: If the account is closed, the amount is negative,
                        or the withdrawal amount exceeds the balance.
        """
        self._raise_error_if_not_open()
        self._raise_error_if_amount_less_than_0(amount)
        if amount > self._balance:
            raise ValueError("amount must be less than balance")
        self._balance -= amount

    def close(self):
        """Close the bank account and reset the balance to zero.

        Raises:
            ValueError: If the account is already closed.
        """
        self._raise_error_if_not_open()
        self._opened = False
        self._balance = 0
