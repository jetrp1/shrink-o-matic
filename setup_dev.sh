# Verify Python installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python 3."
    exit 1
fi

# verify python3-venv installed
if ! python3 -m venv --help &> /dev/null; then
    echo "Python venv module is not installed. Please install python3-venv."
    exit 1
fi

# Create a virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi  

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install required packages
if [ ! -f "requirements.txt" ]; then
    echo "Error: requirements.txt not found!"
    exit 1
fi

echo "Installing required packages from requirements.txt..."
if ! pip install -r requirements.txt; then
    echo "Error: Failed to install Python packages!"
    deactivate
    exit 1
fi

# deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate 

# setup the node js environment
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Please install Node.js."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "npm is not installed. Please install npm."
    exit 1
fi

# Install required Node.js packages
if [ ! -f "package.json" ]; then
    echo "Error: package.json not found!"
    exit 1
fi

echo "Installing Node.js packages from package.json..."
if ! npm install; then
    echo "Error: Failed to install Node.js packages!"
    exit 1
fi
