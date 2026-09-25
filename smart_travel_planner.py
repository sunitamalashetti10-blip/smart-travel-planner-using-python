"""Beginner-friendly console Smart Travel Planner."""


def get_positive_integer(prompt):
    """Read an integer greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")


def get_non_negative_float(prompt):
    """Read a number that is zero or greater."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Cost cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_transportation_cost(cost_per_traveler, traveler_count):
    return cost_per_traveler * traveler_count


def calculate_hotel_cost(cost_per_day, travel_days):
    return cost_per_day * travel_days


def calculate_food_cost(cost_per_traveler_per_day, traveler_count, travel_days):
    return cost_per_traveler_per_day * traveler_count * travel_days


def calculate_activity_cost(cost_per_traveler, traveler_count):
    return cost_per_traveler * traveler_count


def calculate_overall_trip_cost(
    transportation_cost, hotel_cost, food_cost, activity_cost
):
    return transportation_cost + hotel_cost + food_cost + activity_cost


def calculate_cost_per_traveler(overall_cost, traveler_count):
    return overall_cost / traveler_count


def calculate_average_daily_cost(overall_cost, travel_days):
    return overall_cost / travel_days


def collect_travel_information():
    """Collect and organize the travel inputs in a dictionary."""
    travel = {
        "name": input("Travel name: ").strip(),
        "destination": input("Destination: ").strip(),
        "traveler_count": get_positive_integer("Number of travelers: "),
        "travel_days": get_positive_integer("Number of travel days: "),
        "transportation_cost_per_traveler": get_non_negative_float(
            "Transportation cost per traveler: "
        ),
        "hotel_cost_per_day": get_non_negative_float("Hotel cost per day: "),
        "food_cost_per_traveler_per_day": get_non_negative_float(
            "Food cost per traveler per day: "
        ),
        "activity_cost_per_traveler": get_non_negative_float(
            "Activity cost per traveler: "
        ),
    }
    return travel


def display_summary(travel, costs):
    """Display the collected information and calculated costs."""
    print("\n" + "=" * 52)
    print("SMART TRAVEL PLANNER - TRIP SUMMARY")
    print("=" * 52)
    print(f"Travel name:       {travel['name'] or 'Unnamed trip'}")
    print(f"Destination:       {travel['destination'] or 'Not provided'}")
    print(f"Travelers:         {travel['traveler_count']}")
    print(f"Travel days:       {travel['travel_days']}")
    print("-" * 52)
    print(f"Transportation:    ${costs['transportation']:,.2f}")
    print(f"Hotel:             ${costs['hotel']:,.2f}")
    print(f"Food:              ${costs['food']:,.2f}")
    print(f"Activities:        ${costs['activities']:,.2f}")
    print("-" * 52)
    print(f"Overall trip cost: ${costs['overall']:,.2f}")
    print(f"Cost per traveler: ${costs['per_traveler']:,.2f}")
    print(f"Average daily cost: ${costs['daily_average']:,.2f}")
    print("=" * 52)


def main():
    print("Welcome to Smart Travel Planner")
    travel = collect_travel_information()

    transportation = calculate_transportation_cost(
        travel["transportation_cost_per_traveler"], travel["traveler_count"]
    )
    hotel = calculate_hotel_cost(
        travel["hotel_cost_per_day"], travel["travel_days"]
    )
    food = calculate_food_cost(
        travel["food_cost_per_traveler_per_day"],
        travel["traveler_count"],
        travel["travel_days"],
    )
    activities = calculate_activity_cost(
        travel["activity_cost_per_traveler"], travel["traveler_count"]
    )
    overall = calculate_overall_trip_cost(transportation, hotel, food, activities)

    costs = {
        "transportation": transportation,
        "hotel": hotel,
        "food": food,
        "activities": activities,
        "overall": overall,
        "per_traveler": calculate_cost_per_traveler(
            overall, travel["traveler_count"]
        ),
        "daily_average": calculate_average_daily_cost(overall, travel["travel_days"]),
    }
    display_summary(travel, costs)


if __name__ == "__main__":
    main()
