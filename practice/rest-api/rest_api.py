"""
The RestAPI class provides a simple RESTful API interface for managing user data. Here's an overview of the approach:

1. **Class Structure**:
    - The class maintains a `user_database` dictionary to store user data.
    - Separate dictionaries `get_handlers` and `post_handlers` are used to map URLs to corresponding handler methods.

2. **Initialization**:
    - In the `__init__` method, the user-provided database (if any) is assigned to `user_database`.
    - Default handlers for GET and POST requests are set for the `/users`, `/add`, and `/iou` endpoints.

3. **GET and POST Handling**:
    - The `get` and `post` methods handle HTTP GET and POST requests respectively by delegating to the `execute_handler` method.
    - The `execute_handler` method retrieves the appropriate handler function for the given URL from the corresponding dictionary.

4. **Handler Execution**:
    - The handler functions defined for various endpoints process the requests and return the appropriate responses.
    - Handlers are responsible for validating input, performing operations on the user database, and generating responses.

5. **User Management**:
    - The `get_users`, `get_named_users`, and `add_user` methods handle user-related requests.
    - `get_users` returns a JSON string of all users or filtered users based on provided names.
    - `add_user` adds a new user to the database if it doesn't already exist.
    - `get_named_users` filters users based on provided names.

6. **IOU Management**:
    - The `add_iou` method handles IOU-related requests.
    - It parses the payload to extract lender, borrower, and amount information.
    - It adjusts balances for both lender and borrower accordingly and updates the user database.
    - The method ensures that both lender and borrower exist in the database before proceeding.

7. **Balances Adjustment**:
    - The `adjust_balances` method updates balances for a user after an IOU is added.
    - It determines the appropriate balance types (`owes` or `owed_by`) based on whether the user is the lender or borrower.
    - It adjusts balances and handles cases where previous balances need to be cancelled or reduced.

8. **Error Handling**:
    - Various exceptions are raised to handle error conditions such as missing keys in payload, user not found, etc.
    - Exceptions provide informative error messages to aid in debugging and troubleshooting.

9. **Utility Methods**:
    - Utility methods like `create_user`, `increase_named_balance`, and `find_user` are used to perform common tasks in a modular manner.
    
"""

import json

class RestAPI():
    user_database = dict()
    get_handlers = dict()
    post_handlers = dict()

    def __init__(self, database=None):
        self.user_database = database
        self.get_handlers['/users'] = self.get_users
        self.post_handlers['/add'] = self.add_user
        self.post_handlers['/iou'] = self.add_iou

    def get(self, url, payload=None):
        return self.execute_handler(self.get_handlers, url, payload)

    def post(self, url, payload=None):
        return self.execute_handler(self.post_handlers, url, payload)

    @staticmethod
    def execute_handler(handlers, url, payload):
        handler = handlers.get(url)
        if not handler:
            raise ValueError(f"No route defined for {url}.")
        return handler(payload)

    def get_users(self, payload):
        if payload:
            return self.get_named_users(payload)
        else:
            return json.dumps(self.user_database)

    def get_named_users(self, payload):
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
        return {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}

    def add_iou(self, payload):
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
        if name in balances:
            new_balance = balances[name] + amount
            if new_balance:
                balances[name] = new_balance
            else:
                del balances[name]
        elif amount:
            balances[name] = amount

    def find_user(self, name):
        for user in self.user_database['users']:
            if user['name'] == name:
                return user
        return None

