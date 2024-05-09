import anvil.server
from .Card import Card
import anvil.designer
from ..Functions import property_with_callback

#todo figure out how to get default value to work
enabled_property = {"name": "enabled", "type": "boolean", "important": True, "default_value": True, "designerHint": "enabled", "group": "Interaction"}
click_event = {"name": "click", "default_event": True, "description": "When the component is clicked"}

class InteractiveCard(Card):
  _anvil_properties_ = [enabled_property, *Card._anvil_properties_]
  _anvil_events_ = [click_event, *Card._anvil_events_]
  def __init__(self, **properties):
    super().__init__(**properties)
    self.init_components(**properties)
    self.dom_nodes['anvil-m3-card'].classList.toggle('interactive', True)
    self._handle_click = self._handle_click
    self.enabled = self.enabled
    self.add_event_handler("x-anvil-page-added", self._on_mount)
    self.add_event_handler("x-anvil-page-removed", self._on_cleanup)

  def _set_enabled(self, value): #why not being set in the beginning??
    self.dom_nodes['anvil-m3-card'].classList.toggle('disabled', not value)
  enabled = property_with_callback("enabled", _set_enabled, default_value=True)
  
  def _on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-card'].addEventListener("click", self._handle_click)
  def _on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-card'].removeEventListener("click", self._handle_click)

  def _handle_click(self, event):
    event.preventDefault()
    self.raise_event("click")
