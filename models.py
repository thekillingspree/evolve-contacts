class Contact:
  """
  A class representing a contact.

  Attributes:
  -----------
  name : str
    The name of the contact.
  phone : str
    The phone number of the contact.
  email : str
    The email address of the contact.
  address : str
    The address of the contact.
  """

  def __init__(self, name, phone="", email="", address=""):
    """
    Initializes a new instance of the Contact class.

    Parameters:
    -----------
    name : str
      The name of the contact.
    phone : str, optional
      The phone number of the contact. Default is an empty string.
    email : str, optional
      The email address of the contact. Default is an empty string.
    address : str, optional
      The address of the contact. Default is an empty string.
    """
    self.name = name
    self.phone = phone
    self.email = email
    self.address = address

  @staticmethod
  def prettify(contacts):
    """
    Returns a prettified string of a given list of Contacts

    Parameters:
    -----------
    contacts : Contact[]
      The list of contacts to print.

    Returns:
    --------
    str
      A prettified string representation of the contacts in the list.
    """
     
    print(f"\nContacts\nTotal Contacts: {len(contacts)}:")
    print("-----------------")

    return "\n-----------------\n".join([str(contact) for contact in contacts])

  def __str__(self):
    """
    Returns a string representation of the Contact object.

    Returns:
    --------
    str
      A string representation of the Contact object.
    """
    return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n-----------------\n"

