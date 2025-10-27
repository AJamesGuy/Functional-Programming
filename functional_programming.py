movies = [
    {'title': 'The Matrix', 'year': 1999, 'rating': 8.7, 'genre': 'Sci-Fi'},
    {'title': 'Inception', 'year': 2010, 'rating': 8.8, 'genre': 'Thriller'},
    {'title': 'Pulp Fiction', 'year': 1994, 'rating': 8.9, 'genre': 'Crime'},
    {'title': 'The Godfather', 'year': 1972, 'rating': 9.2, 'genre': 'Crime'},
    {'title': 'Avatar', 'year': 2009, 'rating': 7.8, 'genre': 'Sci-Fi'},
    {'title': 'Titanic', 'year': 1997, 'rating': 7.8, 'genre': 'Romance'}
]


# TODO: Sort movies by rating (highest first)
by_rating = sorted(movies, key=lambda movie: movie['rating'], reverse=True)

# TODO: Sort movies by year (newest first) 
by_year = sorted(movies, key=lambda movie: movie['year'], reverse=True)

# Test your sorting
print("Highest rated:", by_rating[0]['title'])
print("Newest movie:", by_year[0]['title'])

# TODO: Create a lambda to classify movies by era
# - Year >= 2000: 'Modern'
# - Year >= 1990: 'Recent'  
# - Otherwise: 'Classic'
classify_era = lambda year: 'Modern' if year >= 2000 else 'Recent' if year >= 1990 else 'Classic'

# TODO: Create a lambda to determine rating category
# - Rating >= 9.0: 'Masterpiece'
# - Rating >= 8.0: 'Excellent'
# - Otherwise: 'Good'
rating_category = lambda rating: 'Masterpiece' if rating >= 9.0 else 'Excellent' if rating >= 8.0 else 'Good'

# Test your lambdas
print("Movie Classifications:")
for movie in movies:
    era = classify_era(movie['year'])
    category = rating_category(movie['rating'])
    print(f"{movie['title']}: {era}, {category}")
