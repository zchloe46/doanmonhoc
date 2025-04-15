# DjangoProject1

## Overview
This project is a Django web application designed to perform text classification and tokenization using the UnderTheSea library. It includes functionalities for sentiment analysis, tokenization, and part-of-speech tagging.

## Project Structure
```
DjangoProject1
├── dashboard
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── __init__.py
├── DjangoProject1
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

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd DjangoProject1
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install django underthesea
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
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage database records.

## Models
The application includes the following models:
- `van_ban`: Represents the text data.
- `tach_tu`: Represents tokenized words.
- `gan_nhan`: Represents tagged data.
- `phan_loai`: Represents classified data.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.