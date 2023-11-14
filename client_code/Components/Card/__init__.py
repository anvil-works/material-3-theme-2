from ._anvil_designer import CardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import HtmlTemplate
from ...Functions import property_with_callback, style_property

class Card(CardTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  align = style_property('anvil-m3-card-component', 'justifyContent', 'align')
  visible = HtmlTemplate.visible
  
  def set_appearance(self, value):
    self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-outlined', False)
    self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-filled', False)
    self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-elevated', False)
    self.dom_nodes['anvil-m3-card'].classList.toggle(f'anvil-m3-{value}', True)
  appearance = property_with_callback("appearance", set_appearance)