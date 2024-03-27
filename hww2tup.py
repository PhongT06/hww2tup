#1

def format_itineraries(itineraries):
    formatted = []  
    itinerary_number = 1  
    for itinerary in itineraries:  
        traveler_name, origin, destination = itinerary  
        formatted_itinerary = f"Itinerary {itinerary_number}: {traveler_name} - From {origin} to {destination}"
        formatted.append(formatted_itinerary)  
        itinerary_number += 1  

    result = '\n'.join(formatted)
    return result  

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

output = format_itineraries(itineraries)
print(output)

#2###############################################################################

def add_book(library, title, author):
    new_book = (title, author)
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")
    else:
        print(f"Book '{title}' {author} is already in the library.")

library =[("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

add_book(library, "1984", "George Orwell")
add_book(library, "The Eye of the World", "Robert Jordan")
add_book(library, "The Great Hunt", "Robert Jordan")
add_book(library, "Brave New World", "Aldous Huxley")

print("Updated Library:")
print(library)


#3########################################################

def avg_closing_price(stock_data, stock_symbol):
    total_price = 0
    count = 0

    for symbol, _, closing_price in stock_data:
        if symbol == stock_symbol:
            total_price += closing_price
            count += 1
    if count == 0:
        return(f"'{stock_symbol}' not found.")
    else:
        return total_price / count

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("MSFT", "2021-01-01", 420.0)
]

analyze_symbol = "MSFT"
avg_price = avg_closing_price(stock_data, analyze_symbol)
print(f"Average closing price of {analyze_symbol}: ${avg_price}")

#3.2##################################################

def list(attendees, event_name):
    event_attendees = []  
    for attendee in attendees: 
        if attendee[1] == event_name:  
            event_attendees.append(attendee[0])  
    if event_attendees:  
        print(f"Attendees of {event_name}:")  
        for attendee_name in event_attendees: 
            print("-", attendee_name)  
    else:  
        print(f"No attendees found for event '{event_name}'")

def count(attendees):
    
    event_counts = {} 
    for attendee in attendees:  
        event = attendee[1]  
        if event in event_counts:  
            event_counts[event] += 1  
        else:  
            event_counts[event] = 1  
    print("Number of attendees per event:")  
    for event, count in event_counts.items():  
        print(f"- {event}: {count}")  

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    ("Diana", "AI Summit")
]

list(attendees, "Python Conference")
count(attendees)














