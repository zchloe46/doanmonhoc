# Doanmonhoc

## Overview
This project is a Django web application designed to perform text classification and tokenization using the UnderTheSea library. It includes functionalities for sentiment analysis, tokenization, and part-of-speech tagging.

## Project Structure
```
doanmonhoc
├── dashboard
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── __init__.py
├── doanmonhoc
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
└── README.md
```

## Requirements
- Python 3.8
- Django
- UnderTheSea
- Pymysql

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/zchloe46/doanmonhoc.git
   cd doanmonhoc
   ```

2. Create a virtual environment:
   ```
   py 3.8 -m venv .venv
   ```

3. Install the required packages:
   ```
   pip install django underthesea pymysql
   ```

4. Configure the database settings in `DjangoProject1/settings.py` to connect to your MySQL database.

5. Run migrations to set up the database:
   ```
   python manage.py migrate
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.