from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from pearson import pearson

ENGINE = create_engine("sqlite:///ratings.db", echo=True)
Session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = Session.query_property()

#Class declaratison
class NexusTable(Base):
	__tablename__ = "nexustable"

	id = Column(Integer, primary_key=True)
	skill_id = Column(Integer, ForeignKey("skills.id"))
	jobtitle_id = Column(Integer, ForeignKey("jobtitle.id"))
	joblisting_id = Column(Integer, ForeignKey("joblisting.id"))

	skills = relationship("Skills",
        backref=backref("nexustable", order_by=id))

	jobtitle = relationship("JobTitle",
        backref=backref("rating", order_by=id))

   	joblisting = relationship("JobListing",
        backref=backref("nexustable", order_by=id))
 
	def __repr__(self):
		return "NexusColumn ID: %d, Skill ID: %d, Job Title ID: %d, Job Listing ID: %d" % (id, skill_id, jobtitle_id, joblisting_id)

class JobListing(Base):
	__tablename__ = "joblisting"

	id = Column(String(20), primary_key = True)
	date_posted = Column(DateTime(timezone=False), nullable=False)
	jobtitle = Column(String(64), nullable=False)
	role_tag = Column(Integer, nullable=True)
	company = Column(String(64), nullable=False) 
	description = Column(String(1000), nullable=True)
	location = Column(String(100), nullable=True) 


	def __repr__(self):
		return "JobListing_id: %d, Date Posted: %r, Jobtitle: %s, Role Tag Company: %s,\
		 Description: %s, Location: %s"\
		 % (id, date_posted, jobtitle, role_tag, company, description, location)

class JobTitle(Base):
	__tablename__ = "jobtitle"

	id = Column(Integer, primary_key = True)
	angellist_tag_display = Column(String, nullable=True)
	angellist_tag_name = Column(String, nullable=True) 
	jobtitle = Column(String(64) nullable=False)

	def __repr__(self):
		return "Job Title: %d, Tag Name: %s, Tag Display: %s, Job_id: %s" % (id, angellist_tagdisplay, key_word, job_id)

class Skills(Base):
	__tablename__ = "skills"

	id = Column(Integer, primary_key = True)
	angellist_tagdisplayname = Column(String(64), nullable=True)
	angellist_tagname = Column(String(64), nullable=False)


	# job_id = Column(String(64), ForeignKey('job_id'))
	def __repr__(self):
		return "Skills ID: %d, Skill: %s, Skill Displaytag: %s" % (id, angellist_tag_name, angellist_tagdisplay)


class Trends(Base):
	__tablename__ = "Trends"

	keyword = Column(String(64), primary_key = True)
	mon_year = Column(DateTime(timezone=False), nullable=False)
	monthly_occurances = Column(Integer, nullable=False)

	def __repr__(self):
		return "Key_word: %s, Month_Year: %r, Monthly_Occurances: %d" % (keyword, mon_year, monthly_occurances)


class DemandLocation(Base):
	__tablename__ = "demandlocation"

	id = Column(Integer, primary_key = True)
	date_posted = Column(DateTime(timezone=False), nullable=False)
	jobtitle = Column(String(64), nullable=True)
	skill = Column(String(64), nullable=True)
	company = Column(String(64), nullable=False) 
	description = Column(String(500), nullable=True)
	location = Column(String(100), nullable=True) 
	latitude = Column(String(64), nullable=True)
	longitude = Column(String(64), nullable=True)

# def main():
#     """In case I need this for something"""
#     pass

if __name__ == "__main__":
    main()