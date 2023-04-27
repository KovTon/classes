import unittest
from hero_class import Hero


class HeroTakeDamageMethod(unittest.TestCase):

    def test_take_dmg(self):
        hero = Hero('', '', '', 100, 50, 50, 50)
        hero.get_dmg(10)
        self.assertEqual(hero.hp, 90)

    def test_take_more_dmg(self):
        hero = Hero('', '', '', 100, 50, 50, 50)
        hero.get_dmg(20000000)
        self.assertEqual(hero.hp, 0)

    def test_take_zero_dmg(self):
        hero = Hero('', '', '', 100, 50, 50, 50)
        hero.get_dmg(0)
        self.assertEqual(hero.hp, 100)

    def test_take_dmg_with_defense(self):
        hero = Hero('', '', '', 100, 50, 50, 50)
        hero.defense()
        hero.get_dmg(10)
        self.assertEqual(hero.hp, 100)

    def test_take_more_dmg_with_defense(self):
        hero = Hero('', '', '', 100, 50, 50, 50)
        hero.defense()
        hero.get_dmg(20000000)
        self.assertEqual(hero.hp, 0)

    def test_take_zero_dmg_with_defense(self):
        hero = Hero('', '', '', 100, 50, 50, 50)
        hero.defense()
        hero.get_dmg(0)
        self.assertEqual(hero.hp, 100)

    def test_take_dmg_over_defense(self):
        hero = Hero('', '', '', 100, 50, 50, 50)
        hero.defense()
        hero.get_dmg(51)
        self.assertEqual(hero.hp, 99)


if __name__ == '__main__':
    unittest.main()
