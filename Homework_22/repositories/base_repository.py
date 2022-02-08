from sqlalchemy import create_engine

from sqlalchemy.orm import Session, sessionmaker

from ..core.config import Config

from ..core.singleton import Singleton


class BaseRepository(Singleton):
    def __init__(self) -> None:
        self.__config = Config()

        self.__engine = create_engine(f"{self.__config.driver_name}://{self.__config.user}:"
                                      f"{self.__config.password}@{self.__config.host}:"
                                      f"{self.__config.port}/{self.__config.database}")
        self.session: Session = sessionmaker(self.__engine)()
