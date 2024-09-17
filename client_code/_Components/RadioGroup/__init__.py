from ._anvil_designer import RadioGroupTemplate
from anvil import *
from ...Functions import property_with_callback, property_without_callback, margin_property, color_property
from anvil.js import window, get_dom_node
from anvil.js.window import document
import random, string, math
from ...utils import gen_id
import anvil.designer
from RadioButton import RadioButton

class RadioGroup(RadioGroupTemplate):
  def __init__(self, **properties):
    self._props = properties
    self._tooltip_node = None
    self.init_components(**properties)

  def _set_group_name(self, value):
    # go thru an change the group_name of every child to this
    pass
  group_name = property_with_callback("group_name", _set_group_name)
  
  items = property_without_callback("items") #can be tuple, use third element as props for radiobutton

  


# <div anvil-name="anvil-m3-radiogroup-component" style="display:flex">
#   <div anvil-name="anvil-m3-radiogroup-container" class="anvil-m3-radiogroup-container">
#   </div>
# </div>

  def form_show(self, **event_args):
    self.create_group_items()

  def create_group_items(self):
    for i in self.items:
      radio_button = RadioButton()
      radio_button.group_name = self.group_name
      self.add_component(radio_button, slot="anvil-m3-radiogroup-slot")
      
      
