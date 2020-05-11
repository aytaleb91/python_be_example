# pythonBE
Compose and Django app with a PostgreSQL database 

## Installation
steps:

* clone thre repo
`git clone https://aytaleb@bitbucket.org/aytaleb/python_be.git`

* Build 
`docker-compose up --build`

* make migrations 
`sudo docker-compose run web  python manage.py makemigrations store --name init_models`

* migrate 

`sudo docker-compose run web  python manage.py migrate`

* load data into db from fixture.json

`sudo docker-compose run web  python manage.py loaddata fixture.json`

## endpoints
the app will be running on `localhost:8000`


## Endpoint

```http
GET /products
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `page_size` | `int` | **optional**. default 25 |
| `page_number` | `int` | **optional**. default 1 |


## Responses

a list of products

```javascript
[
    {
        "model": "store.product", 
        "pk": 0, 
        "fields": {
                    "name": "flower_0", 
                    "stock": 62, 
                    "price": 1.0
                }
    }
]
```

## Endpoint

```http
GET /orders
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `page_size` | `int` | **optional**. default 25 |
| `page_number` | `int` | **optional**. default 1 |


## Responses

a list of orders

```javascript
[
    {
        "model": "store.order",
        "pk": 0,
        "fields": {
            "order_date": "2016-06-12",
            "quantity": 85, 
            "total": 85.0 
        }
    }
]
```
## Endpoint

```http
GET /products/<int:pk>
```

## Responses

product, list of products was sold with the product ordered by the times a product was bought

```javascript
{
    "product": {
        "name": "flower_14", 
        "stock": 65, 
        "price": 1.0
        },
    "bougthWithProducts": [
        {
            "name": "flower_8", 
            "count": 5
        },
        {
            "name": "flower_4", 
            "count": 4
        }, 
        {
            "name": "flower_3", 
            "count": 2
        }
    ]
}
```
## Endpoint

```http
GET /orders/<int:pk>
```

## Responses

an html page of order detail

## Endpoint

```http
GET /generateData/
```

## Responses

an endpoint to generate random products and orders used to create fixture.json
