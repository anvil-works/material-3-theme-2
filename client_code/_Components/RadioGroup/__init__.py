from ._anvil_designer import RadioGroupTemplate
from anvil import *
from ...Functions import property_with_callback, property_without_callback, margin_property, color_property
from anvil.js import window, get_dom_node
from anvil.js.window import document
import random, string, math
from ...utils import gen_id
import anvil.designer

class RadioGroup(RadioGroupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def _set_group_name(self, value):
    # go thru an change the group_name of every child to this
    pass
  group_name = property_with_callback("group_name", _set_group_name)
  
  items = property_without_callback("items")



# <div anvil-name="anvil-m3-radiogroup-component" style="display:flex">
#   <div anvil-name="anvil-m3-radiogroup-container" class="anvil-m3-radiogroup-container">
#   </div>
# </div>