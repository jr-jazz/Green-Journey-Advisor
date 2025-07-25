# Green Journey Advisor

A web application for planning sustainable travel options, built with Flask, SQLite, Tailwind CSS, and JavaScript.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Green-Journey-Advisor.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the SQLite database:
   ```bash
   python src/database/init_db.py
   ```
5. Run the application:
   ```bash
   python src/app.py
   ```
6. Open `http://127.0.0.1:5000` in a browser.

## Features
- Homepage with a call-to-action to explore travel options.
- Travel options page displaying eco-friendly travel choices from a SQLite database.
- Form to add new travel options with validation.
- Responsive design for desktop, tablet, and mobile.
- Accessible interface with ARIA attributes and clear feedback.

## Project Structure
- `src/app.py`: Main Flask application.
- `src/templates/`: HTML templates for the interface.
- `src/static/`: CSS and JavaScript files.
- `src/database/`: SQLite database and initialization script.