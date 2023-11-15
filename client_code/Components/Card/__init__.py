from ._anvil_designer import CardTemplate
import anvil.designer
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
    if not anvil.designer.in_designer:
      self.dom_nodes['empty-slot'].style = "display: none"
  align = style_property('anvil-m3-card-component', 'justifyContent', 'align')
  visible = HtmlTemplate.visible
    

  def set_image_position(self, value):
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle('none-image', False)
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle('top-image', False)
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle('bottom-image', False)
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle('left-image', False)
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle('right-image', False)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle('none-image', False)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle('top-image', False)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle('bottom-image', False)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle('left-image', False)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle('right-image', False)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle('none-image', False)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle('top-image', False)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle('bottom-image', False)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle('left-image', False)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle('right-image', False)

    v = value.lower()
    print(v)
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle(f'{v}-image', True)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle(f'{v}-image', True)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle(f'{v}-image', True)
  image_position = property_with_callback("image_position", set_image_position)
  
  def set_appearance(self, value):
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle('anvil-m3-outlined', False)
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle('anvil-m3-filled', False)
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle('anvil-m3-elevated', False)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle('anvil-m3-outlined', False)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle('anvil-m3-filled', False)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle('anvil-m3-elevated', False)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle('anvil-m3-outlined', False)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle('anvil-m3-filled', False)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle('anvil-m3-elevated', False)
    
    self.dom_nodes['anvil-m3-card-shadow'].classList.toggle(f'anvil-m3-{value}', True)
    self.dom_nodes['anvil-m3-card-image'].classList.toggle(f'anvil-m3-{value}', True)
    self.dom_nodes['anvil-m3-card-content'].classList.toggle(f'anvil-m3-{value}', True)
  appearance = property_with_callback("appearance", set_appearance)

  def set_image(self, value):
    if value:
      self.dom_nodes['anvil-m3-card-image'].style.backgroundImage = f"url('{value}')";
    else:
      self.dom_nodes['anvil-m3-card-image'].style.element.style.removeProperty = "background-image"
  card_image = property_with_callback("card_image", set_image)