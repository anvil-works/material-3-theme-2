from ._anvil_designer import RadioButtonTemplate
from anvil import *
from ...Functions import checked_property, innerText_property, disabled_property, name_property

# <div anvil-name="anvil-m3-radiobutton-container" class="anvil-m3-radiobutton-container">
#   <div class="anvil-m3-radiobutton-hover">
#     <input class="anvil-m3-radiobutton" anvil-name="anvil-m3-radiobutton" type="radio">
#   </div>
#   <label class="anvil-m3-radiobutton-label" anvil-name="anvil-m3-radiobutton-label"></label>
# </div>


class RadioButton(RadioButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  enabled = not disabled_property('anvil-m3-radiobutton')
  selected = checked_property('anvil-m3-radiobutton')
  group_name = name_property('anvil-m3-radiobutton')
  label = innerText_property('anvil-m3-radiobutton-label')

    # Any code you write here will run before the form opens.

# from ._anvil_designer import CheckboxTemplate
# from anvil import *
# from ...Functions import checked_property, innerText_property, disabled_property

# class Checkbox(CheckboxTemplate):
#   def __init__(self, **properties):
#     # Set Form properties and Data Bindings.
#     self.init_components(**properties)

#   disabled = disabled_property('anvil-m3-checkbox')

#   selected = checked_property('anvil-m3-checkbox')

#   label = innerText_property('anvil-m3-checkbox-label')

#   @property
#   def error(self):
#     return self._error

#   @error.setter
#   def error(self, value):
#     self.dom_nodes['anvil-m3-checkbox-container'].classList.remove('anvil-m3-checkbox-error')
#     self._error = value
#     if value:
#       self.dom_nodes['anvil-m3-checkbox-container'].classList.add('anvil-m3-checkbox-error')
#       self._error = value
