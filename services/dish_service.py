from db_engine.engine import engine, DbEngine


class DishService:
    engine: DbEngine

    def __init__(self):
        self.engine = engine

