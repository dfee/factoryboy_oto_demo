import factory


class Profile:
    call_count = 0

    def __init__(self, musician=None, phone_number=None):
        self.musician = musician
        self.phone_number = phone_number
        self.__class__.call_count += 1


class ProfileFactory(factory.Factory):
    musician = factory.SubFactory(
        'music.musician.MusicianFactory',
        profile=None,
    )
    phone_number = factory.Faker('phone_number')

    class Meta:
        model = Profile

    @factory.post_generation
    def attach(self, create, extracted, **kwargs):
        if self.musician:
            self.musician.profile = self
