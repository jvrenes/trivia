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

```
{
  "categories": [
    "Science", 
    "Art", 
    "Geography", 
    "History", 
    "Entertainment", 
    "Sports"
  ], 
  "success": true
}
```

### GET /questions

- General:
    - Returns a list of questions object, alist of categories object,  succes value and total number of questions.
    - Results are paginated in groups of 10. Include a request argument to choose page number,starting from 1.
- Sample: ```curl http://127.0.0.1:5000/questions?page=1```

```
{
  "categories": [
    "Science", 
    "Art", 
    "Geography", 
    "History", 
    "Entertainment", 
    "Sports"
  ], 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "succes": true, 
  "total_questions": 19
}
```

### GET /questions/<question_id>

- General:
    - Returns an object with the info based on a particuales question id and a success value.
    - Sample: ```curl http://127.0.0.1:5000/question/6``` 

```
{
  "question": {
    "answer": "Edward Scissorhands", 
    "category": 5, 
    "difficulty": 3, 
    "id": 6, 
    "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
  }, 
  "success": true
}
```

### DELETE /questions/<question_id>

- General:
    - Delete a given question based on the question id passed in the endpoint.
    - Returns a success value and the question id that has been deleted.
    - Sample : ```curl -X DELETE http://127.0.0.1:5000/questions/9```

```
{
  "question_id_deleted": 9, 
  "success": true
}
```

### POST /questions

- General:
    - Add a new question to the database.
    - Returns a success value for the operation.
    - Sample: ```curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question";"new question", "answer":"new answer", "category":category name", "difficulty": 2}```

```
{
    "success": True,
}
```

### POST /questions/search

- General:
    - Search any coincidence on the questions title for any given word or term.
    - Returns an object containing any questions that match with the given term, succes value, and a number with the total of questions found.
    - Sample: ```curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":"mahal"}' ```

```
{
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "total_questions": 1
}
```

### GET /categories/<category_name>/questions

- General:
    - Obtain questions on a given category name.
    - Returns an object containing questions, and succes value.
    - Sample ```curl http://127.0.0.1:5000/categories/art/questions````

```
{
  "questions": [
    {
      "answer": "Respuesta6", 
      "category": "geography", 
      "difficulty": 1, 
      "id": 13, 
      "question": "Pregunta6"
    }, 
    {
      "answer": "Respuesta9", 
      "category": "geography", 
      "difficulty": 4, 
      "id": 16, 
      "question": "Pregunta9"
    }
  ], 
  "success": true
}
```

### POST /quizzes

- General: 
    - Obtain an aleatory question for any given category if selected, if ypu want to return any random question within all the categories, you should post the value 'click' for the 'category_name' key.
    - Questions are not repeated within the same game.
    - Returns an object containing the question
    - Sample: ```curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type:application/json" -d '{"quiz_category":"{"type":"click", "id":"0"}", "previous_questions":"[]"}'```

```
{
  "question": {
      "answer": "Respuesta6", 
      "category": "geography", 
      "difficulty": 1, 
      "id": 13, 
      "question": "Pregunta6"
    },
  "success": true
}
```