
import sqlalchemy as db
DATABASE_NAME = 'Pythagoras.db'
TABLE_NAME = 'different_info'
engine = db.create_engine(f'sqlite:///{DATABASE_NAME}')

connection = engine.connect()

metadata = db.MetaData()

general_info = db.Table(TABLE_NAME, metadata,
                        db.Column('name', db.Integer, primary_key=True),
                        db.Column('info_ru', db.Text),
                        db.Column('info_en', db.Text),
                        db.Column('info_de', db.Text),
                        db.Column('info_ua', db.Text)
                        )
