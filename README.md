# ServiceLink - Online Service Marketplace

ServiceLink is a full-stack marketplace platform built with Django, designed to connect service providers with customers. The application allows users to create professional listings, upload images via Cloudinary, search for services, and manage their personal portfolio with real-time value calculations.

* **Live Project**: [https://online-service-sorin-c2b78d35ddee.herokuapp.com/](https://online-service-sorin-c2b78d35ddee.herokuapp.com/)
* **GitHub Repository**: [https://github.com/Sori678/online-service-marketplace](https://github.com/Sori678/online-service-marketplace)

## 1. Project Goals

The project aims to provide a secure environment for local commerce:

* **User Empowerment**: Allow individuals to monetize their skills easily.
* **Reliability**: Use a robust backend with persistent cloud storage to ensure data integrity.
* **Clean UX**: Provide a responsive interface that works on all devices using Bootstrap 5.

## 2. User Experience (UX)

### User Stories

* **As a Visitor**: I want to browse services and use the search bar to find specific offerings.
* **As a Registered User**: I want to post new services with descriptions, prices, and images.
* **As an Owner**: I want to edit or delete my listings to keep my information accurate.
* **As a Professional**: I want to see the total financial value of my active ads on my dashboard.

### Design Process

* **Wireframes**: Initial sketches were created to ensure a mobile-first approach.
* **Color Palette**: A professional combination of blue, white, and dark gray was chosen to convey trust and clarity.
* **Typography**: Clean sans-serif fonts are used to maintain high readability across different screen sizes.

## 3. Agile Methodology

This project was developed using Agile principles. Tasks were managed via GitHub Projects, utilizing User Stories with specific Acceptance Criteria and prioritization (Must Have/Should Have labels).

The project board can be found here: [GitHub Project Board](https://github.com/users/Sori678/projects/20)

## 4. Features

* **Authentication**: Secure Login/Register/Logout flow using **Django Allauth**.
* **CRUD Management**: Full control over service listings (Create, Read, Update, Delete).
* **Media Management**: Persistent image hosting and transformation via **Cloudinary API**.
* **Portfolio Dashboard**: A private "My Services" page for every user with automated price summation.
* **Search Engine**: Real-time keyword-based filtering for the main service list.

## 5. Testing and Validation

### Validation Results

* **Python (PEP8)**: All code in `views.py`, `models.py`, and `settings.py` has been validated for PEP8 compliance.
* **HTML/CSS**: Validated using W3C Services; all templates use semantic HTML5.

### Manual Testing

| Test ID | Feature | Expected Result | Result |
| --- | --- | --- | --- |
| **t7** | Sign-Up | Form validates correctly; creates user and redirects to home. | Pass |
| **t8-t9** | Image Upload | Images are successfully sent to Cloudinary and displayed. | Pass |
| **t14-t15** | Deletion | A confirmation page appears before a record is deleted. | Pass |
| **t16** | Search | The query correctly filters results by title or description. | Pass |

## 6. Deployment

### Heroku Deployment

The project is deployed on Heroku with the following configuration:

1. **Environment Variables (Config Vars)**:
   * `SECRET_KEY`: Django's security key.
   * `DATABASE_URL`: Connection string for Heroku Postgres.
   * `CLOUDINARY_URL`: API environment variable for media storage.
   * `DISABLE_COLLECTSTATIC`: Set to `0` for production.
2. **Database**: Migrations were executed via Heroku CLI to set up the Postgres schema.
3. **Static Files**: Managed by **WhiteNoise** for efficient delivery in production.

### Local Installation

1. Clone the repo: `git clone https://github.com/Sori678/online-service-marketplace.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a local `env.py` (optional) or set environment variables.
4. Run `python manage.py migrate` and `python manage.py runserver`.

## 7. Technologies Used

* **Core**: Python, HTML5, CSS3, JavaScript.
* **Framework**: Django 6.0.
* **Storage**: Cloudinary (Media), Whitenoise (Static Files).
* **Server**: Gunicorn.
* **Libraries**: Pillow, Django-Allauth, dj-database-url, Psycopg2.

## 8. Credits

* **Code Institute**: For the pedagogical framework and support.
* **Cloudinary**: For the media management documentation.
* **Bootstrap**: For the responsive UI components.