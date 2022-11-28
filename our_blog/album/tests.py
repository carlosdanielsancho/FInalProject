from django.test import TestCase

# Create your tests here.

import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from album.models import Album


class AlbumTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            usertitle="testuser",
            password="qwerty-1234",
        )
        Album.objects.create(title="Breakfast in America", performer="Supertramp", owner=self.test_user)
        Album.objects.create(title="MTV Unplugged", performer="Eric Clapton", owner=self.test_user)

        album_test_num = 20
        self.mock_titles = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(album_test_num)
        ]
        self.mock_performers = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(album_test_num)
        ]

        for mock_title, mock_performer in zip(self.mock_titles, self.mock_performers):
            Album.objects.create(title=mock_title, performer=mock_performer, owner=self.test_user)

    def test_album_model(self):
        """Albums creation are correctly identified"""
        breakfast_in_america_album = Album.objects.get(title="Breakfast in America")
        mtv_unplugged_album = Album.objects.get(title="MTV Unplugged")
        self.assertEqual(breakfast_in_america_album.owner.usertitle, "testuser")
        self.assertEqual(mtv_unplugged_album.owner.usertitle, "testuser")
        self.assertEqual(breakfast_in_america_album.performer, "Supertramp")
        self.assertEqual(mtv_unplugged_album.performer, "Eric Clapton")

    def test_album_list(self):
        for mock_title, mock_performer in zip(self.mock_titles, self.mock_performers):
            album_test = Album.objects.get(title=mock_title)
            self.assertEqual(album_test.owner.usertitle, "testuser")
            self.assertEqual(album_test.performer, mock_performer)
