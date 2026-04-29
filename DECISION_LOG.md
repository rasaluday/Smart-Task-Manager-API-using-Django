# DECISION LOG

## 1. Time Breakdown

- 20 minutes: Read and understood the assignment requirements
- 30 minutes: Decided tech stack and overall API structure
- 1 hour: Built Django REST API endpoints (POST, GET, PATCH)
- 45 minutes: Implemented smart feature (auto-priority suggestion)
- 30 minutes: Tested APIs using browser and Postman
- 45 minutes: Wrote README.md and DECISION_LOG.md
- 30 minutes: GitHub setup and final cleanup

Total time: ~4.5 hours

---

## 2. Where AI Was Used — and Why

I used AI in the following areas:

- Understanding the assignment requirements clearly
- Planning a minimal API structure using Django REST Framework
- Reviewing endpoint implementation logic
- Improving documentation (README and decision log)

Reason:
The assignment explicitly required AI usage. I used AI as a helper to speed up development and avoid basic mistakes, but I reviewed and modified all outputs.

---

## 3. Where AI Was NOT Used — and Why

I avoided using AI for final decision-making:

- Choosing Django instead of other frameworks
- Deciding to use in-memory storage instead of database
- Selecting only one smart feature
- Keeping the project minimal (no Docker, no authentication, no frontend)

Reason:
These decisions required understanding the assignment constraints and prioritizing simplicity.

---

## 4. At Least 2 Bad AI Outputs

### Bad Output 1

AI suggested using:
- PostgreSQL database
- Django models and migrations
- Docker setup

Why it was incorrect:
The assignment clearly states no database migrations and no production setup.

Fix:
I removed all unnecessary complexity and used simple in-memory storage.

---

### Bad Output 2

AI suggested implementing multiple AI features like:
- Task summarization
- Duplicate detection
- Priority suggestion

Why it was incorrect:
The assignment requires implementing only ONE smart feature.

Fix:
I implemented only auto-priority suggestion properly.

---

## 5. Trade-offs Made

I intentionally did NOT implement:

- Database persistence
- Authentication system
- Frontend UI
- Docker setup
- Multiple smart features
- Complex architecture

Reason:
The assignment focuses on speed, decision-making, and simplicity. A working solution within time is more valuable than an over-engineered incomplete solution.

---

## 6. What I Would Improve With More Time

If I had 2 more hours, I would:

- Add SQLite database for persistence
- Use Django serializers for better structure
- Improve priority logic using an actual AI/ML API
- Add input validation and error handling
- Write unit tests

---

## 7. Final Reflection

I focused on:
- Delivering a working API within time
- Keeping the solution simple and clean
- Following assignment constraints strictly

I avoided over-engineering and prioritized clarity and functionality.
