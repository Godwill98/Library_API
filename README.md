Library Management System

Project Overview

The Library Management System is a Django-based web application designed to manage various aspects of a library. 
This project includes functionalities to handle authors, books, members, loans, and librarians using Django REST framework for API development.

Features

- Authors: Manage author details including name and biography.
- Books: Manage book details including title, author, publication date, and ISBN.
- Members: Manage library members with personal details.
- Loans: Track book loans including loan date and return date.
- Librarians: Manage librarian details including user name and employee number.

Technologies Used

- **Django**: Framework for building the web application.
- **Django REST framework**: Toolkit for creating RESTful APIs.
- **Python**: Programming language.

 Installation

1. Clone the Repository:

   ```bash
   git clone <your-github-repo-url>
   cd LibraryManagementSystem
   ```

2. Set Up a Virtual Environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run Migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the Development Server:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

API Endpoints

- Authors

  - `GET /api/authors/` - List all authors
  - `POST /api/authors/` - Create a new author
  - `GET /api/authors/{id}/` - Retrieve a specific author
  - `PUT /api/authors/{id}/` - Update a specific author
  - `DELETE /api/authors/{id}/` - Delete a specific author

- Books

  - `GET /api/books/` - List all books
  - `POST /api/books/` - Create a new book
  - `GET /api/books/{id}/` - Retrieve a specific book
  - `PUT /api/books/{id}/` - Update a specific book
  - `DELETE /api/books/{id}/` - Delete a specific book

- Members

  - `GET /api/members/` - List all members
  - `POST /api/members/` - Create a new member
  - `GET /api/members/{id}/` - Retrieve a specific member
  - `PUT /api/members/{id}/` - Update a specific member
  - `DELETE /api/members/{id}/` - Delete a specific member

- Loans

  - `GET /api/loans/` - List all loans
  - `POST /api/loans/` - Create a new loan
  - `GET /api/loans/{id}/` - Retrieve a specific loan
  - `PUT /api/loans/{id}/` - Update a specific loan
  - `DELETE /api/loans/{id}/` - Delete a specific loan

- Librarians

  - `GET /api/librarians/` - List all librarians
  - `POST /api/librarians/` - Create a new librarian
  - `GET /api/librarians/{id}/` - Retrieve a specific librarian
  - `PUT /api/librarians/{id}/` - Update a specific librarian
  - `DELETE /api/librarians/{id}/` - Delete a specific librarian

Testing

To ensure the API works as expected, unit tests have been implemented. You can run the tests with:

```bash
python manage.py test
```

Test Results

Testing was performed using Django’s inbuilt test framework. The results of the tests are as follows:

- Authors: All CRUD operations tested successfully.
- Books: All CRUD operations tested successfully.
- Members: All CRUD operations tested successfully.
- Loans: All CRUD operations tested successfully.
- Librarians: All CRUD operations tested successfully.

*Screenshots and detailed test logs are included in the `testing_evidence` folder.*

Contributing

Feel free to fork the repository and submit pull requests for improvements or bug fixes. Please ensure that any changes made are well-documented and tested.

 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Authors

- Godwill Kiplagat - *Initial work* - [YourGitHubProfile](https://github.com/godwill98)

---

Feel free to customize the details to match your specific project requirements and include any additional sections you find necessary.
