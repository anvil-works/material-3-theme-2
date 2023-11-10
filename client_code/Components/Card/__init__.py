from ._anvil_designer import CardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil import HtmlTemplate
from anvil.tables import app_tables
from ...Functions import property_with_callback, style_property

class Card(CardTemplate):
  def __init__(self, **properties):
    self._props = properties
    self.init_components(**properties)
    
    self.handle_click = self.handle_click
    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.dom_nodes['anvil-m3-card'].addEventListener('click', self.handle_click)
  def on_cleanup(self, **event_args):
    self.dom_nodes['anvil-m3-card'].removeEventListener('click', self.handle_click)

  def handle_click(self, event):
    self.raise_event("click")

  align = style_property('anvil-m3-card-component', 'justifyContent', 'align')
  visible = HtmlTemplate.visible
  
  def set_appearance(self, value):
    self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-outlined', False)
    self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-filled', False)
    self.dom_nodes['anvil-m3-card'].classList.toggle('anvil-m3-elevated', False)
    self.dom_nodes['anvil-m3-card'].classList.toggle(f'anvil-m3-{value}', True)
  appearance = property_with_callback("appearance", set_appearance)
    
  # @property
  # def interactive(self):
  #   return self._interactive
    
  # @interactive.setter
  # def interactive(self, value):
  #   self._interactive = value
  #   classes = self.dom_nodes['anvil-m3-card'].classList
  #   classes.toggle('anvil-m3-interactive', value)
      
  # @property
  # def disabled(self):
  #   return self._disabled
    
  # @disabled.setter
  # def disabled(self, value):
  #   self._disabled = value
  #   card = self.dom_nodes['anvil-m3-card']
  #   classes = card.classList
  #   classes.toggle('anvil-m3-disabled', value)
    
  # def hasClass(self, className):
  #   classes = self.dom_nodes['anvil-m3-card'].classList
  #   return classes.contains(className)

  # def printAllClasses(self):
  #   classes = self.dom_nodes['anvil-m3-card'].classList
  #   for c in classes:
  #     print(c)
