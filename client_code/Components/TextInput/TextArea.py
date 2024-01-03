import anvil.server
from .. import TextInput
import anvil.designer

class TextArea(TextInput):
  # _anvil_properties_ = [*TextInput._anvil_properties_]
  
  def __init__(self, **properties):
    # super().__init__(**properties)
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
