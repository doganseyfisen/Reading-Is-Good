To run Django:
```
cd {project directory}
.venv\Scripts\activate
python manage.py runserver
```

To run Vue:
```
cd {project directory}\readingisgoodvue
npm run serve
```

To run all tests:
```
cd {project directory}
.venv\Scripts\activate
python manage.py test
```

To build & up Docker:
```
cd {project directory}
docker-compose build
docker-compose up
```

To stop Docker:
```
cd {project directory}
docker-compose down
```

Admin (Superuser) info:
* admin
* 12345

User info:
* commonuser
* pass12345

Credit cart info (Please look at the website of [Stripe](https://stripe.com/docs)):
* 4242 4242 4242 4242
* MM/YY (Date can be any further date, like 12/24)
* CVV (Any 3 digit numbers)
