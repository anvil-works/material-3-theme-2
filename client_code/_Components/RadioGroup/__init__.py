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
    self._selected_item = None
    self.init_components(**properties)
    
    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _on_mount(self, **event_args):
    pass

  def _on_cleanup(self, **event_args):
    pass

  def _set_group_name(self, value):
    self.recreate_group_items()
    # this is overkill - Probably makes more sense to just go thru and set the group_name of all the children
  group_name = property_with_callback("group_name", _set_group_name)

  def _set_items(self, value):
    self.recreate_group_items()
  items = property_with_callback("items", _set_items)

  def _set_selected_item(self, value):
    pass
    # 
  selected_item = property_with_callback("selected_item", _set_selected_item)

  def form_show(self, **event_args):
    if not self.group_name:
      self.group_name = gen_id()
    self.recreate_group_items()

  def recreate_group_items(self):
    self.clear(slot="anvil-m3-radiogroup-slot")
    for item in self.items:
      radio_button = RadioButton()
      radio_button.group_name = self.group_name
      radio_button.selected = item is self.selected_item
      if isinstance(item, tuple):
        radio_button.text = item[0]
        # todo: include all the properties and such
      else:
        radio_button.text = item
      def _handle_r_button_click(value = item, **e):
        self.selected_item = value
        self.raise_event("change")
      radio_button.add_event_handler("click", _handle_r_button_click)
      self.add_component(radio_button, slot="anvil-m3-radiogroup-slot")
      
  def get_group_value(self):
    return self.selected_item