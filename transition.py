
class Transition:
  def __init__(self, startval: float, endval: float, duration=1000.0):
    self.startval = startval
    self.endval = endval
    self.duration = duration
    self.curval = startval
    self.t = 0.0

  def tick(self, clock):
    self.t += clock.get_time()
    if self.t > self.duration:
      self.t = self.duration
    return self.startval + self.interpolate() * (self.endval - self.startval)

  def interpolate(self):
    return self.t / self.duration