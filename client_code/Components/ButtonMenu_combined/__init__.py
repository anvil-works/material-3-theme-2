from ._anvil_designer import ButtonMenu_combinedTemplate
from anvil import *
from anvil.js import window
from anvil.js.window import document
import random, string

class ButtonMenu_combined(ButtonMenu_combinedTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # TODO: needs an event handler to close when not focused
    # self.id = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

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

  @property
  def windowSize(self):
    return self._windowSize;
  @windowSize.setter
  def windowSize(self, value)

  def toggle_menu_visibility(self, **event_args):
    self.set_visibility()
    self.menuOpen = not self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList.contains('anvil-m3-buttonMenu-items-hidden')
    self.get_button_position() #TODO: Will really only need to get this if visible is true
    # self.printPosition()

  def set_visibility(self, value = None):
    classes = self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList
    if value is not None:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', not value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')

  def checkFocus(self, event):
    # document.activeElement
    # var descendants = theElement.querySelectorAll("*");
    print(event.target)
    pass

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
    print("Selected! Open")
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
