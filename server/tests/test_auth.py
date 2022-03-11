from .base_user import CustomUserTests
import requests
import json


class TestAuthentication(CustomUserTests):
    def setUp(self) -> None:
        self.cleanup()

    def test_user_register(self):
        try:
            data = self.user_data()
            response = self.request.post(
                self.base_url + "auth/register", data=json.dumps(data), headers=self.headers
            )
            self.assertEqual(response.status_code, 201)

            self.assertIn("access_token", response.json())
            self.assertIn("refresh_token", response.json())

            data = self.user_data()
            response = self.request.post(
                self.base_url + "auth/register", data=json.dumps(data), headers=self.headers
            )
            self.assertEqual(response.status_code, 400)

            data = self.user_data()
            data.pop("Email")
            response = self.request.post(
                self.base_url + "auth/register", data=json.dumps(data), headers=self.headers
            )
            self.assertEqual(response.status_code, 500)

        except requests.exceptions.ConnectionError:
            print("Connection Error")

    def test_user_login(self):
        try:
            data = self.user_data()
            response = self.request.post(
                self.base_url + "auth/register", data=json.dumps(data), headers=self.headers
            )
            self.assertEqual(response.status_code, 201)

            login_data = {"Password": data["Password"], "Email": data["Email"]}
            response = self.request.post(
                self.base_url + "auth/login",
                data=json.dumps(login_data),
                headers=self.headers,
            )

            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json()["access_token"], str)
            self.assertIsInstance(response.json()["refresh_token"], str)

            login_data = {"Password": "wrongpwd", "Email": data["Email"]}
            response = self.request.post(
                self.base_url + "auth/login",
                data=json.dumps(login_data),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 401)

            login_data = {"Password": data["Password"], "Email": "wrongmail@gmail.com"}
            response = self.request.post(
                self.base_url + "auth/login",
                data=json.dumps(login_data),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 404)

            incomplete_data = {"Email": "testmail@gmail.com"}
            response = self.request.post(
                self.base_url + "auth/login",
                data=json.dumps(incomplete_data),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 500)

        except requests.exceptions.ConnectionError:
            print("Connection Error")

    def test_get_tokens(self):
        try:
            tokens = self.login_user(get_refresh=True)
            data_acc = {"RefreshToken": tokens["refresh_token"], "RefreshStatus": True}

            response = self.request.post(
                self.base_url + "auth/generatetokens",
                data=json.dumps(data_acc),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn("access_token", response.json())

            data_ref = {"RefreshToken": tokens["refresh_token"], "RefreshStatus": False}
            response = self.request.post(
                self.base_url + "auth/generatetokens",
                data=json.dumps(data_ref),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn("access_token", response.json())
            self.assertIn("refresh_token", response.json())

            wrong_data = {"RefreshToken": "wrongtoken", "RefreshStatus": False}
            response = self.request.post(
                self.base_url + "auth/generatetokens",
                data=json.dumps(wrong_data),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 401)

            incomplete_data = {"RefeshStatus": True}
            response = self.request.post(
                self.base_url + "auth/generatetokens",
                data=json.dumps(incomplete_data),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 500)

        except requests.exceptions.ConnectionError:
            print("Connection Error")

    def test_admin_login(self):
        try:
            adm_data = self.admin_data()

            tokens = self.login_admin(get_refresh=True)
            self.assertIsInstance(tokens.json()["access_token"], str)
            self.assertIsInstance(tokens.json()["refresh_token"], str)

            login_data = {"Password": "wrongpwd", "Email": adm_data["Email"]}
            response = self.request.post(
                self.base_url + "admin/login",
                data=json.dumps(login_data),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 401)

            login_data = {"Password": adm_data["Password"], "Email": "wrongmail@gmail.com"}
            response = self.request.post(
                self.base_url + "admin/login",
                data=json.dumps(login_data),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 404)

            incomplete_data = {"Email": "testmail@gmail.com"}
            response = self.request.post(
                self.base_url + "admin/login",
                data=json.dumps(incomplete_data),
                headers=self.headers,
            )
            self.assertEqual(response.status_code, 500)

        except requests.exceptions.ConnectionError:
            print("Connection Error")

    def tearDown(self) -> None:
        self.cleanup()
