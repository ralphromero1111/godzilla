class seatopia:
  def __init__(self) -> None:
    print("megalon! MEGALON! wake up MEAGALON!\n")

seatopia()

class movie:
  def __init__(self, title, distributor, year):
    self.title = title
    self.distributor = distributor
    self.year = year

  def release(self):
    print(f'{self.title} was released by {self.distributor} in {self.year}.')


m = movie('Godzilla Vs. Megalon', 'Cinema Shares International', 1976)

m.release()


g = movie('Godzilla Vs. Gigan', 'Cinema Shares International',1977)

g.release()

smog = movie('Godzilla Vs The Smog Monster', 'American International Pictures', 1972)

smog.release()