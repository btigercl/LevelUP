from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

# ENGINE = None
# Session = None

ENGINE = create_engine("sqlite:///db/json.db", echo=True)
Session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = Session.query_property()

class Stored_JSON_Objects(Base):
	__tablename__ = "stored_objects"
		#This table holds json objects in order to "cahce" api calls, and make the app faster. This cache should be updated everday programatically. 

	id = Column(Integer, primary_key=True)
	skill_name = Column(String(64), nullable= False)
	skill_obj = Column(String(100000), nullable=False)
	date_stored = Column(DateTime(timezone=False), nullable=False)

	def __repr__(self):
		return "Main ID: %r, Skill Name: %s, JSON Object: %r, Date Stored: %r" (self.id, self.skill_name, self.skill_obj, self.date_stored)

def get_object_by_skill_name(skill_name_passed):
	json_obj = Session.query(Stored_JSON_Objects).filter_by(skill_name=skill_name_passed).first()
	return json_obj

def add_skill_object(skill_id, skill_name_passed, json_string, date):
	new_skill_object = Stored_JSON_Objects(id=skill_id, skill_name=skill_name_passed, skill_obj=json_string, date_stored=date)
	Session.add(new_skill_object)
	Session.commit()

def updating_skill_object(skill_name_passed, new_json, new_date):
	skill_object_stored = Session.query(Stored_JSON_Objects).filter_by(skill_name=skill_name_passed).first()
	skill_object_stored.skill_object = new_json
	skill_object_stored.date_stored = new_date


def main():
    pass

if __name__ == "__main__":
    main()


# def connect():
#     global ENGINE
#     global Session

#     ENGINE = create_engine("sqlite:///json.db", echo=True)
#     Session = sessionmaker(bind=ENGINE)

#     return Session()

# def main(session):


# if __name__ == "__main__":
#     s= model.connect()
#     main(s)