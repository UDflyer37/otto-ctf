from ._anvil_designer import Home_PageTemplate
from anvil.js.window import document
import anvil.server

class Home_Page(Home_PageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)



    
      