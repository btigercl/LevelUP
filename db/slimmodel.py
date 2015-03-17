from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

# ENGINE = None
# Session = None
ENGINE = create_engine("sqlite:///db/levelup.db", echo=True)
Session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = Session.query_property()

#Class declaratison
class JobTitle(Base):
	__tablename__ = "jobtitle"
		#The ID and tags are based upon the AngelList's tags

	id = Column(Integer, primary_key = True)
	tagdisplay = Column(String, nullable=False)
	tagname = Column(String, nullable=False) 
	jobtitle = Column(String(64), nullable=False)

	def __repr__(self):
		return "Job Title: %d, Tag Name: %s, Tag Display: %s, Job_id: %s" % (self.id, self.tagdisplay, self.tagname, self.jobtitle)
	

class Skills(Base):
	__tablename__ = "skills"
	#The ID and tags are based upon the AngelList's tags

	id = Column(Integer, primary_key = True)
	tagdisplayname = Column(String(64), nullable=False)
	tagname = Column(String(64), nullable=False)
		
	def __repr__(self):
		return "Skills ID: %d, Skill: %s, Skill Displaytag: %s" % (self.id, self.tagdisplayname, self.tagname)

	

class Stack_Overflow_Trends(Base):
	__tablename__ = "trends"
		#This is the basis for the app's trending data. It links to the Skills table for normalization purposes.

	id = Column(String(64), primary_key=True) #this will be skill_table_id plus epoctime to avoid dups
	skill_id = Column(Integer, nullable= False)
	skill = Column(String(64), nullable= False) 
	date_epoc = Column(DateTime(timezone=False), nullable=False)
	question_count = Column(Integer, nullable=False)

	def __repr__(self):
		return "Main ID: %r, Skill ID: %r, Skill: %s, Date of Occurance: %r, Question Count: %r" % (self.id, self.skill_id, self.skill, self.date_epoc, self.question_count)

def get_jobtitles_list():
	jobtitles_list = Session.query(JobTitle).all()
	return jobtitles_list

def get_skills_list():
	skill_list = Session.query(Skills).all()
	return skill_list

def get_trend_list():
	trend_list = Session.query(Stack_Overflow_Trends).all()
	return trend_list

def get_skill_display_name():
	display_name = Session.query(Skills.tagdisplayname).all()
	return display_name

def get_skill_by_tagname(tagname_passed):
	obj = Session.query(Skills).filter_by(tagname=tagname_passed).first()
	return obj

def get_skill_by_id(passed_id):
	skill_obj = Session.query(Skills).filter_by(id=passed_id).first()
	return skill_obj

def get_skill_by_name(passed_name):
	skill_obj = Session.query(Skills).filter_by(tagdisplayname=passed_name).first()
	return skill_obj

def get_trend_skill_name():
	skill_name_list = Session.query(Stack_Overflow_Trends.skill).filter(Stack_Overflow_Trends.skill != 'question').distinct().order_by('skill').all()
	return skill_name_list

def get_trend_by_name(name):
	single_entry = Session.query(Stack_Overflow_Trends).filter_by(skill=name).all()
	return single_entry

def get_trend_by_skill_id(passed_id):
	trend_name = Session.query(Stack_Overflow_Trends.skill).filter_by(skill_id=passed_id).first()
	return trend_name[0]

def get_question_count_by_date(date):
	single_entry = Session.query(Stack_Overflow_Trends.question_count).filter_by(skill="question", date_epoc=date).first()
	return single_entry

# def connect():
#     global ENGINE
#     global Session

#     ENGINE = create_engine("sqlite:///levelup.db", echo=True)
#     Session = sessionmaker(bind=ENGINE)

#     return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()