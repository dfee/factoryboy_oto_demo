import factory


class Musician:
    call_count = 0

    def __init__(self, name=None, profile=None, best_song=None, worst_song=None):
        self.name = name
        self.profile = profile
        self.best_song = best_song
        self.worst_song = worst_song
        self.__class__.call_count += 1


class MusicianFactory(factory.Factory):
    name = factory.Faker('name')
    profile = factory.SubFactory(
        'music.profile.ProfileFactory',
        musician=None,
    )
    best_song = factory.SubFactory(
        'music.song.SongFactory',
        musician=None,
    )
    worst_song = factory.SubFactory(
        'music.song.SongFactory',
        musician=None,
    )

    @factory.post_generation
    def attach(self, create, extracted, **kwargs):
        if self.profile:
            self.profile.musician = self
        if self.best_song:
            self.best_song.musician = self
        if self.worst_song:
            self.worst_song.musician = self

    class Meta:
        model = Musician
