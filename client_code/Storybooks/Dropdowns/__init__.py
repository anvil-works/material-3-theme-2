from ._anvil_designer import DropdownsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Dropdowns(DropdownsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.dropdown_menu_4.items = [("First Option", 0), ("Second Option", 1), ("Third Option", 2)]
    # Any code you write here will run before the form opens.

  def dropdown_menu_4_change(self, **event_args):
    if self.dropdown_menu_4.selected_value:
      self.label_1.text = self.dropdown_menu_4.selected_value[1]
    else:
      self.label_1.text = "nothing selected"

  def dropdown_menu_2_change(self, **event_args):
    """This method is called when an item is selected"""
    # print('hello')
    pass

  def set_dd_click(self, **event_args):
    self.dropdown_menu_3.selected_value = "TEEHEEHEE"

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.drop_down_1.selected_value = "something else"

  def button_2_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.dropdown_menu_2.selected_value = self.dropdown_menu_2.items[2]
