import os
import random
from threading import Thread
from time import sleep


UP = 1
DOWN = -1

class Elevator:

  def __init__(self, height):
    self.floor = 1
    self.direction = UP
    self.up = [0] * (height + 1)
    self.down = [0] * (height + 1)
    self.queue = []
    self.top = height

  def add_floor(self, level, direction):
    if len(self.queue) == 0:
      if direction == self.direction:
        return

  def run(self):
    while(True):
      self.move()
      sleep(1)

  ## Move up and down sporatically, no queue implementation
  def move(self):
      if self.floor == 1:
        self.direction = UP
      elif self.floor == self.top:
        self.direction = DOWN
      self.floor += self.direction

  def print(self):
    while(True):
      print(self)
      sleep(.1)

  def __str__(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    res = ""
    for x in range(self.top, 0, -1):
      res += "=={}==\n".format(x)
      if x == self.floor:
        res += "H"
      else:
        res += " "

      res += " ^" if self.up[x] else " "
      res += " "
      res += " v" if self.down[x] else " "
      res += "\n"
    return res

if __name__ == '__main__':
  floors = 5
  ele = Elevator(floors)
  t1 = Thread(None, ele.run)
  t1.start()
  t2 = Thread(None, ele.print)
  t2.start()
  while(True):
    sleep(1)
    floor = random.randint(1, floors)
    if random.randint(0, 1):
      ele.up[floor] = not ele.up[floor]
    else:
      ele.down[floor] = not ele.up[floor]