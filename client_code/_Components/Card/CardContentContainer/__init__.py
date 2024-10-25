from ._anvil_designer import CardContentContainerTemplate
from anvil import *
import anvil.server
import anvil.designer
from ....utils.properties import margin_property

class CardContentContainer(CardContentContainerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.tag = ComponentTag()
    self._props = properties
    self.init_components(**properties)
    
    if not anvil.designer.in_designer:
      self.dom_nodes['empty-slot'].style.display = "none"

  margin = margin_property('anvil-m3-card-content-container')

  def add_component(self, component, slot="card-content-container-slot", **layout_props):
    super().add_component(component, slot=slot, **layout_props)
    