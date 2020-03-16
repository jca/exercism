ALLERGIES = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128
}

class Allergies(object):

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        if item not in ALLERGIES:
            raise ValueError('{} is not a valid allergy'.format(item))

        return bool(ALLERGIES[item] & self.score)

    @property
    def lst(self):
        return [k for (k, v) in ALLERGIES.items() if v & self.score]
