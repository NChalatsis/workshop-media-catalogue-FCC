import pytest

from main import (
    MediaError,
    Movie,
    TVSeries,
    MediaCatalogue,
)


def test_movie_creation():
    movie = Movie(
        "The Matrix",
        1999,
        "The Wachowskis",
        136
    )

    assert movie.title == "The Matrix"
    assert movie.year == 1999
    assert movie.director == "The Wachowskis"
    assert movie.duration == 136


def test_movie_string():
    movie = Movie(
        "Inception",
        2010,
        "Christopher Nolan",
        148
    )

    assert str(movie) == (
        "Inception (2010) - "
        "148 min, Christopher Nolan"
    )


def test_empty_movie_title():
    with pytest.raises(ValueError):
        Movie("", 2000, "Director", 120)


def test_invalid_movie_year():
    with pytest.raises(ValueError):
        Movie("Test", 1800, "Director", 120)


def test_empty_director():
    with pytest.raises(ValueError):
        Movie("Test", 2000, "", 120)


def test_invalid_duration():
    with pytest.raises(ValueError):
        Movie("Test", 2000, "Director", 0)


def test_tv_series_creation():
    series = TVSeries(
        "Breaking Bad",
        2008,
        "Vince Gilligan",
        47,
        5,
        62
    )

    assert series.title == "Breaking Bad"
    assert series.seasons == 5
    assert series.total_episodes == 62


def test_tv_series_is_movie():
    series = TVSeries(
        "Breaking Bad",
        2008,
        "Vince Gilligan",
        47,
        5,
        62
    )

    assert isinstance(series, Movie)


def test_invalid_seasons():
    with pytest.raises(ValueError):
        TVSeries(
            "Series",
            2020,
            "Director",
            45,
            0,
            10
        )


def test_invalid_episode_count():
    with pytest.raises(ValueError):
        TVSeries(
            "Series",
            2020,
            "Director",
            45,
            2,
            0
        )


def test_add_movie():
    catalogue = MediaCatalogue()

    movie = Movie(
        "The Matrix",
        1999,
        "The Wachowskis",
        136
    )

    catalogue.add(movie)

    assert movie in catalogue.items


def test_invalid_media_object():
    catalogue = MediaCatalogue()

    with pytest.raises(MediaError):
        catalogue.add("Not a media object")


def test_get_movies():
    catalogue = MediaCatalogue()

    movie = Movie(
        "The Matrix",
        1999,
        "The Wachowskis",
        136
    )

    series = TVSeries(
        "Breaking Bad",
        2008,
        "Vince Gilligan",
        47,
        5,
        62
    )

    catalogue.add(movie)
    catalogue.add(series)

    assert catalogue.get_movies() == [movie]


def test_get_tv_series():
    catalogue = MediaCatalogue()

    series = TVSeries(
        "Breaking Bad",
        2008,
        "Vince Gilligan",
        47,
        5,
        62
    )

    catalogue.add(series)

    assert catalogue.get_tv_series() == [series]


def test_empty_catalogue_string():
    catalogue = MediaCatalogue()

    assert str(catalogue) == "Media Catalogue (empty)"
