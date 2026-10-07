import math


movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},  # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


# --- Этап 1. Переменные, числа, math ---
def average_rating(movies_list):
    return round(sum(m["rating"] for m in movies_list) / len(movies_list), 1)


def catalog_age_stats(movies_list, current_year=2026):
    ages = [current_year - m["year"] for m in movies_list]
    oldest = max(ages)
    newest = min(ages)
    avg = math.ceil(sum(ages) / len(ages))
    return oldest, newest, avg


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


# --- Этап 2. Условия и match ---
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо" if rating < 5 else "неизвестно"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# --- Этап 3. Циклы ---
def print_non_comedy_movies(movies_list):
    for m in movies_list:
        if "comedy" in m["genres"]:
            continue
        print(m["title"])


def find_first_masterpiece(movies_list):
    i = 0
    while i < len(movies_list):
        if movies_list[i]["rating"] > 9.0:
            print(f"Первый шедевр: {movies_list[i]['title']}")
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies_list, threshold=120):
    count = 0
    for m in movies_list:
        if m["duration_min"] > threshold:
            count += 1
    return count


# --- Этап 4. Строки ---
def normalize_title(title):
    words = title.split(" ")
    normalized = []
    for word in words:
        if not word:
            continue
        normalized.append(word[0].upper() + word[1:])
    return " ".join(normalized)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(list(movie["genres"])))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'


# --- Этап 5. Списки ---
def titles_sorted_by_rating(movies_list):
    return [m["title"] for m in sorted(movies_list, key=lambda x: x["rating"], reverse=True)]


def top_n_by_rating(movies_list, n=3):
    sorted_movies = sorted(movies_list, key=lambda x: x["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in sorted_movies[:n]]
