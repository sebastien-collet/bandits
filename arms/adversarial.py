class AdversarialArm():
  def __init__(self, active):
    self.active = active

  def activate(self):
    self.active = True
    
  def deactivate(self):
    self.active = False
  
  def draw(self):
    if self.active:
      return 1.0
    else:
      return 0.0


