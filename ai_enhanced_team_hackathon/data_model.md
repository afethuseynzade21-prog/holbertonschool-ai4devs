# Data Model

## Overview
The NearRide MVP uses five main entities: `User`, `Vehicle`, `Trip`, `SeatRequest`, and `Notification`.

## Entities

### 1. User
Represents a person using NearRide as a driver, passenger, or both.

| Field | Type | Description |
|---|---|---|
| id | UUID | Unique user identifier |
| name | string | User's display name |
| email | string | Unique email address |
| phone | string | Contact number |
| created_at | datetime | Account creation timestamp |

### 2. Vehicle
Represents a vehicle owned or used by a driver.

| Field | Type | Description |
|---|---|---|
| id | UUID | Unique vehicle identifier |
| owner_id | UUID | References `User.id` |
| make | string | Vehicle manufacturer |
| model | string | Vehicle model |
| plate_number | string | Vehicle registration number |
| passenger_seat_capacity | integer | Maximum passenger seats available for sharing |

### 3. Trip
Represents a planned journey published by a driver.

| Field | Type | Description |
|---|---|---|
| id | UUID | Unique trip identifier |
| driver_id | UUID | References `User.id` |
| vehicle_id | UUID | References `Vehicle.id` |
| origin | string | Starting location |
| destination | string | Destination location |
| departure_at | datetime | Planned departure date and time |
| available_seats | integer | Passenger seats currently available |
| price_per_seat | decimal | Driver's price for one passenger seat |
| status | enum | `active`, `cancelled`, or `completed` |
| created_at | datetime | Trip creation timestamp |

### 4. SeatRequest
Represents a passenger's request to reserve seats on a trip.

| Field | Type | Description |
|---|---|---|
| id | UUID | Unique request identifier |
| trip_id | UUID | References `Trip.id` |
| passenger_id | UUID | References `User.id` |
| seats_requested | integer | Number of seats requested |
| price_per_seat_at_request | decimal | Price shown when the request is submitted |
| total_price | decimal | `seats_requested * price_per_seat_at_request` |
| status | enum | `pending`, `accepted`, `declined`, or `cancelled` |
| created_at | datetime | Request creation timestamp |
| updated_at | datetime | Last status update timestamp |

### 5. Notification
Represents an in-app update for a user.

| Field | Type | Description |
|---|---|---|
| id | UUID | Unique notification identifier |
| user_id | UUID | References `User.id` |
| trip_id | UUID | References `Trip.id`, nullable |
| seat_request_id | UUID | References `SeatRequest.id`, nullable |
| message | string | Notification text |
| is_read | boolean | Whether the user has read it |
| created_at | datetime | Notification creation timestamp |

## Relationships

- One **User** can own many **Vehicles**.
- One **User** can publish many **Trips** as a driver.
- One **Vehicle** can be associated with many **Trips** over time.
- One **Trip** can receive many **SeatRequests**.
- One **User** can submit many **SeatRequests** as a passenger.
- One **User** can receive many **Notifications**.
- A **SeatRequest** belongs to one **Trip** and one passenger (**User**).

## Business Rules and Data Integrity

- `available_seats` cannot be negative.
- `seats_requested` must be greater than zero.
- A request can be accepted only if enough seats remain.
- Accepting a request decreases `Trip.available_seats` by `SeatRequest.seats_requested`.
- Declining or cancelling a pending request does not change available seats.
- The price per seat must be zero or greater; the MVP may apply a configurable minimum if required by product policy.
- `price_per_seat_at_request` stores the price shown when the passenger submitted the request, so later trip edits do not silently change an existing request's displayed total.
- The system must process acceptance and seat-count updates atomically to prevent overbooking.

## Example

A driver publishes a trip:
- Origin: Khirdalan
- Destination: 28 May, Baku
- Departure: 08:00
- Available seats: 3
- Price per seat: 5 AZN

A passenger requests 2 seats:
- `seats_requested`: 2
- `price_per_seat_at_request`: 5 AZN
- `total_price`: 10 AZN
- `status`: `pending`

If the driver accepts:
- Request status becomes `accepted`.
- Trip available seats decrease from 3 to 1.
