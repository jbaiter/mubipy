from nose.tools import raises

from mubi import Mubi

# Specify your Mubi-Login for testing
USER = ""
PASSWORD = ""

class TestMubi(object):
    def setUp(self):
        self.mubi = Mubi()
        self.mubi.login(USER, PASSWORD)

    def tearDown(self):
        del self.mubi

    def test_is_film_available(self):
        assert self.mubi.is_film_available(244)
        assert self.mubi.is_film_available(3723)
        assert not self.mubi.is_film_available(863)

    def test_get_play_url(self):
        assert "cleo-de-5-a-7_de_640W_600.m4v" in self.mubi.get_play_url(244)
        assert "branded-to-kill_de_640W_600.m4v" in self.mubi.get_play_url(576)

    @raises(Exception)
    def test_get_bad_play_url(self):
        self.mubi.get_play(863)

    def test_search_film(self):
        assert ((u'Nostalghia (1983)', 12580, "http://s3.amazonaws.com/auteurs_production/images/film/nostalghia/w448/nostalghia.jpg")
                in self.mubi.search_film("nostalghia"))

    def test_search_person(self):
        assert (u'Peter Tscherkassky',
                68993) in self.mubi.search_person("tscherkassky")

    def test_get_person_films(self):
        assert len(self.mubi.get_person_films(68993)) == 7

    def test_get_all_films(self):
        assert self.mubi.get_all_films()[0] == 53
        assert len(self.mubi.get_all_films()[1]) == 20
        assert len(self.mubi.get_all_films(page=2)[1]) == 20

    def test_get_all_programs(self):
        assert ((u'Films by Peter Tscherkassky', u'films-by-peter-tscherkassky--2',
                "http://s3.amazonaws.com/auteurs_production/program_images/305/films-by-peter-tscherkassky.jpg")
                in self.mubi.get_all_programs())

    def test_get_program_films(self):
        assert len(self.mubi.get_program_films("films-by-peter-tscherkassky--2")) == 7

    def test_get_watchlist(self):
        assert ((u'From Morning to Midnight (Germany 1920)',
                36051, 'http://s3.amazonaws.com/auteurs_production/images/film/from-morning-to-midnight/w448/from-morning-to-midnight.jpg')
                in self.mubi.get_watchlist())
