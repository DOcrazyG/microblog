import os

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///" + os.path.join(
        basedir, "app.db"
    )
    POSTS_PER_PAGE = 3

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    ADMINS = ["1379825060@qq.com"]

    LANGUAGES = ["en", "es"]

    TRANSLATION_APP_ID = os.getenv("TRANSLATION_APP_ID")
    TRANSLATION_API_KEY = os.getenv("TRANSLATION_API_KEY")


if __name__ == "__main__":
    print(Config.SECRET_KEY)
    print(Config.MAIL_SERVER)
