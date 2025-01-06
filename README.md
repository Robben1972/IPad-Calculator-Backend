## Features
- FastAPI backend
- Integration with Gemini API
- Simple setup and deployment

## Installation

### Prerequisites
- Python 3.9 or higher
- Git
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository**:
   ```bash
   git clone git@github.com:Robben1972/IPad-Calculator-Backend.git
   cd IPad-Calculator-Backend
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory:
   ```bash
   touch .env
   ```

   Add the following content to `.env`:
   ```dotenv
   GEMINI_API_KEY=""
   ```

   Replace `GEMINI_API_KEY` with your actual API key from Gemini. You can obtain this by signing up on [Gemini's website](https://www.gemini.com/).

## Running the Application

1. **Run the FastAPI server**:
   ```bash
   py main.py
   ```

   The application will be accessible at `[http://127.0.0.1:8000](http://localhost:8900)`.


## Screenshots

**Question Screen:**
![Question Screenshot](path/to/Screenshot-2025-01-06-100817.png)

**Answer Screen:**
![Answer Screenshot](path/to/Screenshot-2025-01-06-100905.png)
