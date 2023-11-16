import anvil.server
from .Card import Card
import anvil.designer
from ..Functions import property_with_callback

enabled_property = {"name": "enabled", "type": "boolean", "important": True, "default_value": True, "designerHint": "enabled"}
click_event = {"name": "click", "default_event": True, "description": "When the component is clicked"}

class InteractiveCard(Card):
  _anvil_properties_ = [enabled_property, *Card._anvil_properties_]
  _anvil_events_ = [click_event, *Card._anvil_events_]
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-card'].classList.toggle('interactive', True)
    self.handle_click = self.handle_click
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def set_enabled(self, value): #why not being set in the beginning??
    self.dom_nodes['anvil-m3-card'].classList.toggle('disabled', not value)
  enabled = property_with_callback("enabled", set_enabled)
  
  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-card'].addEventListener("click", self.handle_click)
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-card'].removeEventListener("click", self.handle_click)

  def handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")
