import unittest


from main.models import Player, Field, Match
from helpers import get_invalid_matches, remove_invalid_matches, create_new_match


class GetInvalidMatchesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.player1 = Player.objects.create(name="Tom")
        cls.player2 = Player.objects.create(name="Marca")
        cls.field = Field.objects.create(name="Bio lounge")

    def tearDown(self):
        Match.objects.all().delete()

    def test_one_invalid_match(self):
        match = create_new_match(self.player1.id, self.player2.id, 13, 17, self.field.id)
        self.assertEqual(get_invalid_matches(), [match])

    def test_multiple_invalid_matches(self):
        match = create_new_match(self.player1.id, self.player2.id, 11, 11, self.field.id)
        match2 = create_new_match(self.player1.id, self.player2.id, 11, -1, self.field.id)
        self.assertEqual(len(get_invalid_matches()), 2)

    def test_no_matches(self):
        self.assertEqual(get_invalid_matches(), [])

    def test_one_valid_match(self):
        match = create_new_match(self.player1.id, self.player2.id, 11, 10, self.field.id)
        self.assertEqual(get_invalid_matches(), [])

    def test_invalid_and_valid_match(self):
        match1 = create_new_match(self.player1.id, self.player2.id, 11, 10, self.field.id)
        match = create_new_match(self.player1.id, self.player2.id, 12, 10, self.field.id)
        self.assertEqual(get_invalid_matches(), [match])

    def test_same_score(self):
        match = create_new_match(self.player1.id, self.player2.id, 10, 10, self.field.id)
        self.assertEqual(get_invalid_matches(), [match])

    def test_same_winning_score(self):
        match = create_new_match(self.player1.id, self.player2.id, 11, 11, self.field.id)
        self.assertEqual(get_invalid_matches(), [match])


class RemoveInvalidMatchesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.player1 = Player.objects.create(name="Tom")
        cls.player2 = Player.objects.create(name="Marca")
        cls.field = Field.objects.create(name="Bio Lounge")

    def tearDown(self):
        Match.objects.all().delete()

    def test_only_invalid_removal(self):
        match1 = create_new_match(self.player1.id, self.player2.id, 11, 10, self.field.id)
        match1_id = match1.id
        match = create_new_match(self.player1.id, self.player2.id, 12, 10, self.field.id)
        invalid_ids = remove_invalid_matches()
        self.assertEqual(match1_id, Match.objects.first().id)
