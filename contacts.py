
from models import Contact
from storage import PickleStorage

class ContactBook:
  """
  A class representing a contact book.

  Attributes:
  -----------
  storage : BaseStorage
    An instance of BaseStorage to store and retrieve contacts.
  verbose : bool
    A boolean flag to indicate whether to print debug log messages or not.

  Methods:
  --------
  load_contacts()
    Loads contacts from storage.
  save_contacts()
    Saves contacts to storage.
  has_contact(name: str) -> bool
    Checks if a contact with the given name exists in the contact book.
  add_contact(contact: Contact)
    Adds a new contact to the contact book.
  search_contact(query: str)
    Searches for contacts in the contact book based on the given query.
  get_contact(name: str) -> Contact
    Returns the contact with the given name.
  update_contact(name: str, contact: Contact)
    Updates the contact with the given name.
  delete_contact(name: str)
    Deletes the contact with the given name.
  __str__() -> str
    Returns a string representation of the contact book.
  """
  def __init__(self, storage, verbose=False):
    """
    Initializes a new instance of ContactBook class.

    Parameters:
    -----------
    storage : PickleStorage
      An instance of PickleStorage class to store and retrieve contacts.
    verbose : bool, optional
      A boolean flag to indicate whether to print log messages or not. Default is False.
    """
    self._contacts = {}
    self.storage = storage
    self.verbose = verbose
    self.load_contacts()

  def _log(self, message):
    """
    Prints the given message if verbose flag is True.

    Parameters:
    -----------
    message : str
      The message to be printed.
    """
    if self.verbose:
      print(message)

  def load_contacts(self):
    """
    Loads contacts from storage.
    """
    try:
      self._contacts = self.storage.load()
      self._log("-- Contacts loaded from storage --")
    except:
      self._log("-- Contacts not loaded from storage --")
      self._contacts = {}

  def save_contacts(self):
    """
    Saves contacts to storage.
    """
    self.storage.save(self._contacts)
    self._log("-- Contacts saved to storage --")

  def has_contact(self, name):
    """
    Checks if a contact with the given name exists in the contact book.

    Parameters:
    -----------
    name : str
      The name of the contact to be checked.

    Returns:
    --------
    bool
      True if a contact with the given name exists, False otherwise.
    """
    return name in self._contacts

  def add_contact(self, contact):
    """
    Adds a new contact to the contact book.

    Parameters:
    -----------
    contact : Contact
      The contact to be added.
    """
    self._contacts[contact.name] = contact

  def search_contact(self, query):
    """
    Searches for contacts in the contact book based on the given query.

    Parameters:
    -----------
    query : str
      The query to be used for searching.

    Returns:
    --------
    Contact[]
    """
    results = []

    query = query.lower()
    for contact_name in self._contacts:
      contact = self._contacts[contact_name]
      if query in contact_name.lower() or query in contact.phone.lower() or query in contact.email.lower() or query in contact.address.lower():
        results.append(self._contacts[contact_name])

    return results
  
  def get_contact(self, name):
    """
    Returns the contact with the given name.

    Parameters:
    -----------
    name : str
      The name of the contact to be returned.

    Returns:
    --------
    Contact
      The contact with the given name.

    Raises:
    -------
    ValueError
      If a contact with the given name does not exist.
    """
    if name not in self._contacts:
      raise ValueError(f"Contact {name} not found")
    return self._contacts[name]
  
  def update_contact(self, name, contact):
    """
    Updates the contact with the given name.

    Parameters:
    -----------
    name : str
      The name of the contact to be updated.
    contact : Contact
      The updated contact.

    Raises:
    -------
    ValueError
      If a contact with the given name does not exist.
    """
    if name not in self._contacts:
      raise ValueError(f"Contact {name} not found")
    self._contacts[name] = contact
  
  def delete_contact(self, name):
    """
    Deletes the contact with the given name.

    Parameters:
    -----------
    name : str
      The name of the contact to be deleted.

    Raises:
    -------
    ValueError
      If a contact with the given name does not exist.
    """
    if name not in self._contacts:
      raise ValueError(f"Contact {name} not found")
    del self._contacts[name]
  
  def __str__(self):
    """
    Returns a string representation of the contact book.

    Returns:
    --------
    str
      A string representation of the contact book.
    """
    return Contact.prettify(self._contacts.values())
  
# Storage singleton - Pickle based 
storage = PickleStorage("contacts.pickle")
# ContactBook singleton 
contact_book_manager = ContactBook(storage)
