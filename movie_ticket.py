tickets = {
    "silver": 100,
    "gold": 200,
    "platinum": 300
}

print("Welcome to the Movie Ticket Booking System!")

print("silver ticket: Rs 100\ngold ticket: Rs 200\nplatinum ticket: Rs 300")

ticket_total = 0

while True:
    choice = input("Enter the type of ticket you want to book (silver/gold/platinum): ").lower().strip()
    if choice in tickets:
        ticket_total += tickets[choice]
        print(f"You have booked a {choice} ticket for Rs {tickets[choice]}.")
    else:
        print("Invalid ticket type. Please try again.")
    
    if input("Do you want to book another ticket? (yes/no) ").lower() != "yes":
        break
print(f"Total amount to be paid: Rs {ticket_total}")