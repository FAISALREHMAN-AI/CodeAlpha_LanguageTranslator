# 🌐 CodeAlpha Language Translator (Task)

**A full-stack language translation web application built with React.js and Django REST Framework.**

This project was developed as **Task ** for the Artificial Intelligence Internship at **CodeAlpha**. It provides a user-friendly interface to translate text between multiple languages while also offering premium usability features like Text-to-Speech and clipboard support.

---

## ✨ Features
* **Real-Time Translation:** Select a source and target language to translate text instantly using the Google Translate API via Python.
* **Auto-Language Detection:** The application can automatically detect the input language.
* **Text-to-Speech (Audio Playback):** Listen to the translated text with a single click.
* **Audio Controls:** Includes a Stop button to halt audio playback at any time.
* **Copy to Clipboard:** Easily copy the translated results with a built-in copy button.
* **Modern UI:** A clean, responsive, and intuitive interface built with React.

---

## 🛠️ Tech Stack
* **Frontend:** React.js, HTML/CSS, Axios (for API requests)
* **Backend:** Python, Django, Django REST Framework (DRF)
* **Libraries/Packages:** 
  * `django-cors-headers` (Cross-Origin Resource Sharing)
  * `deep-translator` (For robust API translation handling)
  * `gTTS` (Google Text-to-Speech for audio generation)

---

## 🚀 Installation & Setup

To run this project locally on your machine, follow these steps:

### Prerequisites
Make sure you have the following installed on your system:
* [Python](https://www.python.org/downloads/) (v3.8+)
* [Node.js & npm](https://nodejs.org/)

### 1. Backend Setup (Django)
Open your terminal and navigate to the project directory:

```bash
# Navigate to the backend folder
cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For Mac/Linux:
source venv/bin/activate

# Install required Python packages
pip install django djangorestframework django-cors-headers deep-translator gtts

# Run the Django server
python manage.py runserver