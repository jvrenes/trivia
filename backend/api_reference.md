# API REFERENCE

## Getting Started

-Base URL: http://127.0.0.1:5000 this app can only be run locally.
-Authentication: This version of the application does not require authentication API keys.

## Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "succes": False,
    "error": 400,
    "messagge": "bad request"
}
```

The API returns four different errors types when request fails:
    - 400: Bad request
    - 404: Resource not found
    - 405: Method not allowed
    - 422: Unprocessable

## Endpoints

### GET /categories

- General:
    - Returns an array list of categories and a success value.
    - Sample: ```curl http://127.0.0.1:5000/categories``` 

### GET /questions

- General:
    - Returns a list of questions object, succes value and total number of questions.
    - Results are paginated in groups of 10. Include a request argument to choose page number,starting from 1.
- Sample: ```curl http://127.0.0.1:5000/questions```