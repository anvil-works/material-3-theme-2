from ._anvil_designer import DropdownMenu_integratedTemplate
from anvil import HtmlTemplate
from anvil import *
from anvil.js.window import document
import anvil.designer
from ...Functions import underline_property, italic_property, style_property, color_property, innerText_property, bold_property, font_size_property

class DropdownMenu_integrated(DropdownMenu_integratedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.open = False
    self.window_size = {}
    self.menu_size = {}
    self.button_positioning = {}

    self.hoverIndex = None
    self.itemIndices = set()
    self.children = None
    
    self.shield = document.createElement("div")
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)
    self.menuNode = self.dom_nodes['anvil-m3-dropdownMenu-items-container']

    self.handle_keyboard_events = self.handle_keyboard_events
    self.remove_shield_handler = self.remove_shield_handler
    self.child_clicked = self.child_clicked

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.text_field.dom_nodes['text-field'].addEventListener('click', self.handle_box_click)
  # click event listener on box to toggle open or closed menu

    # document.addEventListener('keydown', self.handle_keyboard_events)
    self.shield.addEventListener('click', self.remove_shield_handler)
    # self.menuNode.addEventListener('click', self.child_clicked)
  def on_cleanup(self, **event_args):
    self.text_field.dom_nodes['text-field'].removeEventListener('click', self.handle_box_click)
    # document.removeEventListener('keydown', self.handle_keyboard_events)
    self.shield.removeEventListener('click', self.remove_shield_handler)
    # self.menuNode.removeEventListener('click', self.child_clicked)


  visible = HtmlTemplate.visible
  align = style_property('anvil-m3-dropdownMenu-component', 'justifyContent')

  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.text_field.enabled = value

  def set_visibility(self, value = None):
    classes = self.menuNode.classList
    if value is not None:
      classes.toggle('anvil-m3-dropdownMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-dropdownMenu-items-hidden')
      
    self.open = not classes.contains('anvil-m3-dropdownMenu-items-hidden')
    if self.open:
      if not anvil.designer.in_designer:
        self.place_shield()
      # self.get_button_measurements()
      # self.update_menu_placement()

      # self.get_hover_index_information()

  def handle_box_click(self, event):
    # todo: figure out how to get it to now do the textfield interactions
    event.preventDefault()
    event.stopPropagation()
    self.toggle_menu_visibility()

  def toggle_menu_visibility(self, value = None):
    if (value is None):
      value = not self.menu.visible
    self.menu.visible = value
    if value:
      if not anvil.designer.in_designer:
        self.place_shield()

  def place_shield(self):
    if not document.contains(self.shield):
      document.body.appendChild(self.shield)
      document.body.style.overflow = "hidden"

  def remove_shield_handler(self, event):
    self.remove_shield()
    self.set_menu_visibility(False)

  def remove_shield(self):
    if document.contains(self.shield):
      document.body.removeChild(self.shield)
      document.body.style.removeProperty("overflow")
