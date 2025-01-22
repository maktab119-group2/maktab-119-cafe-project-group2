# maktab-119-cafe-project-group2
# Wood Coffee  

Welcome to **Wood Coffee**, a collaborative project inspired by the warmth of a rustic, wood-themed coffee shop. This platform is designed to enhance the coffee shop experience by providing a dynamic and easy-to-use interface.  

## Project Overview  
The **Wood Coffee** project showcases our teamwork and creativity in developing a simple yet elegant platform. It allows customers to explore the menu, place orders, and interact with the coffee shop in a seamless way.  

## Features  
- **Interactive Menu**: Browse a detailed menu with descriptions and pricing.  
- **Order Management**: Place orders for pickup or in-store dining.  
- **Reservation System**: Reserve tables effortlessly.  
- **Admin Tools**: Manage menu items and track orders easily.  
- **Translation Support**: U can translate the platform into Persian (fa).

## Tech Stack  
- **Frontend**: HTML, CSS (using Bootstrap for styling)  
- **Backend**: Python (Django)  
- **Database**: SQLite/PostgreSQL  
- **Version Control**: Git and GitHub  

## Installation  

### Prerequisites  
- Python 3.8 or higher  
- Django framework  

### Steps  
1. Clone the repository:  
   
bash  
   git@github.com:maktab119-group2/Maktab119_cafe_project_group2.git  
  
2. Navigate to the project directory:  
   
bash  
   cd wood-coffee-shop  
  
3. Install the required dependencies:  
   
bash  
   pip install -r requirements.txt  
  
4. Run the application:  
   
bash  
   python manage.py runserver  
  
5. Open your browser and go to `http://127.0.0.1:8000` (or the appropriate address).  

## Translation Setup  

To enable translations (e.g., English to Persian), follow these steps based on your operating system:  

### Linux  
1. Install `gettext`:  
   
bash  
   sudo apt install gettext  
  
2. Alternatively, install it via Python:  
   
bash  
   pip install python-gettext  
  
3. Add `gettext` to your PATH (for Zsh):  
   
bash  
   echo 'export PATH="/usr/local/opt/gettext/bin:$PATH"' >> ~/.zshrc  
   source ~/.zshrc  
  
4. Create translation files:  
   
bash  
   python manage.py makemessages -l fa  
  
5. Compile translations:  
   
bash  
   python manage.py compilemessages  
  
### Windows  
1. Install `gettext` via pip:  
   
bash  
   pip install python-gettext  
  
2. Download and install the Windows version of `gettext` from:  
   [https://mlocati.github.io/articles/gettext-iconv-windows.html](https://mlocati.github.io/articles/gettext-iconv-windows.html)  
3. Add the `bin` directory of `gettext` to your PATH environment variable.  
4. Run the following commands in your project directory:  
   
bash  
   python manage.py makemessages -l fa  
   python manage.py compilemessages  
  
### macOS  
1. Install `gettext` via Homebrew:  
   
bash  
   brew install gettext  
  
2. Add it to your PATH:  
   
bash  
   echo 'export PATH="/usr/local/opt/gettext/bin:$PATH"' >> ~/.zshrc  
   source ~/.zshrc  
  
3. Create and compile translation files:  
   
bash  
   python manage.py makemessages -l fa  
   python manage.py compilemessages  
  
## How to Contribute  
1. Fork the repository.  
2. Create a new branch for your feature or fix:  
   
bash  
   git checkout -b feature-name  
  
3. Commit your changes:  
   
bash  
   git commit -m "Description of changes"  
  
4. Push your branch to your fork:  
   
bash  
   git push origin feature-name  
  
5. Submit a pull request, detailing your contribution.  

## License  
This project is licensed under the [MIT License](LICENSE).  

## Acknowledgments  
Special thanks to the entire team for their hard work and dedication. This project wouldn’t be possible without our shared passion for great coffee and technology!  

---  

We hope you enjoy both building and using the Wood Coffee Shop platform!
