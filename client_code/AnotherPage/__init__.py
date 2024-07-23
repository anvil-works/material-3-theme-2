from ._anvil_designer import AnotherPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Components.Link import Link as M3_Link
from ..Components.Slider import Slider

class AnotherPage(AnotherPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    link_1 = M3_Link(text="link", bold=True)
    link_2 = M3_Link(text="another link")
    self.button_menu_1.menu_items = [link_1, link_2]
    self.dropdown_menu_1.items = [('Hello', True), ('Goodbye', False)]
    self.drop_down_1.items = [('Hello', True), ('Goodbye', False)]


    # Notification("This is a notification", timeout=None, title="Notification!", style="info").show()
    # Notification("This is a notification", timeout=None, title="Notification!", style="success").show()
    # Notification("This is a notification", timeout=None, title="Notification!", style="danger").show()
    # Notification("This is a notification", timeout=None, title="Notification!", style="warning").show()




