# User Stories

## 1. Create a User Profile
As a visitor, I want to create a user profile so that I can publish trips or request seats.

**Acceptance criteria**
- I can register with the required account details.
- I can view and edit my basic profile information.
- The same account can act as a driver and a passenger.
- I must be signed in before creating a trip or sending a seat request.

## 2. Add a Vehicle
As a driver, I want to add my vehicle details so that passengers can see which vehicle is offered for a trip.

**Acceptance criteria**
- I can enter the vehicle make/model and passenger-seat capacity.
- Vehicle details are associated with my user profile.
- I can select one of my vehicles when publishing a trip.
- The system does not allow the trip's available seats to exceed the vehicle's passenger-seat capacity.

## 3. Publish a Trip
As a driver, I want to publish a planned trip so that passengers travelling in a similar direction can find it.

**Acceptance criteria**
- I can enter origin, destination, departure date, and departure time.
- I can select a vehicle and enter the number of available passenger seats.
- I can set a price per seat.
- Required fields are validated before the trip is published.
- The published trip appears in search results when it matches a passenger's search.

## 4. Search for Trips
As a passenger, I want to search by origin, destination, date, and time so that I can find a suitable shared journey.

**Acceptance criteria**
- I can enter origin and destination.
- I can select a travel date and preferred time or time range.
- I can optionally set a maximum price per seat.
- Results show route, departure time, available seats, and price per seat.
- I see a helpful message when no matching trips are found.

## 5. Understand Matching Results
As a passenger, I want to understand why a trip is shown as a match so that I can decide whether to request a seat.

**Acceptance criteria**
- The system ranks results using route proximity, direction, time compatibility, available seats, and price.
- The system does not show a trip as available when it has no remaining seats.
- An AI-assisted search can convert natural-language input into structured filters.
- Any AI explanation is based on actual trip data returned by the matching logic.
- If AI is unavailable, standard search and matching still work.

## 6. Request a Seat
As a passenger, I want to request one or more available seats so that the driver can decide whether to take me on the trip.

**Acceptance criteria**
- I can select the number of seats requested.
- I can see the price per seat and calculated total before submitting.
- I cannot request more seats than are currently available.
- A new request has a pending status until the driver responds.
- I can view the status of my request.

## 7. Accept or Decline a Seat Request
As a driver, I want to accept or decline a passenger's request so that I control who joins my trip.

**Acceptance criteria**
- I can view requests for my trips.
- I can see the passenger, requested seat count, and calculated total.
- I can accept or decline a pending request.
- The system prevents accepting requests that exceed remaining seats.
- Accepting a request updates the trip's available-seat count.
- A request cannot be accepted or declined more than once.

## 8. Receive Notifications
As a user, I want to receive notifications about my trip and seat-request activity so that I know when action is needed.

**Acceptance criteria**
- A driver receives a notification when a passenger submits a request.
- A passenger receives a notification when the driver accepts or declines.
- Notifications identify the relevant trip and request status.
- Users can see their notifications in the application.
- A notification failure does not corrupt the trip or request status.

## 9. Cancel a Pending Request
As a passenger, I want to cancel my pending seat request so that I can withdraw a request I no longer need.

**Acceptance criteria**
- I can cancel my own pending request.
- I cannot cancel another passenger's request.
- A cancelled request is no longer available for driver approval.
- Cancelling a pending request does not change the trip's available-seat count.

## 10. Manage My Published Trips
As a driver, I want to view and manage my published trips so that I can keep trip information accurate.

**Acceptance criteria**
- I can view trips that I created.
- I can see each trip's status and remaining seats.
- I can cancel a trip that has not been completed.
- A cancelled trip is not returned as an available search result.
- Passengers with affected requests are notified of cancellation.

## 11. View Booking and Trip Details
As a user, I want to view the details of a trip and its request so that I can check the agreed information.

**Acceptance criteria**
- I can see origin, destination, departure time, vehicle, and price per seat.
- A passenger can see the number of seats requested and total displayed price.
- A driver can see the status of requests for their trip.
- Users can only access private request details for trips in which they are involved or which they own.

## 12. Receive Clear Validation and Error Feedback
As a user, I want clear messages when an action fails so that I know what to correct or try again.

**Acceptance criteria**
- Missing or invalid required fields are identified.
- The application shows a loading state during searches and submissions.
- API or AI failures show a clear message and a retry option where appropriate.
- The application prevents duplicate submissions where possible.
- Errors do not cause available-seat counts or request statuses to become inconsistent.
