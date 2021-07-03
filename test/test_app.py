from unittest import TestCase
from flask import Flask
import app


class TestFlaskApp(TestCase):
    def test_exist_create_app(self):
        self.assertEqual(hasattr(app, "create_app"), True, "app factory doesnt exist!")

    def test_invoke_create_app(self):
        self.assertEqual(
            hasattr(app.create_app, "__call__"), True, "app factory doesnt invoke"
        )

    def test_returns_flask_app_create_app(self):
        self.assertIsInstance(
            app.create_app(), Flask, "app factory doesnt Flask instance"
        )
