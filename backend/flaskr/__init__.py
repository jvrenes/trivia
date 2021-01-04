import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
<<<<<<< HEAD
=======
import unittest
>>>>>>> test

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app


  app = Flask(__name__)
  setup_db(app)
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"*": {"origins": "*"}})


  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  #CORS headers
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,'),
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE'),
    response.headers.add('Access-Control-Allow-Origin', '*'),
    return response



  def paginate_questions(request):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = Question.query.all()
    formatted_questions = [question.format() for question in questions]
    return formatted_questions

  
  def get_categories():
    categories = Category.query.all()
    result = []

    for category in categories:
      item = Category.format(category)
      result.append(item)

<<<<<<< HEAD
=======
    if len(result) == 0:
      abort(404)

>>>>>>> test
    return result


  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
<<<<<<< HEAD
  @app.route('/categories', methods=['GET', 'POST'])
  def get_categories():
    if request.method == 'POST':
      return "Trying to POST on Categories"

=======
  @app.route('/categories', methods=['GET'])
  def get_categories():
>>>>>>> test
    if request.method == 'GET':
      categories = Category.query.all()
      if categories is not None:
        result = []
        for category in categories:
          item = Category.format(category)
          result.append(item['type'])
        return jsonify({
<<<<<<< HEAD
          "succes": True,
          "categories": result
        })
      return abort(404)
=======
          "success": True,
          "categories": result
        })
      return abort(404)
    
    else:
      abort(405)
>>>>>>> test



  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories.

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions', methods=['GET'])
  def get_questions():
    try:
      page = request.args.get('page', 1, type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = start + 10
      print("PAGE: ", page)

      questions = Question.query.all()
      formatted_questions = [question.format() for question in questions]
      categories = Category.query.all()
      formatted_categories = [category.format() for category in categories]
      category_ids = []
<<<<<<< HEAD
      for category in formatted_categories:
        category_ids.append(category['type'])

      if len(formatted_questions) == 0:
=======
      result = formatted_questions[start:end]
      for category in formatted_categories:
        category_ids.append(category['type'])

      if len(result) == 0:
>>>>>>> test
        abort(404)

      return jsonify({
        'succes': True,
<<<<<<< HEAD
        'questions': formatted_questions[start:end],
=======
        'questions': result,
>>>>>>> test
        'total_questions': len(questions),
        'categories': category_ids
      })
    except:
      abort(404)


  @app.route('/questions/<int:question_id>')
  def get_specific_question(question_id):
    question = Question.query.filter(Question.id == question_id).one_or_none()

    if question is None:
      abort(404)

    else:
      return jsonify({
<<<<<<< HEAD
        'succes': True,
=======
        'success': True,
>>>>>>> test
        'question': question.format()
      })
  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.get(question_id)

      if question is None:
        abort(404)

      question.delete()

      return jsonify({
        'success': True,
<<<<<<< HEAD
        'question_id_deleted': question_id,
      })
    
    except:
      abort(422)
=======
        'question_id_deleted': question_id
      })
    
    except:
      abort(404)
>>>>>>> test

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()

    new_question = body.get('question', None)
    new_answer = body.get('answer', None)
    new_category = body.get('category', None)
    new_difficulty = body.get('difficulty', None)

<<<<<<< HEAD

    print(new_category)

=======
>>>>>>> test
    try:
      item = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
      item.insert()

      return jsonify({
        "success": True,
      })

    except:
      abort(404)

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    body = request.get_json()
    query = body.get('searchTerm', None)
    print(query)

    if query is None:
<<<<<<< HEAD
      abort(404)
=======
      abort(400) #Bad request error
>>>>>>> test

    try:
      questions = Question.query.filter(Question.question.ilike('%{}%'.format(query))).all()
      formatted_questions = [question.format() for question in questions]
      print("Questions: ", formatted_questions)

      if len(questions) == 0:
<<<<<<< HEAD
        abort(404)
=======
        abort(404) #Not found error
>>>>>>> test
      
      return jsonify({
        "success": True,
        "questions": formatted_questions,
        "total_questions": len(questions)
      })
    
    except:
      abort(404)

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category.

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:id>/questions')
  def questions_by_category(id):
<<<<<<< HEAD
    category = Category.query.get(id + 1)
    category_name = category.type
    questions = Question.query.filter_by(category=category_name).all()
    formatted_questions = [question.format() for question in questions]
    return jsonify({
      "questions": formatted_questions,
      "success": True,
    })
=======
    try:
      category = Category.query.get(id + 1)
      category_name = category.type
      questions = Question.query.filter_by(category=category_name).all()
      formatted_questions = [question.format() for question in questions]
      return jsonify({
        "questions": formatted_questions,
        "success": True,
      })

    except:
      abort(404)
>>>>>>> test


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def quiz():
    body = request.get_json()
    previous_questions = body.get('previous_questions', [])
    print(previous_questions)
    quiz_category = body.get('quiz_category')
    category_name = quiz_category['type']
    category_id =  quiz_category['id']

    if category_name == 'click':
      print('No category selected')
      questions = Question.query.all()
      selected = []

      for question in questions:
        if question.id not in previous_questions:
          selected.append(question)

      formatted_questions = [question.format() for question in selected]
      question = (random.choice(formatted_questions))
      
      if len(question) != 0:
        return jsonify({
          "success": True,
          "question": question
        })
      else:
        abort(404)

    elif category_name != 'click':
      print(f'Category selected: {category_name}')
      questions = Question.query.filter_by(category=category_name).all()
      selected = []

      for question in questions:
        if question.id not in previous_questions:
          selected.append(question)

      formatted_questions = [question.format() for question in selected]
      question = random.choice(formatted_questions)
      print(questions)

      return jsonify({
        "success": True,
        "question": question
      })

      


    return jsonify({
      "success": True,
      "request": True
    })

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
<<<<<<< HEAD
=======
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'Not found'
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
    }), 422
    
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request"
    }), 400

  @app.errorhandler(405)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 405,
      "message": "method not allowed"
    }), 405

>>>>>>> test
  
  return app

    