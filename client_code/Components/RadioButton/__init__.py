from ._anvil_designer import RadioButtonTemplate
from anvil import *
from ...Functions import checked_property, innerText_property, name_property

class RadioButton(RadioButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  selected = checked_property('anvil-m3-radiobutton')
  group_name = name_property('anvil-m3-radiobutton')
  label = innerText_property('anvil-m3-radiobutton-label')

  @property
  def enabled(self):
    return self._enabled

  @enabled.setter
  def enabled(self, value):
    self.dom_nodes['anvil-m3-radiobutton'].disabled = not value

  # create event listener and add that when anywhere in the container is clicked, it changes it to selected