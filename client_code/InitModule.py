import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from anvil import pluggable_ui
from ._Components.Button import Button
from ._Components.TextInput.TextBox import TextBox
from ._Components.Checkbox import Checkbox

def make_footer_button(button_type, **kwargs):
  return Button(**kwargs)

pluggable_ui.provide("m3", {
  "anvil.TextBoxWithLabel": TextBox,
  "anvil.TextBox": TextBox,
  "anvil.Button": Button,
  "anvil.CheckBox": Checkbox,
  "anvil.alerts.FooterButton": make_footer_button
})

