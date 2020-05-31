from typing import Dict, Tuple

from orderedset import OrderedSet

from pyUbiForge2.api.data_types import ForgeFileName, DataFileIdentifier, FileIdentifier, FileIdentifierTriplet

class HistoryManager:
    """A class to track which files have been used recently """
    def __init__(self):
        self._history = OrderedSet()

    def add(self, key: FileIdentifierTriplet):
        """Add a file identifier triplet to the history database.
        If the entry is already in the database it will be moved to the end."""
        if key in self._history:
            self._history.remove(key)  # remove it if it exists so that it can be added to the end
        self._history.add(key)  # add it to the end

    def remove_half(self):
        """Remove half of the files ids and return them"""
