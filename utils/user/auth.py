import hashlib


class AuthClient:
    """
    Класс для регистрации, авторизации и управления сессиями пользователей.
    """
    async def _hash_password(self, password: str) -> str:
        """
        Хэширует пароль для отправки на сервер.
        """
        return hashlib.sha3_512(password.encode('utf-8')).hexdigest()

    async def register(self,fio:str, password):
        ...
    # async def _get_headers(self, request: Request) -> dict:
    #     """
    #     Формирует заголовки для запросов.
    #     """
    #     token = request.cookies.get("access_token")
    #     return {
    #         "Accept": "application/json",
    #         "Authorization": f"Bearer {token}" if token else "",
    #     }

    # async def login(self, fastapi_response: Response, user: User) -> StatusMessage | DetailMessage:
    #     """
    #     Выполняет вход пользователя.
    #
    #     :param fastapi_response: Response: объект для управления куками
    #     :param user: User: данные пользователя для входа
    #     :return: Статус операции.
    #     """
    #     async with aiohttp.ClientSession() as session:
    #         payload = {
    #             "username": user.username,
    #             "password": await self._hash_password(user.password),
    #         }
    #         async with session.post(url=f"{settings.base_url}{settings.login_url}", data=payload) as response:
    #             try:
    #                 response.raise_for_status()
    #                 resp = await response.json()
    #                 fastapi_response.set_cookie("access_token", resp["data"]["token"])
    #                 return settings.success
    #             except ClientResponseError:
    #                 return settings.incorrect_data
    #
    # async def logout(self, request: Request) -> StatusMessage | DetailMessage:
    #     """
    #     Выполняет выход пользователя.
    #
    #     :param request: Request: текущий запрос
    #     :return: Статус запроса.
    #     """
    #     async with aiohttp.ClientSession() as session:
    #         headers = await self._get_headers(request)
    #         async with session.get(f"{settings.base_url}{settings.logout_url}", headers=headers) as response:
    #             try:
    #                 response.raise_for_status()
    #                 return await response.json()
    #             except ClientResponseError:
    #                 return settings.unauthorized


auth_client = AuthClient()
