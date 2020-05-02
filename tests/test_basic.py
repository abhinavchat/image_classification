import unittest
from image_classification import create_app, db
from config import create_config
from image_classification.models import User
from app import load_user
from image_classification.auth.forms import LoginForm, SignupForm


class TestBasic(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app(create_config['test'])
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login(self, username=None, password=None):
        with self.app_context:
            form = LoginForm(username=username, password=password)
            return self.client.post('/login', data=form.data, follow_redirects=True)

    def signup(self, username=None, email=None, password=None, password2=None):
        with self.app_context:
            form = SignupForm(username=username, email=email, password=password, password2=password2)
            return self.client.post('/signup', data=form.data, follow_redirects=True)

    def test_login(self):
        with self.app_context:
            u = User(username='testuser', email='test@testing.com')
            u.password = 'test123'
            db.session.add(u)
            db.session.commit()

        response = self.login(username='testuser', password='test1234')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Incorrect username or password.', response.data)

        response = self.login(username='testuser', password='test123')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have successfully logged in', response.data)

    def test_signup(self):
        with self.app_context:
            u = User(username='testuser2', email='test2@user.com')
            u.password = 'test123'
            db.session.add(u)
            db.session.commit()

        response = self.signup(username='testuser3', email='abc@def.com', password='test123', password2='test1234')
        self.assertIn(b'Password and Confirm Password must be equal', response.data)

        response = self.signup(username='testuser2', email='test2@user.com', password='test123', password2='test123')
        self.assertIn(b'Username testuser2 already taken.', response.data)

        response = self.signup(username='testuser3', email='test3@user.com', password='test123', password2='test123')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have successfully Registered', response.data)

    def test_adduser(self):
        with self.app_context:
            u = User(username='testuser', email='testuser@testing.com')
            u.password = "testing123"
            db.session.add(u)
            db.session.commit()
            self.assertEqual(len(User.query.all()), 1)

    def test_deluser(self):
        with self.app_context:
            u = User(username='testuser', email='testuser@testing.com')
            u.password = 'testing123'
            db.session.add(u)
            db.session.commit()
            self.assertEqual(len(User.query.all()), 1)
            u = User.query.first()
            db.session.delete(u)
            db.session.commit()
            self.assertEqual(len(User.query.all()), 0)

    def test_uniquenessusername(self):
        with self.app_context:
            u = User(username='testuser', email='testuser@testing.com')
            u.password = 'testing123'
            db.session.add(u)
            db.session.commit()

            u = User(username='testuser', email='testuser2@testing.com')
            u.password = 'testing123'
            db.session.add(u)

            from sqlalchemy.exc import IntegrityError
            with self.assertRaises(IntegrityError) as ie:
                db.session.commit()

            db.session.rollback()

            u = User(username='testuser2', email='testuser@testing.com')
            u.password = 'testing123'
            db.session.add(u)

            with self.assertRaises(IntegrityError) as ie:
                db.session.commit()

    def test_nullablefields(self):
        with self.app_context:
            u = User(username=None, email='testuser@testing.com')
            u.password = 'testing123'
            db.session.add(u)

            from sqlalchemy.exc import DataError, IntegrityError
            with self.assertRaises(IntegrityError) as de:
                db.session.commit()




if __name__ == "__main__":
    unittest.main(verbosity=2)
