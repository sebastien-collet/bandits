import random

class BernoulliArm():
  def __init__(self, p):
    self.p = p
  
  def draw(self):
    if random.random() > self.p:
      return 0.0
    else:
      return 1.0
  
    
class ContextualBernoulliArm():
    def __init__(self, p):
        self.p_for_context = p
  
    def draw(self,context):
        if random.random() > self.p_for_context[context]:
            return 0
        else:
            return 1.0

