import unittest
from image_classification import create_app, db
from config import create_config
from image_classification.models import User


class TestBasic(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app(create_config['test'])
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    # def test_home(self):
    #     with self.app_context:
    #         response = self.app.test_client().get('/home', follow_redirects=True)
    #         self.assertEqual(response.status_code, 200)

    def test_user(self):
        with self.app_context:
            u = User(username='testuser', email='testuser@testing.com')
            u.password = "testing123"
            db.session.add(u)
            db.session.commit()
            self.assertEqual(len(User.query.all()), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
