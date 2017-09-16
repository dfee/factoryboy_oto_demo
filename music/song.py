import factory


class Song:
    call_count = 0

    def __init__(self, musician=None, name=None):
        self.musician = musician
        self.name = name
        self.__class__.call_count += 1


class SongFactory(factory.Factory):
    musician = factory.SubFactory(
        'music.musician.MusicianFactory',
        # Notice: unlike on ProfileFactory, we don't have to break the circular
        # dependency here! Though, we could not create best_song / worst_song...
        # best_song = None,
        # worst_song = None,
    )
    name = factory.Faker('sentence')

    class Meta:
        model = Song
