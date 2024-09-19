class seatopia:
  def __init__(self) -> None:
    print("megalon! MEGALON! wake up MEAGALON!\n")

seatopia()

class movie:
  def __init__(self, title, distributor):
    self.title = title
    self.distributor = distributor

  def release(self):
    print(f'{self.title} was released by {self.distributor}.')


m = movie('Godzilla Vs. Megalon', 'Cinema Shares International')

m.release()
