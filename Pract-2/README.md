# Train Management System

This project is a simple Train Management System that handles train data, passenger bookings, and generates reports on train details and revenue. It is designed to be straightforward and easy to use, making it ideal for managing small to medium-sized train operations.

## Table of Contents
- [Files](#files)
- [Data Formats](#data-formats)
- [Functions](#functions)
- [Usage](#usage)
- [Example Output](#example-output)
- [License](#license)

## Files

- **`report_1.txt`**: Contains details of each train and the available seats.
- **`report_2.txt`**: Contains the total revenue earned from each train.
- **`passengers.csv`**: Contains passenger booking details.
- **`trainmanagement.py`**: The main script that processes train and passenger data, updates seat availability, calculates fare, and generates reports.

## Data Formats

### `report_1.txt`
**Train Details and Available Seats:**
```bash
Train ID: 1, Train Name: Express A, Source: Station X, Destination: Station Y, Available Seats: 86 
Train ID: 2, Train Name: Express B, Source: Station Y, Destination: Station Z, Available Seats: 139 
Train ID: 3, Train Name: Express C, Source: Station Z, Destination: Station X, Available Seats: 193
```
### `report_2.txt`
**Total Revenue Earned from Each Train:**
```bash
Train ID: 1, Train Name: Express A, Revenue: 1400 Train ID: 2, 
Train Name: Express B, Revenue: 1100 Train ID: 3, 
Train Name: Express C, Revenue: 700
```
### `passengers.csv`
**Passenger Booking Details:**
```bash
Passenger Name,Train ID,Number of Tickets,Tier 
Alice,1,2,Two Tier Bob,2,3,Three Tier Charlie,3,1,Two Tier 
David,1,5,Three Tier Eve,2,2,Two Tier Frank,3,4,Two Tier 
Grace,1,3,Three Tier Hannah,2,1,Two Tier Ivy,3,2,Three Tier 
Jack,1,4,Two Tier Karen,2,5,Three Tier
```

## Functions

- **`load_train_data(filename)`**: Loads train data from a CSV file.
- **`load_passenger_data(filename)`**: Loads passenger data from a CSV file.
- **`check_seat_availability(trains, train_id, num_tickets)`**: Checks if there are enough seats available on a train.
- **`update_seat_availability(trains, train_id, num_tickets, fare)`**: Updates the available seats and revenue for a train.
- **`generate_report_1(trains)`**: Generates a report of train details and available seats.
- **`generate_report_2(trains)`**: Generates a report of total revenue earned from each train.
- **`calculate_fare(num_tickets)`**: Calculates the fare for a given number of tickets.
- **`main()`**: The main function that processes the data and generates reports.

## Usage

1. Ensure you have the required CSV files (`trains.csv` and `passengers.csv`) in the same directory as `trainmanagement.py`.
2. Run the script:
   ```bash
   python trainmanagement.py
   ```
3. The script will process the data, update seat availability, calculate fare, and generate `report_1.txt` and `report_2.txt`.

## Example Output

**Booking Confirmation**
```bash
Booking confirmed for Alice on Train ID 1 for 2 tickets. Total Fare: 200
Booking confirmed for Bob on Train ID 2 for 3 tickets. Total Fare: 300
...
```

***`report1.txt`***
Train Details and Available Seats:
```bash
Train ID: 1, Train Name: Express A, Source: Station X, Destination: Station Y, Available Seats: 72
Train ID: 2, Train Name: Express B, Source: Station Y, Destination: Station Z, Available Seats: 128
Train ID: 3, Train Name: Express C, Source: Station Z, Destination: Station X, Available Seats: 186
```

***`report_2.txt`***
Total Revenue Earned from Each Train:
```bash
Train ID: 1, Train Name: Express A, Revenue: 1400
Train ID: 2, Train Name: Express B, Revenue: 1100
Train ID: 3, Train Name: Express C, Revenue: 700
```


## License

This project is licensed under the MIT License. See the LICENSE file for details.