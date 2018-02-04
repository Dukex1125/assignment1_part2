#! usr/bin/env
# -*- coding: utf-8 -*-
"""A review of a simple class."""


class Book(object):
    """Object that stores Book data.

    """
    def __init__(self, author, title):
        """Constructor for the Book class.

        Args:
            author (str): name of the author.
            title (str): name of the title.

        Attributes:
            author (str): name of the author.
            title (str): name of the title.
        """
        self.author = author
        self.title = title


    def display(self):
        """displays the book title and name of author.

        Returns:
            mixed: the data of the parameters.

        Example:
            >>>book1 = Book('John Steinbeck', 'Of Mice and Men')
            >>>book1.display()
            Of Mice and Men written by John Steinbeck
        """
        print self.title, 'written by', self.author

book1 = Book('John Steinbeck', 'Of Mice and Men')
book2 = Book('Harper Lee', 'To Kill A Mockingbird')

book1.display()
book2.display()