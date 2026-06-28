"""
==========================================================
Hands-On 1: Web Framework Foundations & Django Project Setup
File: notes.py
==========================================================

Task 1: Understand the Request-Response Cycle
"""

# ==========================================================
# 1. Request-Response Cycle
# ==========================================================

"""
Example Request:
GET /api/courses/

Request Flow:

Browser
   |
   v
HTTP Request
   |
   v
WSGI / ASGI Server
   |
   v
Middleware
   |
   v
URL Router (urls.py)
   |
   v
View (views.py)
   |
   v
Model (models.py)
   |
   v
Database
   |
   v
Model returns data
   |
   v
View prepares Response
   |
   v
Middleware
   |
   v
HTTP Response
   |
   v
Browser

Explanation:

1. User enters the URL in the browser.
2. Browser sends an HTTP request.
3. Django receives the request through a WSGI or ASGI server.
4. Middleware processes the request (authentication, sessions, security, etc.).
5. URL dispatcher (urls.py) matches the requested URL.
6. The corresponding View function/class is called.
7. The View interacts with the Model if database access is needed.
8. The Model executes SQL queries on the database.
9. Retrieved data is returned to the View.
10. The View prepares an HTTP response (HTML or JSON).
11. Middleware processes the response.
12. The browser receives and displays the response.
"""

# ==========================================================
# 2. Middleware
# ==========================================================

"""
Middleware is software that sits between the incoming request
and the view, and also between the view and the outgoing response.

Request
   |
Middleware
   |
View
   |
Middleware
   |
Response

Common uses of Middleware:
- Authentication
- Authorization
- Session management
- Security
- Logging
- Caching
"""

"""
Built-in Django Middleware Examples

1. AuthenticationMiddleware
   - Identifies the currently logged-in user.
   - Makes request.user available.

2. CsrfViewMiddleware
   - Protects against Cross-Site Request Forgery (CSRF) attacks.
   - Verifies CSRF tokens in POST requests.
"""

# ==========================================================
# 3. WSGI vs ASGI
# ==========================================================

"""
WSGI (Web Server Gateway Interface)

- Traditional Python web standard.
- Handles requests synchronously.
- One request is processed at a time.
- Suitable for:
    * CRUD applications
    * REST APIs
    * Admin dashboards

Examples:
- Gunicorn
- uWSGI
"""

"""
ASGI (Asynchronous Server Gateway Interface)

- Modern Python web standard.
- Supports asynchronous programming.
- Handles multiple concurrent requests.
- Supports:
    * WebSockets
    * Async Views
    * Long-running connections
    * Real-time applications

Examples:
- Uvicorn
- Daphne
- Hypercorn
"""

"""
Differences

WSGI
-----
- Synchronous
- No WebSocket support
- Better for traditional web apps

ASGI
-----
- Asynchronous
- Supports WebSockets
- Better for chat apps, notifications,
  live dashboards and streaming
"""

"""
Which one does Django use by default?

Traditionally, Django uses WSGI for deployment.
Modern Django projects also include an ASGI configuration
(asgi.py), allowing deployment with ASGI servers when
asynchronous features such as WebSockets or async views
are required.
"""

# ==========================================================
# 4. MVC vs MVT
# ==========================================================

"""
MVC Architecture

Model
    |
Controller
    |
View (UI)

Model
- Manages database
- Business logic
- Data operations

View
- User Interface
- HTML pages

Controller
- Receives requests
- Calls Model
- Returns View
"""

"""
Django follows MVT Architecture

Model
    |
View
    |
Template

Model
- Database tables
- Data access
- Business data

View
- Receives HTTP requests
- Processes logic
- Calls Models
- Returns responses

Template
- Presentation layer
- HTML
- CSS
- Displays data
"""

"""
MVC to MVT Mapping

MVC                  Django MVT
-----------------------------------------
Model      ----->    Model
View(UI)   ----->    Template
Controller ----->    View

In Django, the View performs the role of the Controller in MVC.
"""

