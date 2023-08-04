from ._anvil_designer import ButtonMenuTemplate
from anvil import *
from anvil.js.window import document

class ButtonMenu(ButtonMenuTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # TODO: needs an event handler to close when not focused
    


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

  @property
  def menuOpen(self):
    return self._menuOpen
  @menuOpen.setter
  def menuOpen(self, value):
    self._menuOpen = value or False
  
  def toggle_menu_visibility(self, **event_args):
    self.set_visibility()
    # return classes.contains(className)
    self.menuOpen = not self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList.contains('anvil-m3-buttonMenu-items-hidden')

  def set_visibility(self, value = None):
    classes = self.dom_nodes['anvil-m3-buttonMenu-items-container'].classList
    if value:
      classes.toggle('anvil-m3-buttonMenu-items-hidden', value)
    else:
      classes.toggle('anvil-m3-buttonMenu-items-hidden')

  def closeOnLoseFocus(self, event):
    if not self.dom_nodes['anvil-m3-buttonMenu-items-container'].contains(event.target):
      print("outside")
      self.set_visibility(False)


# 
    # print("menu is")
    # print(value)
    # if self._menuOpen:
    #   document.addEventListener("click", self.closeOnLoseFocus)
    # else:
    #   document.removeEventListener("click", self.closeOnLoseFocus) 





  
  def _anvil_get_design_info_(self, as_layout=False):
    design_info = super()._anvil_get_design_info_(as_layout)
    design_info["interactions"] = [
      {
        "type": "on_selection",
        "callbacks": {"onSelect": self._on_select, "onDeselect": self._on_deselect, "onSelectDescendent": self._on_select_descendant, "onDeselectDescendant": self._on_deselect_descendant, "onSelectOther": self._on_select_other}
      }
        # {"type": "on_selection", {"onSelect": self._on_select, "onDeselect": self._on_deselect, "onSelectDescendent": self._on_select_descendant, "onDeselectDescendant": self._on_deselect_descendant, "onSelectOther": self._on_select_other}}
    ]
    return design_info

    # plus a whole bunch of methods called _on_select() etc
  def _on_select(self):
    print("on_select called")

  def _on_deselect(self):
    print("on_deselect called")

  def _on_select_descendant(self):
    print("_on_select_descendant called")

  def _on_deselect_descendant(self):
    print("_on_deselect_descendant called")

  def _on_select_other(self):
    print("_on_select_other called")

  def menu_item_1_click(self, **event_args):
    print("clicked the first one!")

  def menu_item_5_click(self, **event_args):
    print("clicked another one")


  
