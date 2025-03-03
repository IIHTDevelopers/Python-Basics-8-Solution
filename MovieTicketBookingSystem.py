import json

# File to store movie data
FILE_NAME = "movie.json"


# Function to load movie data from a file
def load_movies():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Function 1: Total tickets sold for all movies
def total_tickets_sold(movies):
    return sum(movie["booked_seats"] for movie in movies.values())


# Function 2: Highest revenue movie
def highest_revenue_movie(movies):
    revenue_dict = {movie: data["booked_seats"] * data["ticket_price"] for movie, data in movies.items()}
    highest_revenue_movie = max(revenue_dict, key=revenue_dict.get)
    return highest_revenue_movie, revenue_dict[highest_revenue_movie]


# Main function to calculate and display results
def main():
    movies = load_movies()

    # Total tickets sold for all movies
    total_sold = total_tickets_sold(movies)
    print("\n--- Total Tickets Sold ---")
    print(total_sold)

    # Movie with highest revenue
    highest_revenue = highest_revenue_movie(movies)
    print("\n--- Highest Revenue Movie ---")
    print(f"{highest_revenue[0]} with ₹{highest_revenue[1]} revenue")

    return {
        "total_sold": total_sold,
        "highest_revenue": highest_revenue,
    }


if __name__ == "__main__":
    result = main()
    print("\n--- Final Result ---")
    print(result)