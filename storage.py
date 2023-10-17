import pickle
from abc import ABC, abstractmethod

class BaseStorage(ABC):
  """
  Abstract base class for storage classes.
  """

  @abstractmethod
  def save(self, obj):
    """
    Save an object to storage.

    Args:
      obj: The object to save.
    """
    pass

  @abstractmethod
  def load(self):
    """
    Load an object from storage.

    Returns:
      The loaded object.
    """
    pass


class PickleStorage(BaseStorage):
  """
  A class for storing and loading objects using the pickle module.
  """

  def __init__(self, path):
    """
    Initializes a PickleStorage object with the given file path.

    Args:
      path (str): The file path to store the object.
    """
    self.path = path

  def save(self, obj):
    """
    Saves the given object to the file path specified in the constructor.

    Args:
      obj (object): The object to be saved.
    """
    with open(self.path, 'wb') as f:
      pickle.dump(obj, f)

  def load(self):
    """
    Loads the object from the file path specified in the constructor.

    Returns:
      object: The loaded object.
    """
    with open(self.path, 'rb') as f:
      return pickle.load(f)

