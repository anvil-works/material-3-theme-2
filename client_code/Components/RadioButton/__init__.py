from ._anvil_designer import RadioButtonTemplate
from anvil import *

# <div anvil-name="anvil-m3-radio-button-container" class="anvil-m3-radio-button-container">
#   <div class="anvil-m3-radio-button-hover">
#     <input class="anvil-m3-radio-button" anvil-name="anvil-m3-radio-button" type="radio">
#     <span anvil-name="anvil-m3-radio-button-unchecked" class="material-symbols-outlined">radio_button_unchecked</span>
#     <span anvil-name="anvil-m3-radio-button-checked" class="material-symbols-outlined">radio_button_checked</span>
#     <label class="anvil-m3-radio-button-label" anvil-name="anvil-m3-radio-button-label"></label>
#   </div>
# </div>

class RadioButton(RadioButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  @property
  def checked(self):
    return self._checked

  @checked.setter
  def checked(self, value):
    self._checked = value
    if value:
      self.dom_nodes['anvil-m3-radio-button-unchecked'].style.display= "none"
      self.dom_nodes['anvil-m3-radio-button-checked'].style.display= "inline"
    else:
      self.dom_nodes['anvil-m3-radio-button-checked'].style.display= "none"
      self.dom_nodes['anvil-m3-radio-button-unchecked'].style.display= "inline"
      
