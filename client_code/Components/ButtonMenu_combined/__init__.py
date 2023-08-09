from ._anvil_designer import ButtonMenu_combinedTemplate
from anvil import *
from anvil.js import window
from anvil.js.window import document
import random, string

class ButtonMenu_combined(ButtonMenu_combinedTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # TODO: needs an event handler to close when not focused
    self.id = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    self.dom_nodes['anvil-m3-buttonMenu-container'].id = self.id
    self.shield = document.createElement("div")
    self.shield.id = f'shield-{self.id}'
    self.shield.classList.toggle("anvil-m3-menu-clickShield", True)
    self.menuOpen = False

  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = value
    self.menu_button.text = value

  @property
  def appearance(self):
    return self._appearance
  @appearance.setter
  def appearance(self, value):
    self.menu_button.appearance = value

  # @property
  # def menuOpen(self):
  #   return self._menuOpen
  # @menuOpen.setter
  # def menuOpen(self, value):
  #   self._menuOpen = value or False
  #   self.dom_nodes['anvil-m3-buttonMenu-container']
  #   if value:
  #     # check if the eventlistener is there. do nothing if so.
  #     # else add it.
  #     pass
  #   else:
  #     # remove event listener
  #     pass
  #     # self.dom_nodes['anvil-m3-buttonMenu-container'].removeEventListener('focus', self.checkFocus)

  @property
  def enabled(self):
    return self._enabled
  @enabled.setter
  def enabled(self, value):
    self._enabled = value
    self.menu_button.enabled = value

  @property
  def position(self):
    return self._position;
  @position.setter
  def position(self, value = {"top": 0, "left": 0, "bottom": 0, "right": 0}):
    self._position = value
    self.windowSize = {"width": window.innerWidth, "height": window.innerHeight}
    menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
    self.menuSize = {"width": menuNode.offsetWidth, "height": menuNode.offsetHeight}

  def windowSize(self):
    return self._windowSize
  def windowSize(self, value):
    self._windowSize = value
    
  @property
  def menuSize(self):
    return self._menuSize
  @menuSize.setter
  def menuSize(self, value):
    self._menuSize = value

  def toggle_menu_visibility(self, **event_args):
    self.get_button_position() #TODO: Will really only need to get this if visible is true
    self.printPosition()
    self.menuOpen = self.set_visibility()
    if self.menuOpen:
      self.place_shield()
      # listen for children
      menuNode = self.dom_nodes['anvil-m3-buttonMenu-items-container']
      menuNode.addEventListener('click', self.childClicked)
      
  def set_visibility(self, value = None):
    classes = self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList
    if value is not None:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')
    return not self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList.contains('anvil-m3-buttonMenu-items-hidden')
    
  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "on_selection",
        "callbacks": {
          "onSelectDescendent": self._on_select_descendant,
          "onSelectOther": self._on_select_other
        }
      },
    ]
    return design_info

  def _on_select_descendant(self):
    self.set_visibility(True)

  def _on_select_other(self):
    self.set_visibility(False)

  def get_button_position(self):
    rect = self.menu_button.dom_nodes['anvil-m3-button'].getBoundingClientRect()
    self.position = {
      "top": rect.top,
      "right": rect.right,
      "bottom": rect.bottom,
      "left": rect.left
    }

  def printPosition(self):
    print(self.position["top"])
    print(self.position["right"])
    print(self.position["bottom"])
    print(self.position["left"])
    print()
    print(self.windowSize["width"])
    print(self.windowSize["height"])
    print()
    print(self.menuSize["width"])
    print(self.menuSize["height"])
    print("*****")

  def place_shield(self):
    #creating shield
    # shield = document.createElement("div")
    document.body.appendChild(self.shield)
    self.shield.addEventListener('click', self.remove_shield_handler)
    
  def remove_shield_handler(self, event):
    self.remove_shield()
    
  def remove_shield(self):
    if document.contains(self.shield):
      document.body.removeChild(self.shield)
      self.toggle_menu_visibility()
    
  def childClicked(self, event):
    print("child clicked")
    print(event)
    print(event.target)
    self.remove_shield()
  # detect if the child was clicked and if so, close the menu