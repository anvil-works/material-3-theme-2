from ._anvil_designer import TestPageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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
    print("In the bottom")

  def menu_item_8_click(self, **event_args):
    self.select_font(self.menu_item_8.text)
    print("In the bottom")

  def menu_item_11_click(self, **event_args):
    self.select_font(self.menu_item_11.text)
    print("In the bottom")

  def menu_item_9_click(self, **event_args):
    self.select_font(self.menu_item_9.text)

  def menu_item_16_click(self, **event_args):
    alert("0 was clicked")

  def menu_item_19_click(self, **event_args):
    alert("2 was clicked")

  def menu_item_21_click(self, **event_args):
    alert("4 was clicked")

  def menu_item_29_click(self, **event_args):
    alert("6 was clicked")

  def menu_item_26_click(self, **event_args):
    self.selected_trail.text = "Running"

  def menu_item_27_click(self, **event_args):
    self.selected_trail.text = "Walking"

  def menu_item_33_click(self, **event_args):
    self.selected_trail.text = "Cycling"

  def menu_item_31_click(self, **event_args):
    self.selected_trail.text = "Skiing"

  def menu_item_28_click(self, **event_args):
    self.selected_trail.text = "Hiking"

  def menu_item_17_click(self, **event_args):
    is_bold = self.selected_trail.bold
    self.selected_trail.bold = not is_bold

  def menu_item_22_click(self, **event_args):
    is_italic = self.selected_trail.italic
    self.selected_trail.italic = not is_italic

  def menu_item_25_click(self, **event_args):
    is_underline = self.selected_trail.underline
    self.selected_trail.underline = not is_underline

  def menu_item_24_click(self, **event_args):
    alert("Sorry, strikethru not supported")

  def menu_item_23_click(self, **event_args):
    alert("Superscript not supported")

  def menu_item_18_click(self, **event_args):
    alert("Subscript not supported")

  def menu_item_20_click(self, **event_args):
    print("do nothing")

  def switch_3_change(self, **event_args):
    """This method is called when the state of the component is changed"""
    print('switched')

  def checkbox_1_change(self, **event_args):
    """This method is called when the component is checked or unchecked"""
    print('checked')
























