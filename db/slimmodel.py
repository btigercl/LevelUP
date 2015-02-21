from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

# ENGINE = None
# Session = None
ENGINE = create_engine("sqlite:///levelup.db", echo=True)
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
		return "Job Title: %d, Tag Name: %s, Tag Display: %s, Job_id: %s" % (id, angellist_tagdisplay, key_word, job_id)
	

class Skills(Base):
	__tablename__ = "skills"
	#The ID and tags are based upon the AngelList's tags

	id = Column(Integer, primary_key = True)
	tagdisplayname = Column(String(64), nullable=False)
	tagname = Column(String(64), nullable=False)
		
	def __repr__(self):
		return "Skills ID: %d, Skill: %s, Skill Displaytag: %s" % (id, angellist_tag_name, angellist_tagdisplay)

	

class Stack_Overflow_Trends(Base):
	__tablename__ = "trends"
		#This is the basis for the app's trending data. It links to the Skills table for normalization purposes.

	id = Column(String(64), primary_key=True) #this will be skill_table_id plus epoctime to avoid dups
	skill_id = Column(Integer, nullable= False)
	skill = Column(String(64), nullable= False) 
	date_epoc = Column(DateTime(timezone=False), nullable=False)
	question_count = Column(Integer, nullable=False)

	# skills = relationship("Skills",
	# 	backref=backref("trends", order_by=id))

	def __repr__(self):
		return "Key_word: %s, Month_Year: %r, Monthly_Occurances: %d" % (keyword, mon_year, monthly_occurances)

def get_jobtitles_list():
		jobtitles_list = Session.query(JobTitle).all()
		return jobtitles_list

def get_skills_list():
		skill_list = Session.query(Skills).all()
		return skill_list

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///levelup.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

if __name__ == "__main__":
    main()