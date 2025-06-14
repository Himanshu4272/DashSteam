===============================
Python Project Setup Guide (.txt)
===============================

📘 How to Set Up and Install Python Project Requirements (General Guide)

This guide will help you install the required Python packages for a project using a virtual environment.

---------------------------------------
✅ What You Need:
---------------------------------------
- Python 3.11 or newer installed
  👉 Download: https://www.python.org/downloads/
  During installation:
  - ✅ Check “Add Python to PATH”
  - ✅ Enable pip

---------------------------------------
🔧 Step-by-Step Instructions:
---------------------------------------

📁 Step 1: Open Your Project Folder
-----------------------------------
Open Command Prompt or PowerShell, and navigate to your project folder:

    cd path\to\your\project

Example:

    cd C:\Users\YourName\Documents\MyPythonProject

🧹 Step 2: (Optional) Remove Old or Broken Virtual Environment
---------------------------------------------------------------
If there is an existing `venv` folder and it may be broken or outdated, remove it:

    Remove-Item -Recurse -Force .\venv    (For PowerShell)
    rmdir /s /q venv                       (For CMD)
    rm -rf venv                            (For macOS/Linux)

🧪 Step 3: Create a Virtual Environment
---------------------------------------
    python -m venv venv

This creates a folder named `venv` where packages will be installed.

🚀 Step 4: Activate the Virtual Environment
-------------------------------------------

On Windows:
    .\venv\Scripts\activate

On macOS/Linux:
    source venv/bin/activate

After this, your terminal will show:
    (venv) C:\Users\YourName\MyPythonProject>

📦 Step 5: Install Required Packages
------------------------------------
Make sure you have a requirements.txt file in the project folder. Then run:

    pip install -r requirements.txt

🧯 Step 6: (Optional) Upgrade pip
---------------------------------
    python -m pip install --upgrade pip

✅ You’re Done!
---------------
Your Python environment is now ready.

To deactivate the virtual environment later:
    deactivate

🛠 Troubleshooting:
-------------------
- ❌ python not found → Python is not installed or not added to PATH
- ❌ pip errors → Try using Python 3.11 and ensure requirements.txt is valid

Happy coding!
