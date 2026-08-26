# Media Catalogue

A Python Object-Oriented Programming project for managing movies and TV series inside a reusable media catalogue.

The application supports media validation, inheritance between media types, filtering catalogue items, custom exceptions, and formatted catalogue output.

This project was created as part of my Python and Object-Oriented Programming practice through freeCodeCamp.

## Features

* Create and validate movie objects
* Create TV series using inheritance
* Store multiple media types in one catalogue
* Retrieve movies separately from TV series
* Validate titles, release years, directors, and durations
* Validate TV series seasons and episode counts
* Raise custom exceptions for unsupported media objects
* Display formatted catalogue output
* Use inheritance and method overriding

## Concepts Practiced

This project demonstrates:

* Object-Oriented Programming
* Classes and objects
* Inheritance
* Method overriding
* `super()`
* Polymorphism
* Custom exceptions
* Input validation
* `isinstance()`
* Type checking
* List comprehensions
* Encapsulation of business logic
* `__str__` methods

## Project Structure

```text
workshop-media-catalogue-FCC/
│
├── README.md
├── main.py
├── .gitignore
├── LICENSE
└── tests/
    └── test_media_catalogue.py
```

## How It Works

The application contains four main components:

* `Movie`
* `TVSeries`
* `MediaCatalogue`
* `MediaError`

The `Movie` class acts as the base media type, while `TVSeries` inherits from it and adds series-specific properties.

The `MediaCatalogue` stores both types and provides methods for filtering them.

## Movie

The `Movie` class represents a movie with:

* title
* release year
* director
* duration

Example:

```python
movie = Movie(
    "The Matrix",
    1999,
    "The Wachowskis",
    136
)
```

Printing the movie returns:

```text
The Matrix (1999) - 136 min, The Wachowskis
```

## Movie Validation

The constructor validates all provided data.

A movie must have:

* a non-empty title
* a release year of `1895` or later
* a non-empty director
* a duration greater than `0`

Invalid data raises a `ValueError`.

Example:

```python
Movie("", 1999, "Director", 120)
```

raises:

```text
ValueError: Title cannot be empty
```

## TVSeries

`TVSeries` inherits from `Movie`.

```python
class TVSeries(Movie):
    ...
```

This allows a TV series to reuse:

* title
* year
* director
* duration
* base validation logic

while adding:

* seasons
* total episodes

Example:

```python
series = TVSeries(
    "Breaking Bad",
    2008,
    "Vince Gilligan",
    47,
    5,
    62
)
```

## TV Series Validation

A TV series must have:

```text
seasons >= 1
total_episodes >= 1
```

Invalid values raise a `ValueError`.

## Inheritance

Instead of repeating all movie initialization logic, `TVSeries` uses:

```python
super().__init__(title, year, director, duration)
```

This calls the constructor of the parent `Movie` class.

The `TVSeries` class also overrides `__str__` to provide a representation appropriate for a television series.

## Custom Exceptions

The project defines a custom exception:

```python
class MediaError(Exception):
    ...
```

This is used when an invalid object is added to the catalogue.

For example:

```python
catalogue.add("The Matrix")
```

raises a `MediaError` because the catalogue accepts only `Movie` or `TVSeries` instances.

The exception also stores the invalid object:

```python
e.obj
```

which can be useful for debugging and error reporting.

## Media Catalogue

The `MediaCatalogue` class stores media objects inside:

```python
self.items
```

A new catalogue can be created with:

```python
catalogue = MediaCatalogue()
```

## Adding Media

Movies and TV series can be added using:

```python
catalogue.add(movie)
catalogue.add(series)
```

The catalogue validates that the provided object is a supported media type.

## Filtering Movies

The `get_movies()` method returns only objects whose exact type is `Movie`.

```python
movies = catalogue.get_movies()
```

## Filtering TV Series

The `get_tv_series()` method returns all `TVSeries` objects.

```python
series = catalogue.get_tv_series()
```

## Catalogue Representation

An empty catalogue prints:

```text
Media Catalogue (empty)
```

A catalogue containing media produces formatted output grouped by type.

Example:

```text
Media Catalogue (4 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
2. Inception (2010) - 148 min, Christopher Nolan
=== TV SERIES ===
1. Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
2. Breaking Bad (2008) - 5 seasons, 62 episodes, 47 min avg, Vince Gilligan
```

## Usage Example

```python
catalogue = MediaCatalogue()

movie1 = Movie(
    "The Matrix",
    1999,
    "The Wachowskis",
    136
)

movie2 = Movie(
    "Inception",
    2010,
    "Christopher Nolan",
    148
)

series1 = TVSeries(
    "Scrubs",
    2001,
    "Bill Lawrence",
    24,
    9,
    182
)

series2 = TVSeries(
    "Breaking Bad",
    2008,
    "Vince Gilligan",
    47,
    5,
    62
)

catalogue.add(movie1)
catalogue.add(movie2)
catalogue.add(series1)
catalogue.add(series2)

print(catalogue)
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/workshop-media-catalogue-FCC.git
```

Move into the project directory:

```bash
cd workshop-media-catalogue-FCC
```

Run the application:

```bash
python main.py
```

## Requirements

* Python 3.9+
* No external dependencies required

## Testing

The project can be tested using `pytest`.

Install pytest:

```bash
pip install pytest
```

Run the tests:

```bash
pytest
```

## Future Improvements

Possible improvements include:

* Search media by title
* Filter by release year
* Sort catalogue entries
* Ratings and genres
* Media IDs
* Catalogue persistence using JSON
* Database storage
* Additional media types
* Command-line interface
* Type hints
* Improved validation

## Project Source

This project is based on a freeCodeCamp Python workshop and was implemented as part of my Python learning and portfolio development.
