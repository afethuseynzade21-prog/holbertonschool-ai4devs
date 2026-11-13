# User Stories: CarpoolConnect

Priority tags: MVP (needed for first release), High, Medium, Low.

### User Story 1
As an employee, I want to sign up with my work email so that only verified colleagues can use the carpool network.

**Acceptance Criteria**:
- User enters a work email address and receives a verification link.
- Only email domains registered by the company are accepted.
- The account is activated only after the link is confirmed.

**Priority**: MVP

### User Story 2
As a driver, I want to publish a recurring commute offer so that I can fill empty seats on my daily trips to work.

**Acceptance Criteria**:
- Driver enters a pickup area, work location, departure time, available seats, and the days of the week.
- The offer is saved and shown as a recurring weekly ride.
- Driver can edit or delete the offer at any time.

**Priority**: MVP

### User Story 3
As a passenger, I want to search for colleagues who drive along my route so that I can find a reliable ride to work.

**Acceptance Criteria**:
- User enters a pickup area, work location, and preferred arrival time.
- System displays matching drivers whose route and schedule fit within a defined time window.
- Search results appear in under 3 seconds.

**Priority**: MVP

### User Story 4
As a passenger, I want to request a seat on a driver's ride so that I can secure my commute.

**Acceptance Criteria**:
- Passenger can send a seat request for one ride or for all recurring days.
- Driver receives a notification and can accept or decline the request.
- Passenger is notified of the decision, and the number of free seats updates automatically.

**Priority**: MVP

### User Story 5
As a user, I want my exact home address to stay hidden until a ride is confirmed so that my privacy is protected.

**Acceptance Criteria**:
- Search results and profiles show only an approximate pickup zone.
- The exact pickup address is shared only after both the driver and passenger confirm the ride.
- Exact addresses are no longer visible after the ride is cancelled.

**Priority**: High

### User Story 6
As a user, I want to cancel or skip a single day of a ride so that I can handle remote days and last-minute changes.

**Acceptance Criteria**:
- User can cancel one day without cancelling the whole recurring ride.
- The other participants are notified immediately.
- Free seats are updated and shown in the search results again.

**Priority**: High

### User Story 7
As a passenger, I want to see the cost share before I confirm a ride so that I know exactly what I will pay.

**Acceptance Criteria**:
- The cost per ride is calculated from the distance and the number of passengers.
- The amount is displayed before the passenger confirms the request.
- The cost summary is available in the ride history after each trip.

**Priority**: High

### User Story 8
As a passenger, I want to rate my driver after a ride so that other colleagues can see whether the driver is reliable.

**Acceptance Criteria**:
- A rating from 1 to 5 stars with an optional comment is requested after each completed ride.
- The average rating appears on the driver's profile.
- Users can report a problem, which is sent to the company administrator.

**Priority**: Medium

### User Story 9
As a passenger, I want to share my ride details with a trusted contact so that I feel safe during my commute.

**Acceptance Criteria**:
- User can send ride details (driver name, vehicle, time, route area) to a chosen contact.
- Sharing is optional and can be turned off at any time.
- Shared details expire automatically after the ride ends.

**Priority**: Medium

### User Story 10
As an employee, I want to see how much CO2 I have saved by carpooling so that I can track my environmental impact.

**Acceptance Criteria**:
- The profile page shows the estimated CO2 saved per week and in total.
- The calculation is based on shared distance and the number of passengers.
- The method of calculation is explained in a short note on the same page.

**Priority**: Medium

### User Story 11
As a mobility manager, I want a dashboard with anonymized commute statistics so that I can measure the impact of the carpool program.

**Acceptance Criteria**:
- The dashboard shows the number of active users, shared rides, parking spots freed, and CO2 avoided.
- Only aggregated data is shown, with no personal information or home addresses.
- Data can be filtered by week, month, and office location.

**Priority**: High

### User Story 12
As a mobility manager, I want to define rewards for frequent carpoolers so that more employees join the program.

**Acceptance Criteria**:
- Manager can create a reward rule, for example priority parking after 10 shared rides in a month.
- The system tracks each employee's progress towards the reward.
- Employees receive a notification when they earn a reward.

**Priority**: Low
