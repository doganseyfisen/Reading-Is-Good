# Reading Is Good

## Overview
**Reading Is Good** is an online books retail firm operating exclusively on the Internet. The project encompasses a Django-based back-end and a Vue.js front-end, providing a comprehensive web application for book browsing, shopping, and order management.

## Back-end Setup (Django)

### Requirements
- Python 3.10
- Django 5.0
- Other dependencies are listed in `requirements.txt`.

### Installation
1. Clone the repository.
   ```
   git clone https://github.com/doganseyfisen/Reading-Is-Good.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Migrate the database:
   ```
   python manage.py migrate
   ```
4. Run the server:
   ```
   python manage.py runserver
   ```

## Front-end Setup (Vue.js)

### Requirements
- Node.js 14
- NPM
- Dependencies are listed in `package.json`.

### Installation
1. Navigate to the Vue.js project directory.
2. Install dependencies:
   ```
   npm install
   ```
3. Serve the application locally:
   ```
   npm run serve
   ```
4. For production, build the app:
   ```
   npm run build
   ```

## Docker Configuration
Both the Django back-end and Vue.js front-end can be containerized using Docker.

### Back-end
- Dockerfile details how to set up the Django app in a container.
- To build the Docker image for the Django application, use the command:
  ```
  docker-compose build
  ```
- To start the application in a container, use the command:
  ```
  docker-compose up
  ```
- To stop the application and remove the containers, use the command:
  ```
  docker-compose down
  ```

### Front-end
- Dockerfile sets up the Vue.js environment.
- To build and run the container:
  ```
  docker build -t readingisgoodvue .
  docker run -p 8080:8080 readingisgoodvue
  ```

## Features
- User authentication and registration.
- Book browsing by categories.
- Shopping cart and checkout process.
- Back-end API for managing books, orders, and user accounts.

## API Usage Examples (Insomnia)
- See
  ```
  Insomnia_2023-12-31.json
  ```

## Admin (Superuser) info:
```
admin
12345
```

## User info:
```
commonuser
pass12345
```

## Credit cart info ([Stripe](https://stripe.com/docs)):
```
4242 4242 4242 4242
MM/YY (Any further date)
CVC (Any 3 digits)
```