import unittest


from main.models import Player, Field, Match
from helpers import get_invalid_matches


class GetInvalidMatchesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p1 = Player.objects.create(name="Tom")
        cls.p2 = Player.objects.create(name="Marca")
        cls.field = Field.objects.create(name="Bio lounge")

    def tearDown(self):
        Match.objects.all().delete()

    def test_one_invalid_match(self):
        match = self.create_match(13, 17)
        self.assertEqual(get_invalid_matches(), [match])

    def test_multiple_invalid_matches(self):
        match = self.create_match(11, 11)
        match2 = self.create_match(11, -1)
        self.assertEqual(len(get_invalid_matches()), 2)

    def test_no_matches(self):
        self.assertEqual(get_invalid_matches(), [])

    def test_one_valid_match(self):
        match = self.create_match(11, 10)
        self.assertEqual(get_invalid_matches(), [])

    def test_invalid_and_valid_match(self):
        match1 = self.create_match(11, 10)
        match = self.create_match(12, 10)
        self.assertEqual(get_invalid_matches(), [match])

    def test_same_score(self):
        match = self.create_match(10, 10)
        self.assertEqual(get_invalid_matches(), [match])

    def test_same_winning_score(self):
        match = self.create_match(11, 11)
        self.assertEqual(get_invalid_matches(), [match])

    def create_match(self, p1_score, p2_score):
        return Match.objects.create(
            player1=self.p1,
            player2=self.p2,
            player1_score=p1_score,
            player2_score=p2_score,
            field=self.field
        )


class RemoveInvalidMatchesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p1 = Player.objects.create(name="Tom")
        cls.p2 = Player.objects.create(name="Marca")
        cls.field = Field.objects.create(name="Bio lounge")

    def tearDown(self):
        Match.objects.all().delete()

    def test_only_invalid_removal(self):
        match1 = self.create_match(11, 10)
        match1_id = match1.id
        match = self.create_match(12, 10)
        self.assertEqual(match1_id, Match.objects.first().id)

    def create_match(self, p1_score, p2_score):
        return Match.objects.create(
            player1=self.p1,
            player2=self.p2,
            player1_score=p1_score,
            player2_score=p2_score,
            field=self.field
        )
