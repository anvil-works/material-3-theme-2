from ._anvil_designer import DividerTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Divider(DividerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  @property
  def type(self):
    return self._type

  @type.setter
  def type(self, value):
    divider = self.dom_nodes['anvil-m3-divider']
    self._type = value
    value = value.lower().replace(' ', '-')
    divider.className = "anvil-m3-divider"
    self.dom_nodes['anvil-m3-divider'].classList.add(value)


