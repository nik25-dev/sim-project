

# 1. In-memory history tracking database
booking_history = {}


# 2. Function to log a booking with a timestamp
def add_booking(user, item):
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    booking_history.setdefault(user, []).append(f"[{time_str}] {item}")


# 3. Add sample records and display results
add_booking("Alice", "Flight to Paris (Confirmed)")
add_booking("Alice", "Hotel Stay (Cancelled)")
print("\n".join(booking_history.get("Alice", ["No bookings"])))
