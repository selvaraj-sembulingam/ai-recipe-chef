import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

# --- Configuration ---
# It's recommended to use environment variables for your API key.
# Make sure to set the GOOGLE_API_KEY environment variable.
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please provide your API key.")

# genai.configure(api_key=GOOGLE_API_KEY)

# --- FastAPI App Initialization ---
app = FastAPI(
    title="Personalized Recipe Generator API",
    description="An API that generates personalized recipes based on user inputs using the Gemini model.",
    version="1.0.0",
)

# --- CORS Middleware ---
# This allows the frontend (running on a different origin) to communicate with this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for simplicity. For production, restrict this.
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods.
    allow_headers=["*"],  # Allows all headers.
)

# --- Pydantic Models for Data Validation ---
class RecipeRequest(BaseModel):
    """Defines the structure of the incoming request body."""
    ingredients: str
    dietary_restrictions: str = "none"
    cuisine_type: str = "any"

client = genai.Client(api_key=GOOGLE_API_KEY)

# --- API Endpoints ---
@app.get("/")
def read_root():
    """A simple root endpoint to confirm the API is running."""
    return {"message": "Welcome to the Personalized Recipe Generator API!"}

@app.post("/generate-recipe")
async def generate_recipe(request: RecipeRequest):
    """
    Generates a recipe based on the user's input.
    """
    if not request.ingredients:
        raise HTTPException(status_code=400, detail="Ingredients cannot be empty.")

    # --- Constructing the Prompt for the AI Model ---
    prompt = f"""
    You are a creative chef. Generate a delicious recipe based on the following details:

    1.  **Main Ingredients:** {request.ingredients}
    2.  **Dietary Restrictions:** {request.dietary_restrictions}
    3.  **Desired Cuisine:** {request.cuisine_type}

    Please provide a response with the following structure:
    - **Recipe Title:** A catchy name for the dish.
    - **Description:** A short, enticing description.
    - **Ingredients:** A bulleted list of all ingredients with quantities.
    - **Instructions:** Step-by-step cooking instructions.
    - **Serving Suggestion:** (Optional) A suggestion on how to best serve the dish.

    Make the recipe easy to follow for a home cook. Ensure the output is well-formatted in markdown.
    """

    try:
        # --- Calling the Gemini API ---
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        
        # Check if the response has the expected text part
        if not response.parts:
             raise HTTPException(status_code=500, detail="Failed to generate recipe. The model returned an empty response.")
        
        generated_recipe = response.text

        return {"recipe": generated_recipe}

    except Exception as e:
        # --- Error Handling ---
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate recipe due to an internal error.")

# --- To run this application ---
# 1. Install the necessary packages: pip install -r requirements.txt
# 2. Set your Google API key: export GOOGLE_API_KEY='your_api_key_here'
# 3. Run the server: uvicorn main:app --reload
