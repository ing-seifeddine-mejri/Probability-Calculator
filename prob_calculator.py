import copy
import random

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for attr in kwargs.keys():
      for _ in range(kwargs[attr]):
        self.contents.append(attr)

  def draw(self, number):
    number = min(number, len(self.contents))
    random_balls = []
    for _ in range(number):
      no = random.randint(0, len(self.contents)-1)
      random_balls.append(self.contents.pop(no))
    return random_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  count = 0
  for _ in range(num_experiments):
    exp = copy.deepcopy(hat)
    random_balls = exp.draw(num_balls_drawn)
    correct_balls = 0
    for color in expected_balls.keys():
      if random_balls.count(color) >= expected_balls[color]:
        correct_balls += 1
    if correct_balls == len(expected_balls):
        count += 1

  probability = float(count) / num_experiments
  return(probability)