from ._anvil_designer import DropdownMenu_integratedTemplate
from anvil import HtmlTemplate
from anvil import *
from anvil.js.window import document
import anvil.designer
from ..Menu.MenuItem import MenuItem
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

    # self.handle_keyboard_events = self.handle_keyboard_events
    self.remove_shield_handler = self.remove_shield_handler
    self.child_clicked = self.child_clicked

    self.add_event_handler("x-anvil-page-added", self.on_mount)
    self.add_event_handler("x-anvil-page-removed", self.on_cleanup)

  def on_mount(self, **event_args):
    self.text_field.dom_nodes['text-field'].addEventListener('click', self.handle_box_click)
  # click event listener on box to toggle open or closed menu

    # document.addEventListener('keydown', self.handle_keyboard_events)
    self.shield.addEventListener('click', self.remove_shield_handler)
    self.menuNode.addEventListener('click', self.child_clicked)
  def on_cleanup(self, **event_args):
    self.text_field.dom_nodes['text-field'].removeEventListener('click', self.handle_box_click)
    # document.removeEventListener('keydown', self.handle_keyboard_events)
    self.shield.removeEventListener('click', self.remove_shield_handler)
    self.menuNode.removeEventListener('click', self.child_clicked)


  visible = HtmlTemplate.visible
  align = style_property('anvil-m3-dropdownMenu-component', 'justifyContent')

  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.text_field.enabled = value
      # self.get_hover_index_information()

  def handle_box_click(self, event):
    # todo: figure out how to get it to now do the textfield interactions
    event.preventDefault()
    event.stopPropagation()
    self.toggle_menu_visibility()

  def toggle_menu_visibility(self, **event_args):
      self.set_visibility()

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
        
    else:
      self.menuNode.removeAttribute("style")
      self.hoverIndex = None
      # self.clear_hover_styles()

  def place_shield(self):
    if not document.contains(self.shield):
      document.body.appendChild(self.shield)
      document.body.style.overflow = "hidden"

  def remove_shield_handler(self, event):
    self.remove_shield()
    self.set_visibility(False)

  def remove_shield(self):
    if document.contains(self.shield):
      document.body.removeChild(self.shield)
      document.body.style.removeProperty("overflow")


  def child_clicked(self, event):
    # do the click action. The child should handle this
    self.remove_shield()
    self.set_visibility(False)


# DESIGNER INTERACTIONS
  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "designer_events",
        "callbacks": {
          "onSelectDescendent": self._on_select_descendent,
          "onSelectOther": self._on_select_other
        }
      },
      {
      "type": "whole_component",
      "title": "Visible",
      "icon": "add", #TODO: eye icon
      "callbacks": {
        "execute": self.toggle_visible
      }
    }, {
      "type": "whole_component",
      "title": "Enable",
      "icon": "add", #TODO: power icon
      "callbacks": {
        "execute": self.toggle_enabled
      }
    # },{
    #   "type": "whole_component",
    #   "title": "Edit text",
    #   "icon": "edit",
    #   "default": True,
    #   "callbacks": {
    #     "execute": lambda: anvil.designer.start_inline_editing(self.menu_button, "text", self.menu_button.dom_nodes['anvil-m3-button-text'])
    #   }
    }]
    return design_info

  def _on_select_descendent(self):
    self.set_visibility(True)

  def _on_select_other(self):
    self.set_visibility(False)

  def toggle_visible(self):
    self.visible = not self.visible
    anvil.designer.update_component_properties(self, {'visible': self.visible})

  def toggle_enabled(self):
    self.enabled = not self.enabled
    anvil.designer.update_component_properties(self, {'enabled': self.enabled})