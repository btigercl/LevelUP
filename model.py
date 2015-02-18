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
class JobTitle(Base):
	__tablename__ = "jobtitle"

	id = Column(Integer, primary_key = True)
	jobtitle = Column(String(64) nullable=False)


class JobListing(Base):
	__tablename__ = "joblisting"

	id = Column(Integer, primary_key = True)
	jobtitle = Column(String(64), nullable=False)
	company = Column(String(64), nullable=False)
	description = Column(String(500), nullable=False) 
	skills = Column(String(500), nullable=False)
	latitude = Column(String(64), nullable=True)
	longitude = Column(String(64), nullable=True)


	def __repr__(self):
		return "JobListing_id: %d, Jobtitle: %s, Company: %s, Description: %s, Requirements: %s, Latitude: %s, Longitude: %s" % (id, jobtitle, company, description, requirements, latitude, longitude )

class JobDescriptionSkills(Base):
	__tablename__ = "jdkeywords"

	id = Column(Integer, primary_key = True)
	key_word = Column(String(64), nullable=False)
	# job_id = Column(String(64), ForeignKey('job_id'))

	# joblisting = relationship("JobListing",
	# 	backref=backref("jdkeywords", order_by=id))

	def __repr__(self):
		return "JobDescriptionKeyWords_id: %d, Key_word: %s, Job_id: %s" % (id, key_word, job_id)


class KeyWordTags(Base):
	__tablename__ = "keywordtags"

	keyword = Column(String(64), primary_key = True)
	mon_year = Column(DateTime(timezone=False), nullable=False)
	monthly_occurances = Column(Integer, nullable=False)

	def __repr__(self):
		return "Key_word: %s, Month_Year: %r, Monthly_Occurances: %d" % (keyword, mon_year, monthly_occurances)


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()