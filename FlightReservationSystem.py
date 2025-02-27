import numpy as np
import pandas as pd

# Static Dataset of Flights with Seats and Prices
flights_data = {
    "Flight Number": ["AI101", "BA202", "DL303"],
    "Airline": ["Air India", "British Airways", "Delta Airlines"],
    "Total Seats": [150, 180, 200],
    "Booked Seats": [120, 160, 190],
    "Ticket Price": [8000, 12000, 10000]  # Price per ticket in ₹
}

# Creating a DataFrame from the static data
flights_df = pd.DataFrame(flights_data)


# Function 1: List All Flights
def list_all_flights():
    """
    List all available flights with details.
    Uses Pandas DataFrame to display data in tabular format.
    """
    return flights_df


# Function 2: Check Available Seats for a Flight
def available_seats_for_flight(flight_number):
    """
    Returns the number of available seats for a given flight.
    Uses NumPy for numerical calculations.
    """
    flight = flights_df[flights_df["Flight Number"] == flight_number]
    if flight.empty:
        return f"Flight {flight_number} not found."

    total_seats = flight["Total Seats"].values[0]
    booked_seats = flight["Booked Seats"].values[0]

    # Using NumPy for calculation
    available_seats = np.subtract(total_seats, booked_seats)
    return available_seats


# Function 3: Calculate Total Revenue for All Flights
def total_revenue_for_all_flights():
    """
    Calculates total revenue generated from all booked seats.
    Uses Pandas operations for efficient calculations.
    """
    # Calculate revenue for each flight
    flights_df["Total Revenue"] = flights_df["Booked Seats"] * flights_df["Ticket Price"]

    # Sum up the revenue from all flights using Pandas
    total_revenue = flights_df["Total Revenue"].sum()
    return total_revenue


# Main Function to Execute and Display Results
def main():
    print("\n--- All Flights ---")
    print(list_all_flights())

    print("\n--- Available Seats for Each Flight ---")
    for flight in flights_df["Flight Number"]:
        available = available_seats_for_flight(flight)
        print(f"{flight}: {available} seats available")

    print("\n--- Total Revenue for All Flights ---")
    revenue = total_revenue_for_all_flights()
    print(f"Total Revenue: ₹{revenue}")

    # Return all calculated values
    return {
        "flights": list_all_flights(),
        "available_seats": {flight: available_seats_for_flight(flight) for flight in flights_df["Flight Number"]},
        "total_revenue": revenue
    }


if __name__ == "__main__":
    result = main()
    print("\n--- Final Result ---")
    print(result)
