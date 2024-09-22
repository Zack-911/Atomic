{ pkgs ? import <nixpkgs> {} }: 

pkgs.mkShell {
  buildInputs = [
    pkgs.python311              # Python 3.11
    pkgs.python311Packages.pip  # pip for managing Python packages
    pkgs.python311Packages.termcolor # Add colors to your shell
    pkgs.python311Packages.python-dotenv # Manage environment variables
  ];

  shellHook = ''
    cd /home/user/testing/
    clear

    # Create and activate a virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
      echo "Creating virtual environment..."
      python3 -m venv venv
    fi

    echo "Activating virtual environment..."
    source venv/bin/activate

    # Customize the prompt with colors and suppress (venv)
    export PS1="\[\e[32m\]demon@SelfBotX \[\e[34m\]$(pwd)\[\e[0m\] \$ "  # Green for 'demon@SelfBotX', Blue for current directory

    if [ -f requirements.txt ]; then
      echo "Installing packages from requirements.txt..."
      pip install -r requirements.txt > /dev/null 2>&1
      echo "Packages installed."
    else
      echo "No requirements.txt found. Skipping package installation."
    fi

    echo "Virtual environment is ready."
  '';
}
