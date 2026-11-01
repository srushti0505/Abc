
rooms = {}

rooms["A"] = input("Enter status of Room A (Dirty/Clean): ").capitalize()
rooms["B"] = input("Enter status of Room B (Dirty/Clean): ").capitalize()

location = input("Enter starting location (A/B): ").upper()

while True:
    if rooms[location] == "Dirty":
        print("\nLocation:", location)
        print("Percept:", location, "is Dirty")
        print("Action: SUCK")
        rooms[location] = "Clean"

    else:
        if location == "A":
            print("\nLocation:", location)
            print("Percept:", location, "is Clean")
            print("Action: Move Right")
            location = "B"
        else:
            print("\nLocation:", location)
            print("Percept:", location, "is Clean")
            print("Action: Move Left")
            location = "A"

    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nBoth rooms are clean.")
        print("Agent Goal Achieved.")
        break
