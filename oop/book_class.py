#!/usr/bin/env python3
"""
book_class.py

Defines the Book class with __init__, __del__, __str__, and __repr__ magic methods.
This class is designed to model a book with a title, author, and publication year.
"""

class Book:
    """
    Represents a book with a title, author, and publication year.
    Implements key magic methods for initialization, destruction, and string representation.
    """
    def __init__(self, title, author, year):
        """
        Constructor method. Initializes the Book instance's attributes.
        :param title: The title of the book (str).
        :param author: The author of the book (str).
        :param year: The publication year of the book (int).
        """
        self.title = title
        self.author = author
        self.year = year
        # Optional: Print a message to show creation
        # print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor method. Called when the Book instance is about to be destroyed (garbage collected).
        Prints a message indicating the book being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation method.
        Returns a human-readable, informal string for the object.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation method.
        Returns a string that would allow recreation of the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"