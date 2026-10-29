import unittest
import app as todo_app # 2차시에 친 app.py 를 가져온다
class TodoApiTest(unittest.TestCase):
    def setUp(self): # 테스트 하나마다 먼저 돈다
        todo_app.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        todo_app.app.config["TESTING"] = True
        self.client = todo_app.app.test_client()
        self.ctx = todo_app.app.app_context()
        self.ctx.push()
        todo_app.db.drop_all()
        todo_app.db.create_all()
    def tearDown(self): # 끝날 때마다 돈다
        todo_app.db.session.remove()
        self.ctx.pop()