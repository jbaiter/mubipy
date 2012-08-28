from mubi import Mubi

# Specify your Mubi-Login for testing
USER = ""
PASSWORD = ""

class TestMubi(object):
    def setUp(self):
        self.mubi = Mubi(USER, PASSWORD)

    def tearDown(self):
        del self.mubi

    def test_is_film_available(self):
        assert self.mubi.is_film_available(244)

    def test_get_play_url(self):
        assert "cleo-de-5-a-7_de_640W_600.m4v" in self.mubi.get_play_url(244)

    def test_search_film(self):
        assert 12580 in self.mubi.search_film("nostalghia").values()

    def test_search_person(self):
        assert 68993 in self.mubi.search_person("tscherkassky").values()

    def test_get_person_films(self):
        assert len(self.mubi.get_person_films(68993)) == 7

    def test_get_all_films(self):
        assert len(self.mubi.get_all_films()) == 20
        assert len(self.mubi.get_all_films(page=2)) == 20

    def test_get_all_programs(self):
        assert "Films by Peter Tscherkassky" in self.mubi.get_all_programs()

    def test_get_program_films(self):
        assert len(self.mubi.get_program_films("http://mubi.com/programs/films-by-peter-tscherkassky--2")) == 7