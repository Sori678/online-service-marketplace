# ServiceLink - Online Service Marketplace

ServiceLink is a full-stack marketplace platform built with Django, designed to connect service providers with customers. The application allows users to create professional listings, upload images, search for services, and manage their personal portfolio with real-time value calculations.



## 1. Project Goals
The project aims to provide a secure environment for local commerce:
* **User Empowerment**: Allow individuals to monetize their skills easily.
* **Reliability**: Use a robust backend to ensure data persistence and security.
* **Clean UX**: Provide a responsive interface that works on all devices.

## 2. User Experience (UX)

### User Stories
* **As a Visitor**: I want to browse services and use the search bar to find specific offerings.
* **As a Registered User**: I want to post new services with descriptions, prices, and images.
* **As an Owner**: I want to edit or delete my listings to keep my information accurate.
* **As a Professional**: I want to see the total financial value of my active ads on my dashboard.

## 3. Features
* **Authentication**: Secure Login/Register/Logout flow using Django Allauth.
* **CRUD Management**: Full control over service listings (Create, Read, Update, Delete).
* **Image Processing**: Dynamic image uploading and resizing using the Pillow library.
* **Portfolio Dashboard**: A private "My Ads" page for every user.
* **Search Engine**: Keyword-based filtering for the main service list.

## 4. Manual Testing Documentation

I have performed extensive manual testing throughout the development lifecycle. Each test case below is linked to a visual proof located in the `/documentation` folder.

| Test ID | Feature | Expected Result | Visual Proof (Click to view) |
|---------|---------|-----------------|-----------------------------|
| **t1-t2** | Admin Panel | Successfully managed services via admin backend. | [View t1](./documentation/t1.png) / [t2](./documentation/t2.png) |
| **t3-t4** | UI Layout | Initial list converted to Bootstrap cards. | [View t3](./documentation/t3.png) / [t4](./documentation/t4.png) |
| **t5-t6** | Navbar | Navigation links change based on session. | [View t5](./documentation/t5.png) / [t6](./documentation/t6.png) |
| **t7** | Allauth | Functional Sign-Up form with validation. | [View t7](./documentation/t7.png) |
| **t8-t9** | Forms | Service data is correctly captured and saved. | [View t8](./documentation/t8.png) / [t9](./documentation/t9.png) |
| **t10-t11** | Database | Multiple services display correctly with details. | [View t10](./documentation/t10.png) / [t11](./documentation/t11.png) |
| **t12-t13** | Feedback | Success alerts appear after login/update. | [View t12](./documentation/t12.png) / [t13](./documentation/t13.png) |
| **t14-t15** | Security | Confirm prompt appears before deletion. | [View t14](./documentation/t14.png) / [t15](./documentation/t15.png) |
| **t16** | Search | Search bar returns results for keywords. | [View t16](./documentation/t16.png) |
| **t17-t18** | Logic | Dashboard correctly sums portfolio prices. | [View t17](./documentation/t17.png) / [t18](./documentation/t18.png) |
| **t19-t21** | Media | Images render correctly in cards and details. | [View t19](./documentation/t19.png) / [t20](./documentation/t20.png) |
| **t22** | Polish | Final responsive detail view with action buttons. | [View t22](./documentation/t22.png) |

## 5. Technologies Used
* **Languages**: Python, HTML5, CSS3, JavaScript.
* **Framework**: Django 5.x.
* **Libraries**: Pillow, Django-Allauth.
* **Database**: SQLite3.

## 6. Credits
* **Code Institute**: For the project framework and support.

## 7. Credits
* **Code Institute**: For the pedagogical framework.
* **Django Documentation**: For technical guidance.

# Online Service Marketplace

* Link-ul GitHub: https://github.com/Sori678/online-service-marketplace

* Link-ul Live Heroku: https://online-service-sorin-c2b78d35ddee.herokuapp.com/