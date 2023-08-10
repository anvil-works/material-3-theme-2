from ._anvil_designer import TestPageTemplate
from anvil import *
import plotly.graph_objects as go

class TestPage(TestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def select_font(self, value):
    print(f"font face {value} selected")

  def menu_item_2_click(self, **event_args):
    self.select_font(self.menu_item_2.text)

  def menu_item_3_click(self, **event_args):
    self.select_font(self.menu_item_3.text)

  def menu_item_10_click(self, **event_args):
    self.select_font(self.menu_item_10.text)

  def menu_item_12_click(self, **event_args):
    self.select_font(self.menu_item_12.text)

  def menu_item_8_click(self, **event_args):
    self.select_font(self.menu_item_8.text)

  def menu_item_11_click(self, **event_args):
    self.select_font(self.menu_item_11.text)

  def menu_item_9_click(self, **event_args):
    self.select_font(self.menu_item_9.text)






