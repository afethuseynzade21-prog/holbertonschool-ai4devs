# Team Ideation

## Brainstormed Ideas
1. AI Study Buddy — helps students turn lecture notes into flashcards, quizzes, and study plans.
2. Smart Expense Splitter — helps groups record shared expenses and calculate who owes whom.
3. NearRide — connects drivers with empty seats to passengers travelling in the same or a nearby direction. ✅ Chosen

## Chosen Problem Statement
People travelling in the same or nearby directions often make separate journeys, even when drivers have empty seats. Passengers may struggle to find convenient transport, while drivers could make better use of their available seats. They need a simple platform to discover compatible trips, compare seat prices, and request a place.

## Chosen Idea
**NearRide — a route-based carpooling platform**

NearRide connects any driver and passenger whose routes and travel times are sufficiently compatible. Drivers publish planned trips, choose the number of available seats, and set a price per seat. Passengers search for trips, compare route and price details, and send a seat request. The driver accepts or declines the request.

NearRide is a ride-sharing platform for pre-planned journeys, not an on-demand taxi service.

## MVP Features
1. **User profiles and roles:** Users can register and use the platform as drivers, passengers, or both.
2. **Publish a trip:** Drivers enter origin, destination, departure date and time, available seats, vehicle details, and price per seat.
3. **Search and match trips:** Passengers search by origin, destination, date, and time. The system ranks trips using route proximity, direction, time compatibility, available seats, and price. An AI assistant can convert a natural-language search into structured search filters and explain why a result may match.
4. **Seat requests:** Passengers request one or more seats. Drivers accept or decline. Accepted requests reduce the available-seat count.
5. **Notifications and trip status:** Users receive in-app updates when a request is submitted or its status changes. Trips and requests show their current status.

## Out of Scope for MVP
- In-app card payments or payment processing
- Live GPS tracking
- In-app chat and voice calls
- Recurring-trip automation
- Ratings and reviews
- Complex route optimization or multi-stop trip planning
- Native iOS or Android applications

## Product Rules
- The driver sets the price per seat when publishing a trip.
- The price is visible before a passenger sends a request.
- The total requested amount is calculated as seats requested multiplied by price per seat.
- A request is not a confirmed booking until the driver accepts it.
- A driver cannot accept more seats than are available.
- Accepting a request decreases available seats; declining or cancelling a pending request does not.
- The MVP displays the agreed price but does not collect or transfer money.
- NearRide is for planned shared journeys, not on-demand taxi dispatch.
- Route matching is calculated by application logic. AI may parse natural-language search input and explain results, but it must not invent routes, availability, or prices.

## Team Roles
| Member | Role | Main responsibility |
|---|---|---|
| Afet Huseynzade | Product Owner / AI Prompt Strategist | Product scope, user stories, AI behavior, demo and documentation |
| Teammate 1 | Frontend Developer | Search, trip creation, results, and request interfaces |
| Teammate 2 | Backend / Database Developer | API, database, trip and seat-request rules |
| Teammate 3 | QA / UI-UX Lead | User flows, validation, testing, usability, and demo checks |

## Success Criteria
- A driver can publish a trip with a route, departure time, available seats, and price per seat.
- A passenger can search and see trips that meet the defined matching rules.
- A passenger can submit a seat request and the driver can accept or decline it.
- The available-seat count updates correctly after an accepted request.
- The live demo completes the driver-to-passenger booking flow without manual database edits.
- AI search parsing or match explanations assist the flow without replacing deterministic matching rules.
