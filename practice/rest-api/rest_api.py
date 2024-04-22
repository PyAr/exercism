import json

class RestAPI:
    user_database = dict()
    get_handlers = dict()
    post_handlers = dict()

    def __init__(self, database=None):
        """
        Initialize the RestAPI with an optional database.

        Args:
            database (dict, optional): The initial user database. Defaults to None.
        """
        self.user_database = database or {'users': []}
        self.get_handlers['/users'] = self.get_users
        self.post_handlers['/add'] = self.add_user
        self.post_handlers['/iou'] = self.add_iou

    def get(self, url, payload=None):
        """
        Handle GET requests.

        Args:
            url (str): The URL for the GET request.
            payload (str, optional): The payload for the GET request. Defaults to None.

        Returns:
            str: The response to the GET request.
        """
        return self.execute_handler(self.get_handlers, url, payload)

    def post(self, url, payload=None):
        """
        Handle POST requests.

        Args:
            url (str): The URL for the POST request.
            payload (str, optional): The payload for the POST request. Defaults to None.

        Returns:
            str: The response to the POST request.
        """
        return self.execute_handler(self.post_handlers, url, payload)

    @staticmethod
    def execute_handler(handlers, url, payload):
        """
        Execute the handler for the given URL.

        Args:
            handlers (dict): Dictionary of handlers.
            url (str): The URL for the request.
            payload (str): The payload for the request.

        Returns:
            str: The response to the request.
        """
        handler = handlers.get(url)
        if not handler:
            raise ValueError(f"No route defined for {url}.")
        return handler(payload)

    def get_users(self, payload):
        """
        Handle GET request for users.

        Args:
            payload (str): The payload for the request.

        Returns:
            str: The response to the request.
        """
        if payload:
            return self.get_named_users(payload)
        else:
            return json.dumps(self.user_database)

    def get_named_users(self, payload):
        """
        Handle GET request for named users.

        Args:
            payload (str): The payload for the request.

        Returns:
            str: The response to the request.
        """
        try:
            names = json.loads(payload)['users']
            names.sort()
        except KeyError:
            raise ValueError("Payload does not contain 'users' key.")
        except Exception as e:
            raise ValueError(f"Error parsing 'users' key of JSON payload as array: {e}")

        users = [user for user in self.user_database['users'] if user['name'] in names]
        return json.dumps({"users": users})

    def add_user(self, payload):
        """
        Handle POST request to add a user.

        Args:
            payload (str): The payload for the request.

        Returns:
            str: The response to the request.
        """
        try:
            name = json.loads(payload)['user']
        except KeyError:
            raise ValueError("Payload does not contain 'user' key.")
        except Exception as e:
            raise ValueError(f"Error parsing 'user' key of JSON payload: {e}")

        if any(user['name'] == name for user in self.user_database['users']):
            raise ValueError(f"User {name} already exists")

        user = self.create_user(name)
        self.user_database['users'].append(user)
        return json.dumps(user)

    @staticmethod
    def create_user(name):
        """
        Create a user with the given name.

        Args:
            name (str): The name of the user.

        Returns:
            dict: The user dictionary.
        """
        return {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}

    def add_iou(self, payload):
        """
        Handle POST request to add an IOU.

        Args:
            payload (str): The payload for the request.

        Returns:
            str: The response to the request.
        """
        try:
            iou = json.loads(payload)
            lender = self.find_user(iou['lender'])
            borrower = self.find_user(iou['borrower'])
            amount = iou['amount']
        except KeyError:
            raise ValueError("Payload is missing required keys.")
        except Exception as e:
            raise ValueError(f"Error parsing JSON payload: {e}")

        if not lender:
            raise ValueError(f"User {iou['lender']} not found.")
        if not borrower:
            raise ValueError(f"User {iou['borrower']} not found.")

        self.adjust_balances(lender, True, borrower['name'], amount)
        lender['balance'] += amount

        self.adjust_balances(borrower, False, lender['name'], amount)
        borrower['balance'] -= amount

        users = [lender, borrower] if lender['name'] < borrower['name'] else [borrower, lender]
        return json.dumps({"users": users})

    def adjust_balances(self, user, user_is_lender, name, amount):
        """
        Adjust balances for a user.

        Args:
            user (dict): The user dictionary.
            user_is_lender (bool): Indicates if the user is the lender.
            name (str): The name of the other party involved.
            amount (float): The amount of the IOU.
        """
        reduce_balance = 'owes' if user_is_lender else 'owed_by'
        increase_balance = 'owed_by' if user_is_lender else 'owes'

        if name in user[reduce_balance]:
            previous_balance = user[reduce_balance][name]
            new_balance = previous_balance - amount
            if amount < previous_balance:
                user[reduce_balance][name] = new_balance
            else:
                del user[reduce_balance][name]
                remainder = -1 * new_balance
                self.increase_named_balance(user[increase_balance], name, remainder)
        else:
            self.increase_named_balance(user[increase_balance], name, amount)

    @staticmethod
    def increase_named_balance(balances, name, amount):
        """
        Increase the named balance.

        Args:
            balances (dict): The balance dictionary.
            name (str): The name of the other party involved.
            amount (float): The amount of the IOU.
        """
        if name in balances:
            new_balance = balances[name] + amount
            if new_balance:
                balances[name] = new_balance
            else:
                del balances[name]
        elif amount:
            balances[name] = amount

    def find_user(self, name):
        """
        Find a user by name.

        Args:
            name (str): The name of the user.

        Returns:
            dict: The user dictionary if found, None otherwise.
        """
        for user in self.user_database['users']:
            if user['name'] == name:
                return user
        return None
