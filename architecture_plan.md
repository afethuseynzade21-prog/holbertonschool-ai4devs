# Architecture Plan

## 1. Overview
NearRide is a web-based carpooling platform for any driver and passenger travelling in the same or a nearby direction. Drivers publish planned trips, set the number of available seats and a price per seat. Passengers search for compatible trips and submit seat requests. Drivers accept or decline requests.

The MVP focuses on one complete flow: publish a trip → search and match → request seats → driver decision → notification and updated seat availability.

## 2. High-Level Architecture

```text
Browser / React Frontend
        |
        | HTTPS / JSON
        v
Backend REST API
        |
        +--------------------> PostgreSQL Database
        |                       - Users
        |                       - Vehicles
        |                       - Trips
        |                       - SeatRequests
        |                       - Notifications
        |
        +--------------------> Matching Engine
        |                       - Origin proximity
        |                       - Direction / destination compatibility
        |                       - Departure-time window
        |                       - Available seats
        |                       - Price filter and ranking
        |
        +--------------------> AI Service
                                - Natural-language search parsing
                                - Match explanation based on match results
```

## 3. Main Components

### Frontend
- Built with React.
- Provides registration/profile, trip creation, trip search/results, trip details, seat-request, and notification views.
- Shows price per seat and calculated total before a passenger submits a request.
- Communicates with the backend using HTTPS and JSON.
- Displays validation, loading, success, and error states.

### Backend API
- Built with Node.js/Express or Python/FastAPI.
- Handles users, vehicles, trips, seat requests, and notifications.
- Validates user input and enforces ownership/authorization rules.
- Calculates request totals using the stored price per seat.
- Accepts or declines requests and updates available seats.
- Performs seat acceptance and seat-count changes in a database transaction to prevent overbooking.

### Database
- PostgreSQL stores users, vehicles, trips, seat requests, and notifications.
- Uses UUID primary keys and foreign keys.
- Stores a price snapshot on each seat request so a later trip-price edit does not change an existing request's displayed total.
- Uses constraints to prevent negative seat counts and invalid request quantities.

### Matching Engine
- Uses deterministic application logic, not an LLM, for actual compatibility decisions.
- Filters by available seats, departure date/time, origin proximity, and destination/direction compatibility.
- Applies an optional maximum price filter.
- Ranks matching trips and returns the data used by the frontend.
- The MVP may use simplified location matching (normalized place names or coordinates when available); full route optimization is out of scope.

### AI Service
- Uses an external AI API through a backend-controlled endpoint.
- Converts a natural-language request, such as “Tomorrow morning from Masazir to central Baku, under 6 AZN,” into structured search filters.
- Can explain why a returned trip is a possible match using actual trip and matching data.
- Does not invent availability, prices, route distances, or booking status.
- If the AI provider is unavailable, users can still search using standard form fields and deterministic matching.
- API keys are stored in environment variables and are never exposed to the frontend or committed to Git.

## 4. API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/users` | Register a user |
| GET | `/api/users/me` | Get current user's profile |
| POST | `/api/vehicles` | Add a vehicle |
| GET | `/api/vehicles` | List current user's vehicles |
| POST | `/api/trips` | Publish a trip |
| GET | `/api/trips/search` | Search and rank matching trips |
| GET | `/api/trips/:id` | Get trip details |
| POST | `/api/trips/:id/requests` | Submit a seat request |
| GET | `/api/trips/:id/requests` | List requests for a driver's trip |
| PATCH | `/api/requests/:id/status` | Accept or decline a request |
| GET | `/api/notifications` | List current user's notifications |
| PATCH | `/api/notifications/:id/read` | Mark a notification as read |
| POST | `/api/ai/parse-search` | Convert natural-language search into structured filters |

## 5. Core Data Flow

### A. Publish a Trip
1. Driver signs in and selects a vehicle.
2. Driver enters origin, destination, departure date/time, available seats, and price per seat.
3. Frontend sends the trip details to the backend.
4. Backend validates the data and confirms the driver owns or can use the selected vehicle.
5. Backend saves the trip with `active` status.

### B. Search and Match
1. Passenger enters origin, destination, date/time, and optional maximum price.
2. Optionally, the AI service parses a natural-language query into structured filters.
3. Backend sends filters to the Matching Engine.
4. Matching Engine checks route/location compatibility, time, price, and available seats.
5. Backend returns ranked trip results with the data supporting each match.

### C. Request and Confirm Seats
1. Passenger selects a trip and number of seats.
2. Backend calculates the total using the current price per seat and creates a `pending` request.
3. Driver views the request and accepts or declines it.
4. On acceptance, backend uses a database transaction to verify remaining seats, update the request status, and decrement available seats.
5. Backend creates notifications for the relevant users.

## 6. Technology Choices
- Frontend: React
- Backend: Node.js with Express (or Python with FastAPI if the team is more comfortable with Python)
- Database: PostgreSQL
- AI provider: an LLM API accessed from the backend
- Version control: GitHub
- Deployment: Vercel for frontend; Render or Railway for backend and database

For the 24-hour MVP, use one backend framework and one deployment path; avoid adding Redis, microservices, or a separate queue.

## 7. Security and Reliability
- Use HTTPS in deployment.
- Keep credentials and AI API keys in environment variables.
- Validate and sanitize all user input on the backend.
- Require authentication for trip creation and seat requests.
- Enforce authorization: only the trip owner can accept or decline requests for that trip; users can view only their own private request details.
- Do not expose private phone or account details in public search results.
- Prevent overbooking with a database transaction and appropriate row-level locking or equivalent concurrency control.
- Do not treat an AI-generated explanation as proof of route compatibility; use matching-engine results as the source of truth.
- Show clear errors if the AI service or notification delivery fails.

## 8. Testing Plan
- Unit tests for input validation, price calculation, matching filters, and request status transitions.
- API tests for trip creation, trip search, seat requests, and accept/decline actions.
- Test that accepting requests cannot reduce available seats below zero, including concurrent requests.
- Test that declining/cancelling a pending request does not change available seats.
- Test that AI parsing failures fall back to manual search.
- End-to-end demo test: driver publishes a trip; passenger finds it; passenger requests a seat; driver accepts; seat count updates; notifications appear.

## 9. 24-Hour Delivery Plan

| Time | Goal |
|---|---|
| Hours 0–2 | Confirm MVP, roles, user stories, data model, repository setup |
| Hours 2–6 | Create database schema and core backend endpoints |
| Hours 4–9 | Build React screens for trip creation and search |
| Hours 8–13 | Implement deterministic matching and seat-request workflow |
| Hours 12–15 | Add AI search parsing and match explanation with fallback |
| Hours 15–18 | Add notifications, validation, and core tests |
| Hours 18–21 | Fix critical bugs and deploy |
| Hours 21–24 | Prepare README, demo data, pitch, and backup demo recording |

## 10. Demo Scenario
1. A driver publishes a Khirdalan-to-28-May trip for 08:00 with 3 available seats and a price of 5 AZN per seat.
2. A passenger searches from Masazir to 28 May for the same morning and sets a maximum price of 6 AZN.
3. NearRide returns the trip if it passes the configured location, direction, time, and seat rules.
4. The passenger requests 1 seat and sees a total of 5 AZN.
5. The driver accepts the request.
6. The trip's available seats decrease from 3 to 2 and both users see an in-app notification.
