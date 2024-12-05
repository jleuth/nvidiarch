# NVIDIArch

A web-based platform for tracking and rating the stability, features, and general usage of NVIDIA drivers on Linux.

**The name "NVIDIArch" doesn't mean the platform is just for Arch! It just sounded nice.**

## Features
- Real-time display of the latest NVIDIA Linux driver version
- Community-driven rating system for driver releases
- Anonymous feedback submission
- Average rating calculation per driver
- Star-based rating visualization
- Chronological display of user reviews and comments

## Technical Stack
- Django web framework
- HTML/CSS frontend
- Press Start 2P font for retro styling
- SQLite database (default)

## Setup
1. Clone the repository
2. Install dependencies:
```bash
python -m venv venv && source venv/bin/activate && pip3 install django requests
```
3. Run migrations:
```bash
python manage.py migrate
```
4. Start development server:
```bash
python manage.py runserver
```

## Usage
- View latest driver ratings on the home page
- Submit new ratings via "Add a rating" page
- Each rating includes:
  - Driver version
  - Rating (1-5 stars)
  - Optional comment
  - Submission date

## Contributing
Feel free to submit issues and pull requests to help improve the platform.

## License
OSCSL License
