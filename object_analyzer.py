
"""Provides tools for dynamically analyzing Python objects."""
import inspect
from typing import Any


class ObjectAnalyzer:
    """
    A utility class for dynamically analyzing Python objects.

    Provides methods for retrieving information about an object's
    type, attributes, methods, inheritance hierarchy, and documentation.

    Also supports dynamic attribute retrieval and modification.
    """

    def get_type(self, obj: Any) -> str:
        """
        Return the name of the object's type.

        Args:
            obj (Any): The object to analyze.

        Returns:
            str: The name of the object's type.
        """
        return type(obj).__name__

    def get_attributes(self, obj: Any) -> list[str]:
        """
        Retrieve non-callable attributes of an object.

        Iterates over the names returned by dir(), excluding attributes
        whose names start with double underscores and attributes
        whose values are callable.

        Args:
            obj (Any): The object to inspect.

        Returns:
            list[str]: A list of non-callable attribute names.
        """
        filtered_attributes = []
        for attribute in dir(obj):
            if attribute.startswith("__"):
                continue

            value = getattr(obj, attribute)

            if callable(value):
                continue

            filtered_attributes.append(attribute)

        return filtered_attributes

    def get_methods(self, obj: Any) -> dict[str, str]:
        """
        Retrieve callable attributes and their signatures.

        Iterates over the object's attributes, excluding names
        starting with double underscores and non-callable values.

        Uses inspect.signature() to obtain method signatures.
        Callable attributes with unavailable signatures are skipped.

        Args:
            obj (Any): The object to inspect.

        Returns:
            dict[str, str]: A dictionary mapping callable attribute
                names to their string representations of signatures.
        """
        methods = {}
        for attribute in dir(obj):
            if attribute.startswith("__"):
                continue

            value = getattr(obj, attribute)

            if not callable(value):
                continue

            try:
                signature = str(inspect.signature(value))
                methods[attribute] = signature
            except (TypeError, ValueError):
                continue

        return methods

    def get_inheritance(self, obj: Any) -> list[str]:
        """
        Retrieve the object's class inheritance hierarchy.

        Uses the Method Resolution Order (MRO) to determine
        the sequence of classes Python searches when resolving
        attributes and methods.

        Args:
            obj (Any): The object to inspect.

        Returns:
            list[str]: A list of class names in MRO order,
                including the object's class and its base classes.
        """
        inheritance = []

        for item in type(obj).__mro__:
            inheritance.append(item.__name__)

        return inheritance

    def get_documentation(self, obj: Any) -> str | None:
        """
        Retrieve the documentation associated with an object.

        Uses inspect.getdoc() to retrieve and normalize
        the object's documentation string.

        Args:
            obj (Any): The object to inspect.

        Returns:
            str | None: The object's documentation string,
                or None if documentation is unavailable.
        """
        return inspect.getdoc(obj)

    def get_attribute(self, obj: Any, name: str) -> Any:
        """
        Retrieve an attribute value dynamically by its name.

        Uses getattr() to access the specified attribute.
        Returns None if the attribute does not exist.

        Args:
            obj (Any): The object containing the attribute.
            name (str): The name of the attribute to retrieve.

        Returns:
            Any: The attribute value, or None if it does not exist.
        """
        return getattr(obj, name, None)

    def set_attribute(
        self, obj: Any, name: str, value: Any
    ) -> None:
        """
        Set or update an attribute dynamically.

        Uses setattr() to assign a value to an existing attribute
        or create a new attribute if the object supports it.

        Args:
            obj (Any): The object to modify.
            name (str): The name of the attribute to set.
            value (Any): The value to assign.

        Returns:
            None: This method does not return a value.
        """
        setattr(obj, name, value)

    def analyze(self, obj: Any) -> dict[str, Any]:
        """
        Generate a structured analysis report for an object.

        Combines the results of the type, attribute, method,
        inheritance, and documentation analysis methods
        into a single dictionary.

        Args:
            obj (Any): The object to analyze.

        Returns:
            dict[str, Any]: A dictionary containing:
                - type: The object's type name.
                - attributes: Non-callable attribute names.
                - methods: Callable attributes and signatures.
                - inheritance: Class names in MRO order.
                - documentation: The object's documentation.
        """
        report = {}

        report["type"] = self.get_type(obj)
        report["attributes"] = self.get_attributes(obj)
        report["methods"] = self.get_methods(obj)
        report["inheritance"] = self.get_inheritance(obj)
        report["documentation"] = self.get_documentation(obj)

        return report
