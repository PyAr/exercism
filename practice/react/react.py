class InputCell:
    def __init__(self, initial_value):
        """
        Initialize an InputCell.

        Args:
            initial_value: The initial value of the InputCell.
        """
        self._value = initial_value
        self._observers = set()

    @property
    def value(self):
        """
        Getter for the value property.

        Returns:
            The current value of the InputCell.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Setter for the value property.

        Args:
            new_value: The new value to be set.
        """
        self._value = new_value
        # Notify observers upon value change
        for observer in self._observers:
            observer.compute()

    def register_observer(self, observer):
        """
        Register an observer for this InputCell.

        Args:
            observer: The observer to be registered.
        """
        self._observers.add(observer)

    def compute(self):
        """
        Placeholder method for computing the value of InputCell.
        """
        pass


class ComputeCell:
    def __init__(self, inputs, compute_function):
        """
        Initialize a ComputeCell.

        Args:
            inputs: The list of InputCells that this ComputeCell depends on.
            compute_function: The function used to compute the value based on inputs.
        """
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = set()
        self._value = None
        self._start_observing_ultimate_observables()
        self.compute()

    @property
    def value(self):
        """
        Getter for the value property.

        Returns:
            The current value of the ComputeCell.
        """
        return self._value

    @value.setter
    def value(self, computed_value):
        """
        Setter for the value property.

        Args:
            computed_value: The new computed value to be set.
        """
        self._value = computed_value
        # Notify callbacks upon value change
        for callback in self.callbacks:
            callback(self.value)

    def add_callback(self, callback):
        """
        Add a callback function to be called when the value changes.

        Args:
            callback: The callback function to be added.
        """
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        """
        Remove a callback function.

        Args:
            callback: The callback function to be removed.
        """
        self.callbacks.discard(callback)

    def _start_observing_ultimate_observables(self):
        """
        Start observing ultimate observables in the input hierarchy.
        """
        def ultimate_observables(inputs):
            for input_ in inputs:
                if isinstance(input_, ComputeCell):
                    yield from ultimate_observables(input_.inputs)
                else:  # InputCell
                    yield input_

        for ultimate_observable in ultimate_observables(self.inputs):
            ultimate_observable.register_observer(self)

    def compute(self):
        """
        Compute the value based on inputs and compute function.
        """
        for input_ in self.inputs:
            input_.compute()
        computed_value = self.compute_function([input_.value for input_ in self.inputs])
        # Update value if computed value differs
        if computed_value != self.value:
            self.value = computed_value
