from authx import AuthX, AuthXConfig
from src.configs import AuthSettings


class AuthService:
    config: AuthXConfig = AuthXConfig()
    config.JWT_SECRET_KEY = AuthSettings.JWT_SECRET_KEY
    config.JWT_ACCESS_COOKIE_NAME = "csmoney_token"
    config.JWT_TOKEN_LOCATION = "cookie"
    auth_security: AuthX = AuthX(config=config)
