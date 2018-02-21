from helpers import get_initials, get_invalid_matches
import unittest

from main.models import Player, Field, Match


class GetInitialsTestCase(unittest.TestCase):
    def test_two_name_parts(self):
        self.assertEqual(get_initials("Tom Bean"), "T. B.")

    def test_four_name_parts(self):
        self.assertEqual(get_initials("Tom Bean Marca And"), "T. B. M. A.")

    def test_empty(self):
        self.assertEqual(get_initials(""), "")

    def test_space(self):
        self.assertEqual(get_initials(" "), "")


class GetInvalidMatchesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p1 = Player.objects.create(name="Tom")
        cls.p2 = Player.objects.create(name="Marca")
        cls.field = Field.objects.create(name="bio lounge")

    def test_one_invalid_match(self):
        match = self.create_invalid_match(13, 17)
        self.assertEqual(get_invalid_matches(), [match])

    def tearDown(self):
        Match.objects.all().delete()

    def test_no_matches(self):
        self.assertEqual(get_invalid_matches(), [])

    def test_same_score(self):
        match = self.create_invalid_match(11, 11)
        self.assertEqual(get_invalid_matches(), [match])

    def create_invalid_match(self, p1_score, p2_score):
        return Match.objects.create(player1=self.p1, player2=self.p2, player1_score=p1_score, player2_score=p2_score, field=self.field)
