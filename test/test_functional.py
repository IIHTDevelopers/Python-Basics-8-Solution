import unittest
import sys
import os

# Adjusting the path to import TestUtils and the required modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from FlightReservationSystem import list_all_flights, available_seats_for_flight, total_revenue_for_all_flights
from MovieTicketBookingSystem import total_tickets_sold, highest_revenue_movie
from students import count_number_of_days_using_dates, find_most_absent_student


class TestFunctional(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

    def test_list_all_flights(self):
        """
        Test case for list_all_flights() function.
        """
        try:
            result = list_all_flights()
            # Check if the result is a DataFrame with the expected columns
            expected_columns = ["Flight Number", "Airline", "Total Seats", "Booked Seats", "Ticket Price"]
            if all(column in result.columns for column in expected_columns) and len(result) == 3:
                self.test_obj.yakshaAssert("TestListAllFlights", True, "functional")
                print("TestListAllFlights = Passed")
            else:
                self.test_obj.yakshaAssert("TestListAllFlights", False, "functional")
                print("TestListAllFlights = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestListAllFlights", False, "functional")
            print(f"TestListAllFlights = Failed | Exception: {e}")

    def test_available_seats_for_flight(self):
        """
        Test case for available_seats_for_flight(flight_number) function.
        """
        try:
            # Test with a valid flight number
            result = available_seats_for_flight("AI101")
            expected_result = 30  # 150 total - 120 booked
            if result == expected_result:
                self.test_obj.yakshaAssert("TestAvailableSeatsForFlight", True, "functional")
                print("TestAvailableSeatsForFlight = Passed")
            else:
                self.test_obj.yakshaAssert("TestAvailableSeatsForFlight", False, "functional")
                print("TestAvailableSeatsForFlight = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestAvailableSeatsForFlight", False, "functional")
            print(f"TestAvailableSeatsForFlight = Failed | Exception: {e}")

    def test_total_revenue_for_all_flights(self):
        """
        Test case for total_revenue_for_all_flights() function.
        """
        try:
            result = total_revenue_for_all_flights()
            # Calculate expected revenue: (120 * 8000) + (160 * 12000) + (190 * 10000)
            expected_result = 120 * 8000 + 160 * 12000 + 190 * 10000
            if result == expected_result:
                self.test_obj.yakshaAssert("TestTotalRevenueForAllFlights", True, "functional")
                print("TestTotalRevenueForAllFlights = Passed")
            else:
                self.test_obj.yakshaAssert("TestTotalRevenueForAllFlights", False, "functional")
                print("TestTotalRevenueForAllFlights = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalRevenueForAllFlights", False, "functional")
            print(f"TestTotalRevenueForAllFlights = Failed | Exception: {e}")

    def test_total_tickets_sold(self):
        """
        Test case for total_tickets_sold() function.
        """
        try:
            result = total_tickets_sold()
            # Expected total: 7 + 4 + 11 = 22
            expected_result = 22
            if result == expected_result:
                self.test_obj.yakshaAssert("TestTotalTicketsSold", True, "functional")
                print("TestTotalTicketsSold = Passed")
            else:
                self.test_obj.yakshaAssert("TestTotalTicketsSold", False, "functional")
                print("TestTotalTicketsSold = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestTotalTicketsSold", False, "functional")
            print(f"TestTotalTicketsSold = Failed | Exception: {e}")

    def test_highest_revenue_movie(self):
        """
        Test case for highest_revenue_movie() function.
        """
        try:
            result = highest_revenue_movie()
            # Expected: "The Dark Knight" with revenue 11 * 300 = 3300
            expected_movie = "The Dark Knight"
            expected_revenue = 3300
            if result[0] == expected_movie and result[1] == expected_revenue:
                self.test_obj.yakshaAssert("TestHighestRevenueMovie", True, "functional")
                print("TestHighestRevenueMovie = Passed")
            else:
                self.test_obj.yakshaAssert("TestHighestRevenueMovie", False, "functional")
                print("TestHighestRevenueMovie = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestHighestRevenueMovie", False, "functional")
            print(f"TestHighestRevenueMovie = Failed | Exception: {e}")

    def test_count_number_of_days_using_dates(self):
        """
        Test case for count_number_of_days_using_dates() function.
        """
        try:
            result = count_number_of_days_using_dates()
            # Expected: 3 unique dates in the attendance records
            expected_result = 3
            if result == expected_result:
                self.test_obj.yakshaAssert("TestCountNumberOfDaysUsingDates", True, "functional")
                print("TestCountNumberOfDaysUsingDates = Passed")
            else:
                self.test_obj.yakshaAssert("TestCountNumberOfDaysUsingDates", False, "functional")
                print("TestCountNumberOfDaysUsingDates = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCountNumberOfDaysUsingDates", False, "functional")
            print(f"TestCountNumberOfDaysUsingDates = Failed | Exception: {e}")

    def test_find_most_absent_student(self):
        """
        Test case for find_most_absent_student() function.
        """
        try:
            result = find_most_absent_student()
            # Expected: "Alice Johnson" with 3 days absent
            expected_name = "Alice Johnson"
            expected_days = 3
            if result[0] == expected_name and result[1] == expected_days:
                self.test_obj.yakshaAssert("TestFindMostAbsentStudent", True, "functional")
                print("TestFindMostAbsentStudent = Passed")
            else:
                self.test_obj.yakshaAssert("TestFindMostAbsentStudent", False, "functional")
                print("TestFindMostAbsentStudent = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestFindMostAbsentStudent", False, "functional")
            print(f"TestFindMostAbsentStudent = Failed | Exception: {e}")


if __name__ == '__main__':
    unittest.main()
