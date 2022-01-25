from code import compile_command
from decimal import Clamped, Inexact
from fileinput import close
from lib2to3.pgen2.token import STRING
from msilib.schema import Component
from multiprocessing.pool import CLOSE
from re import T
from sqlite3 import IntegrityError, InternalError
from tkinter.messagebox import QUESTION
from typing import Collection
from xml.etree.ElementTree import TreeBuilder
from xmlrpc.client import Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import BOOLEAN, DATETIME, INTEGER, ARRAY, Column, DateTime, ForeignKey, Integer, String, Date, column
from sqlalchemy.orm import relationship

Base = declarative_base()

# class Book(Base):
#     __tablename__ = 'books'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     author = Column(String)
#     pages = Column(Integer)
#     published = Column(Date)
    
#     def __repr__(self):
#         return "<Book(title='{}', author='{}', pages={}, published={})>"\
#                 .format(self.title, self.author, self.pages, self.published)

class Qestion(Base):

    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime)
    is_asnwered = Column(BOOLEAN)
    views = Column(Integer)
    votes_count = Column(Integer)
    bookmarks_count = Column(Integer)
    answers_coun = Column(Integer)
    tags = Column(String) #list
    comment_count = Column(Integer)
    closed = Column(BOOLEAN)
    closed_reason = Column(String)

    user_id = Column(Integer, ForeignKey('user.id'))

    #relations
    answers = relationship("Answer")
    comments = relationship("Comment")
    tags = relationship("Tag")

class Answer(Base):
    
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    created_at = Column(DateTime)
    is_accepted = Column(BOOLEAN)
    votes_count = Column(Integer)

    question_id = Column(Integer, ForeignKey('question.id'))


class Comment(Base):

    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    created_at = Column(DateTime)
    votes_count = Column(Integer)

    answer_id = Column(Integer, ForeignKey('answer.id'))
    question_id = Column(Integer, ForeignKey('question.id'))
    comments = relationship("Comment")

    #Relations
    comment_id = Column(Integer, ForeignKey('comment.id'))

class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    age = Column(Integer)
    created_at = Column(DateTime)
    location = Column(String)
    bookmarks = Column(String)
    badges = Column(String)
    question_count = Column(Integer)
    answer_count = Column(Integer)

    #relations
    questions = relationship("Question")


class Tag(Base):

    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    question_count = Column(Integer)

    question_id = Column(Integer, ForeignKey('question.id'))

class Question_Answer_Comment(Base):

    __tablename__ = 'question_answer_comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    question_id = Column(Integer, ForeignKey('question.id'))
    answer_id = Column(Integer, ForeignKey('answer.id'))
    