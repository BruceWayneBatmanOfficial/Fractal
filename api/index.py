import os
import sys
import subprocess

# Direct Vercel to look at your main streamlit file
def handler(request):
    try:
        # Runs the streamlit application as a background process script execution
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'streamlitapp.py'))
        subprocess.run(["streamlit", "run", script_path, "--server.port=8080", "--server.address=0.0.0.0"], check=True)
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error starting Streamlit: {str(e)}"
        }
    return {
        "statusCode": 200,
        "body": "Streamlit environment initialized."
    }
