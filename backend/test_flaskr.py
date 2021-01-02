import os
import unittest
import json

from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}@{}/{}".format('javier', 'localhost:5432', 'trivia_test')
        setup_db(self.app, self.database_path)

        self.new_question = {
          'question': 'new question from test',
          'answer': 'new answer from test',
          'category': 'art',
          'difficulty': 2
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass



    def test_get_categories(self):
        """Test getting the list of categories"""
        res = self.client().get('/categories')
        data = json.loads(res.data)
        categories = Category.query.all()
        result = []
        for category in categories:
            item = Category.format(category)
            result.append(item['type'])

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['categories'], result)
    
    def test_error_getting_categories(self):
        """Test getting error on method not allowed getting categories"""
        res = self.client().post('/categories')
  
        self.assertEqual(res.status_code, 405)

    def test_getting_specific_question(self):
        """Test getting a specific question"""
        res = self.client().get('/questions/1')
        data = json.loads(res.data)
        question = Question.query.get(1)
        result = question.format()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['question'], result)

    def test_error_getting_especific_question(self):
        """Testing error trying to retrieve an unexisting question"""
        res = self.client().get('/questions/173849')
        
        self.assertEqual(res.status_code, 404)

    def test_delete_question(self):
        """Testing delete a question by its id"""
        res = self.client().delete('questions/1')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_error_deleting_question(self):
        """Test error for deleting unexisting question"""
        res = self.client().delete('questions/1')
        
        self.assertEqual(res.status_code, 404)

    def test_create_new_question(self):
        """Test new question added to the database """
        res = self.client().post('/questions', json={'question':'new question from test', 'answer':'new answer from test', 'category':'art', 'difficulty':2})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()