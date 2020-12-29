import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

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
    response.headers.add('Access-Control-Methods', 'GET, POST, PATCH, DELETE'),
    response.headers.add('Access-Control-Allow-Origin', '*'),
    return response


  # def paginate_questions(request, selection):
  #   return

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

    return result



  @app.route('/')
  def index():
    return "Hello World"

  @app.route('/api/test')
  def with_cors():
    return "Hello Moon"

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories', methods=['GET', 'POST'])
  def get_categories():
    if request.method == 'POST':
      return "Trying to POST on Categories"

    if request.method == 'GET':
      categories = Category.query.all()
      if categories is not None:
        result = []
        for category in categories:
          item = Category.format(category)
          result.append(item['type'])
        return jsonify({
          "succes": True,
          "categories": result
        })
      return abort(404)



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
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + 10
    print("PAGE: ", page)

    questions = Question.query.all()
    formatted_questions = [question.format() for question in questions]
    categories = Category.query.all()
    formatted_categories = [category.format() for category in categories]
    category_ids = []
    for category in formatted_categories:
      category_ids.append(category['type'])

    if len(formatted_questions) == 0:
      abort(404)

    return jsonify({
      'succes': True,
      'questions': formatted_questions[start:end],
      'total_question': len(formatted_questions),
      'categories': category_ids
    })


  @app.route('/questions/<int:question_id>')
  def get_specific_question(question_id):
    question = Question.query.filter(Question.id == question_id).one_or_none()

    if question is None:
      abort(404)

    else:
      return jsonify({
        'succes': True,
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
        'deleted': question_id,
      })
    
    except:
      abort(422)

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

    print(new_category)

    
    try:
      item = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
      item.insert()

      return jsonify({
        "success": True,
      })

    except:
      abort(404)


  # @app.route('/questions', methods=['POST'])
  # def create_question():
  #   body = request.get_json()

  #   new_question = body.get('question', None)
  #   new_answer = body.get('answer', None)
  #   new_category = body.get('category', None)
  #   new_difficulty = body.get('difficulty', None)

  #   try:
  #     question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
  #     question.insert()

  #     selection = Question.query.oder_by(Question.id).all()
  #     current_questions = paginate_questions(request, selection)

  #     return jsonify({
  #       'success': True,
  #       'created': question.id,
  #       'questions': paginate_questions(request),
  #       'total_questions': len(Question.query.all()),
  #     })

  #   except:
  #     abort(404)




  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


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

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  return app

    