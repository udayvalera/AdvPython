import csv

# Load Train Data
def load_train_data(filename):
	trains = {}
	with open(filename, mode='r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			train_id = row['Train ID']
			trains[train_id] = {
				'Train Name': row['Train Name'],
				'Source Station': row['Source Station'],
				'Destination Station': row['Destination Station'],
				'Total Seats': int(row['Total Seats']),
				'Available Seats': int(row['Total Seats']),
				'Revenue': 0
			}
	return trains

# Load Passenger Data
def load_passenger_data(filename):
	passengers = []
	with open(filename, mode='r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			passengers.append({
				'Passenger Name': row['Passenger Name'],
				'Train ID': row['Train ID'],
				'Number of Tickets': int(row['Number of Tickets'])
			})
	return passengers

# Check Seat Availability
def check_seat_availability(trains, train_id, num_tickets):
	if train_id not in trains:
		raise ValueError("Invalid Train ID")
	if trains[train_id]['Available Seats'] < num_tickets:
		raise ValueError("Insufficient Seats")
	return True

# Update Seat Availability
def update_seat_availability(trains, train_id, num_tickets, fare):
	trains[train_id]['Available Seats'] -= num_tickets
	trains[train_id]['Revenue'] += fare

# Generate Report 1
def generate_report_1(trains):
	with open('report_1.txt', 'w') as file:
		file.write("Train Details and Available Seats:\n")
		for train_id, details in trains.items():
			file.write(f"Train ID: {train_id}, Train Name: {details['Train Name']}, Source: {details['Source Station']}, Destination: {details['Destination Station']}, Available Seats: {details['Available Seats']}\n")

# Generate Report 2
def generate_report_2(trains):
	with open('report_2.txt', 'w') as file:
		file.write("Total Revenue Earned from Each Train:\n")
		for train_id, details in trains.items():
			file.write(f"Train ID: {train_id}, Train Name: {details['Train Name']}, Revenue: {details['Revenue']}\n")

# Fare Calculation (Example: Flat rate per ticket)
def calculate_fare(num_tickets):
	return num_tickets * 100  # Example fare rule: 100 currency units per ticket

# Main Function
def main():
	trains = load_train_data('trains.csv')
	passengers = load_passenger_data('passengers.csv')

	for passenger in passengers:
		train_id = passenger['Train ID']
		num_tickets = passenger['Number of Tickets']
		try:
			if check_seat_availability(trains, train_id, num_tickets):
				fare = calculate_fare(num_tickets)
				update_seat_availability(trains, train_id, num_tickets, fare)
				print(f"Booking confirmed for {passenger['Passenger Name']} on Train ID {train_id} for {num_tickets} tickets. Total Fare: {fare}")
		except ValueError as e:
			print(f"Error for {passenger['Passenger Name']}: {e}")

	generate_report_1(trains)
	generate_report_2(trains)

if __name__ == "__main__":
	main()
