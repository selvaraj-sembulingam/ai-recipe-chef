# AI Recipe Chef 🍳
AI Recipe Chef is a web application with a sleek, modern interface that allows users to generate personalized recipes. Simply enter the ingredients you have on hand, specify any dietary restrictions and preferred cuisine, and let the AI craft a unique and delicious recipe for you.

## ✨ Features
* Dynamic Recipe Generation: Get creative recipes based on the ingredients you already own.

* Personalized Filtering: Tailor results with options for dietary needs (Vegetarian, Vegan, Keto, etc.) and cuisine types (Italian, Mexican, etc.).

* Stunning & Responsive UI: A beautiful, user-friendly interface that works seamlessly on desktops, tablets, and mobile devices.

* Dynamic Backgrounds: The background image changes on each visit for a fresh feel.

* Dark & Light Modes: Automatically adapts to your system's theme, with a manual toggle to switch between dark and light modes.

* Copy to Clipboard: An easy one-click button to copy the generated recipe to your clipboard.

* Robust Markdown Parsing: Beautifully renders formatted recipe text, including headers, lists, and bold text, using the Marked.js library.

## 💻 Tech Stack
This project is a full-stack application, consisting of a static frontend and a separate backend server.

### Frontend
* HTML5: For the core structure of the application.

* Tailwind CSS: A utility-first CSS framework for rapid and modern UI development.

* Vanilla JavaScript: For all client-side logic, interactivity, and API communication.

* Font Awesome: For clean and scalable icons.

* Marked.js: A robust library to parse Markdown responses from the backend into formatted HTML.

### Backend (using FastAPI)
* Python 3.x

* FastAPI: A modern, high-performance Python web framework for building APIs.

* Generative AI Model: Powered by a large language model (Google's Gemini) to generate the recipes.

* Uvicorn: An ASGI server to run the FastAPI application.

## 🚀 Getting Started
To get this project up and running on your local machine, you will need to set up both the frontend and the backend.

### Prerequisites
* A modern web browser (for the frontend).

* Python 3.10+ and pip installed (for the backend).

* An API key from a generative AI provider (e.g., Google AI Studio).

### 1. Frontend Setup
The frontend is a single index.html file with no build steps required.

* Clone this repository:
```
git clone https://your-repository-url/ai-recipe-chef.git
```
* Navigate to the project directory:
```
cd ai-recipe-chef
```
* Open the index.html file directly in your web browser.

Note: For the form to work, the backend server must be running and the fetch URL in the JavaScript code must be correctly pointed to the backend server's address.

### 2. Backend Setup (Example)
* Set up a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
* Install the required Python packages:
(You will need a requirements.txt file for this step. If one doesn't exist, you can create it with the necessary libraries like fastapi, uvicorn, python-dotenv, and the AI provider's library, e.g., google-generativeai).
```
pip install -r requirements.txt
```

* Set your AI provider's API key in the environment:
```
export GOOGLE_API_KEY="YOUR_SECRET_API_KEY_HERE"
```
* Run the backend server:
```
uvicorn main:app --reload
```
* The server will typically start on http://127.0.0.1:8000.

🔧 Configuration
Before the application can work, you need to connect the frontend to the backend.

1. Update the API Endpoint in index.html:
Open the index.html file and find the fetch call within the <script> tag. Update the URL to match your running backend server.
```
// Find this line in the <script> section of index.html
const response = await fetch('[http://127.0.0.1:8000/generate-recipe](http://127.0.0.1:8000/generate-recipe)', {
    // ...
});
```
