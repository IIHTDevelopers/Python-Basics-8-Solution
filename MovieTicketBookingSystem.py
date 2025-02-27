# Movie Ticket Booking System (Static Version with Realistic Data)

# Dataset of movies with seat availability and ticket price
movies = {
    "Avengers: Endgame": {
        "total_seats": 10,
        "booked_seats": 7,
        "ticket_price": 250  # Price per ticket in ₹
    },
    "Inception": {
        "total_seats": 8,
        "booked_seats": 4,
        "ticket_price": 200
    },
    "The Dark Knight": {
        "total_seats": 12,
        "booked_seats": 11,
        "ticket_price": 300
    }
}


# Function 1: Total tickets sold for all movies
def total_tickets_sold():
    total_sold = sum(movie["booked_seats"] for movie in movies.values())
    return total_sold


# Function 2: Highest revenue movie
def highest_revenue_movie():
    revenue_dict = {movie: movie_data["booked_seats"] * movie_data["ticket_price"] for movie, movie_data in
                    movies.items()}
    highest_revenue_movie = max(revenue_dict, key=revenue_dict.get)
    return highest_revenue_movie, revenue_dict[highest_revenue_movie]




# Main function to calculate and display the results
def main():
    # Total tickets sold for all movies
    total_sold = total_tickets_sold()
    print("\n--- Total Tickets Sold ---")
    print(total_sold)

    # Movie with highest revenue
    highest_revenue = highest_revenue_movie()
    print("\n--- Highest Revenue Movie ---")
    print(f"{highest_revenue[0]} with ₹{highest_revenue[1]} revenue")



    # Return all calculated values
    return {
        "total_sold": total_sold,
        "highest_revenue": highest_revenue,

    }


if __name__ == "__main__":
    result = main()
    print("\n--- Final Result ---")
    print(result)
