# Role Game Management System

A comprehensive Django-based role-playing game management system that facilitates character creation and game administration through distinct user roles: Players and Game Masters.

## 🎮 Features

### Player Features
- Character creation and management
- Race selection
- Skill configuration
- Equipment management
- Character stats and parameters customization

### Game Master Features
- User profile administration
- Game characteristics management
- Character oversight
- Equipment and inventory control
- Combat system administration

## 🏗️ Project Structure

The project consists of several Django applications:

- **usuarios**: User management and authentication
- **personajes**: Character creation and management
- **raza**: Race definitions and characteristics
- **equipamientos**: Equipment and inventory system
- **ataques**: Combat system and attack management

## 🔧 Dependencies

- Python 3.x
- Django
- django-environ
- Pillow
- Virtualenv

## ⚙️ Installation

1. Clone the repository:
```bash
git https://github.com/ma-thi-as/Role-Game-Management-System
cd Sistema_Juego_de_Rol
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requerimientos.txt
```

4. Navigate to the project directory and run migrations:
```bash
cd rolgame
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## 🚀 Getting Started

1. Register a new account
2. Log in with your credentials
3. Choose your role (Player by default, use createsuperuser command for create a game master role)
4. If you're a player:
   - Create a new character
   - Choose a race
   - Assign skills and attributes
   - Manage your equipment
5. If you're a Game Master:
   - Manage user profiles
   - Override character settings
   - Control game parameters
   - Manage combat scenarios

## 🔐 Security

- Role-based access control
- Secure authentication system
- Protected API endpoints
- User data encryption

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
