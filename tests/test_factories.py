from music.musician import (
    Musician,
    MusicianFactory,
)
from music.profile import (
    Profile,
    ProfileFactory,
)
from music.song import (
    Song,
    SongFactory,
)


def _reset_call_counts():
    Musician.call_count = 0
    Profile.call_count = 0
    Song.call_count = 0


def test_call_musician_factory():
    """
    Expecting Musician to have profile, best_song, worst_song
    """
    _reset_call_counts()
    musician = MusicianFactory()

    # Musician asserts
    assert musician.name is not None
    assert Musician.call_count == 1

    # Profile asserts
    profile = musician.profile
    assert profile is not None
    assert profile.phone_number is not None
    assert Profile.call_count == 1

    # Song asserts
    seen_songs = set()
    for attr_name in ('best_song', 'worst_song'):
        song = getattr(musician, attr_name)
        assert song is not None
        assert song not in seen_songs
        seen_songs.add(song)
        assert song.name is not None
        assert song.musician == musician
    assert Song.call_count == 2


def test_call_song_factory():
    """
    Expecting Song to have musician with profile, but without best_song,
    worst_song
    """
    _reset_call_counts()
    song = SongFactory()

    # Musician asserts
    musician = song.musician
    assert musician is not None
    assert musician.name is not None
    assert Musician.call_count == 1

    # Profile asserts
    profile = musician.profile
    assert profile is not None
    assert profile.phone_number is not None
    assert Profile.call_count == 1

    # Song asserts
    seen_songs = set([song])
    assert song.name is not None
    for attr_name in ('best_song', 'worst_song'):
        song = getattr(musician, attr_name)
        assert song is not None
        assert song not in seen_songs
        seen_songs.add(song)
        assert song.name is not None
        assert song.musician == musician
    assert Song.call_count == 3


def test_call_profile_factory():
    _reset_call_counts()
    profile = ProfileFactory()

    # Musician asserts
    musician = profile.musician
    assert musician is not None
    assert musician.name is not None
    assert Musician.call_count == 1

    # Profile asserts
    assert profile.phone_number is not None
    assert Profile.call_count == 1

    # Song asserts
    seen_songs = set()
    for attr_name in ('best_song', 'worst_song'):
        song = getattr(musician, attr_name)
        assert song is not None
        assert song not in seen_songs
        seen_songs.add(song)
        assert song.name is not None
        assert song.musician == musician
    assert Song.call_count == 2
