# User Stories: EcoRide Office Carpool MVP

Format: As a [user], I want [action], so that [benefit]. Each story has short acceptance criteria.

## Account

**1. Sign up with a company email**
As an employee, I want to sign up with my company email, so that only coworkers can use the app.
- Acceptance: sign-up is accepted only for the allowed company email domain; other domains show an error.

**2. Log in and log out**
As a registered user, I want to log in and log out, so that my rides and requests stay private.
- Acceptance: correct credentials open my account; wrong credentials show an error; logout ends the session.

## Driver

**3. Post a ride offer**
As a driver, I want to post a ride offer with a starting area, departure time and free seats, so that coworkers can join my commute.
- Acceptance: the offer is saved only when area, time and seats (at least 1) are filled in; it appears in search results.

**4. Cancel my ride offer**
As a driver, I want to cancel my ride offer, so that riders do not wait for a ride that will not happen.
- Acceptance: a cancelled offer disappears from search; riders with accepted requests see the cancelled status.

**5. Accept or decline seat requests**
As a driver, I want to accept or decline seat requests, so that I decide who rides with me.
- Acceptance: I see all pending requests for my offer; accepting reduces the free seats by one; I cannot accept more riders than free seats.

## Rider

**6. Search for rides**
As a rider, I want to search ride offers by area and time, so that I can find a ride that fits my commute.
- Acceptance: results show only active offers with at least one free seat that match the area and time; an empty result shows a clear message.

**7. Request a seat**
As a rider, I want to request a seat on a ride, so that the driver knows I want to join.
- Acceptance: I can send only one request per offer; the request starts with the status "pending".

**8. See the status of my requests**
As a rider, I want to see whether my requests are pending, accepted or declined, so that I can plan my commute.
- Acceptance: my requests list shows the current status and the ride details (area, time, driver name).

## History

**9. View trip history with estimated CO2 saved**
As a user, I want to see my completed shared rides and an estimated CO2 saving, so that I can see the benefit of carpooling.
- Acceptance: the history lists my completed rides; the CO2 value is clearly labeled as an estimate.
