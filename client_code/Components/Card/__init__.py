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

  def set_image_position(self, value):
    self.dom_nodes['anvil-m3-card-image'].style = ""
    self.dom_nodes['anvil-m3-card-content'].style = ""
    self.dom_nodes['anvil-m3-card-shadow'].style = ""
    if value is "None":
      self.dom_nodes['anvil-m3-card-image'].style = "display: none;"
    elif value is "Top":
      self.dom_nodes['anvil-m3-card-shadow'].style = "flex-direction: column;"
      self.dom_nodes['anvil-m3-card-image'].style = "width: 100%;"
    elif value is "Bottom":
      self.dom_nodes['anvil-m3-card-shadow'].style = "flex-direction: column-reverse;"
      self.dom_nodes['anvil-m3-card-image'].style = "width: 100%;"
    elif value is "Left":
      self.dom_nodes['anvil-m3-card-shadow'].style = "flex-direction: row;"
      self.dom_nodes['anvil-m3-card-image'].style = "height: 100%;"
    elif value is "Right":
      self.dom_nodes['anvil-m3-card-shadow'].style = "flex-direction: row-reverse;"
      self.dom_nodes['anvil-m3-card-image'].style = "height: 100%;"
    elif value is "Full":
      self.dom_nodes['anvil-m3-card-content'].style = "display: none;"
      # self.dom_nodes['anvil-m3-card-image'].style = "width: 100%; height: 100%;"
  image_position = property_with_callback("image_position", set_image_position)
  
  def set_appearance(self, value):
    pass
    # self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-outlined', False)
    # self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-filled', False)
    # self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-elevated', False)
    # self.dom_nodes['anvil-m3-card'].classList.toggle(f'anvil-m3-{value}', True)
  appearance = property_with_callback("appearance", set_appearance)