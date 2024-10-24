from ._anvil_designer import BrookeTestPageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time
from ..AnotherPage import AnotherPage

class BrookeTestPage(BrookeTestPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.layout.layout.show_sidesheet = False
    self.repeating_panel_1.items = app_tables.people.search()
    self.repeating_panel_1_copy.items = app_tables.people.search()








