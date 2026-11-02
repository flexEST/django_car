# 🚗 AutoLux — Car Marketplace Platform

AutoLux is a Django-based car marketplace web application designed to make browsing and managing car listings simple and convenient.

Users can explore available vehicles, search and filter listings, view detailed vehicle information, and browse multiple car images through a dedicated photo gallery.

## ✨ Features

### 🚘 Car Listings
- Browse available car listings
- Search by brand and model
- Filter by fuel type
- Filter by maximum price
- View detailed car information
- Multiple images and dedicated photo galleries

### ⭐ Featured Cars
- Mark vehicles as featured listings
- Display featured cars separately on the homepage
- Manage featured listings through the admin panel

### 📦 Inventory & Sales Management

Each vehicle supports three sales statuses:

- **Available** — The vehicle is currently listed for sale.
- **Reserved** — The vehicle has been reserved.
- **Sold** — The vehicle has been sold.

Additional management features:
- Manage inventory quantities
- Update vehicle availability
- Add, edit, and manage car listings
- Manage listings through Django Admin

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Backend web framework |
| SQLite | Database |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Interactive functionality |
| Pillow | Image processing |

## 📁 Project Structure

```text
CarWebsite/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── cars/
│   ├── migrations/
│   ├── templates/
│   │   └── cars/
│   │       ├── home.html
│   │       └── detail.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── media/
│   └── cars/
│
├── .venv/
├── manage.py
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

```bash
cd CarWebsite
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django pillow
```

### 5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the website:

http://127.0.0.1:8000/

Admin panel:

http://127.0.0.1:8000/admin/

## 🗄️ Database Models

### Car

Stores the main information about each vehicle:

- Brand
- Model
- Manufacturing year
- Price
- Mileage
- Fuel type
- Transmission
- Main image
- Description
- Sales status
- Featured listing status
- Stock quantity
- Creation and update timestamps

### CarImage

Stores additional images associated with a vehicle. Each car has its own photo gallery.

## 🖥️ Admin Panel

The Django Admin panel allows administrators to:

- Add new vehicles
- Edit vehicle information
- Upload additional car images
- Change sales status
- Mark listings as featured
- Manage inventory quantities
- Search and filter car listings

## 📱 Responsive Design

AutoLux is designed to support different screen sizes:

- Desktop
- Tablet
- Mobile devices

## 🔒 Security Notes

- Never upload your `SECRET_KEY` or other sensitive credentials to GitHub.
- Avoid committing `.venv/`, `db.sqlite3`, and user-uploaded media files.
- Set `DEBUG = False` in production.
- Configure appropriate hosting and storage for uploaded media files.

## 🚀 Planned Features

- User registration and authentication
- User-submitted car listings
- Favorite vehicles
- Advanced search and filtering
- Seller contact system
- Vehicle comparison
- Advanced admin dashboard
- Online inquiry and reservation system

---

**AutoLux** — Making car shopping easier.

© AutoLux. All rights reserved.
