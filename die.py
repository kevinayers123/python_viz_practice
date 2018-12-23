from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)


from Die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for rol_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
