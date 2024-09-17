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

  
  def _set_items(self, value):
    # recreate all items with correc
    pass
  items = property_with_callback("items", _set_items)
  

  


# <div anvil-name="anvil-m3-radiogroup-component" style="display:flex">
#   <div anvil-name="anvil-m3-radiogroup-container" class="anvil-m3-radiogroup-container">
#   </div>
# </div>

  def form_show(self, **event_args):
    if not self.group_name:
      self.group_name = gen_id()
            # id = gen_id()
      # self.dom_nodes["anvil-m3-radiobutton-input"].id = id
      # self.dom_nodes["anvil-m3-radiobutton-label"].setAttribute("for", id)
    self.create_group_items()

  def create_group_items(self):
    for item in self.items:
      radio_button = RadioButton()
      radio_button.group_name = self.group_name
      if isinstance(item, tuple):
        radio_button.text = item[0]
        # todo: include all the properties and such
      else:
        radio_button.text = item
      self.add_component(radio_button, slot="anvil-m3-radiogroup-slot")
      
      
