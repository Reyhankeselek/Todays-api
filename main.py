from fastapi import FastAPI
from datetime import datetime
import uvicorn

# Create FastAPI instance
app = FastAPI(title="Days API")

@app.get("/days")
async def get_days():
    """
    Returns 'today' when a client makes a GET request to /days
    """
    return {"response": "today"}

# For testing in this environment
if __name__ == "__main__":
    print("FastAPI app created. Here's how you would run it:")
    print("uvicorn main:app --reload")
    
    # Simulate a request to /days
    print("\nSimulating a GET request to /days:")
    print("Response would be:", {"response": "today"})
