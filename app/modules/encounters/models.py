# encoding: utf-8
"""
Encounters database models
--------------------
"""

from sqlalchemy_utils import Timestamp

from app.extensions import db

import uuid


class Encounter(db.Model, Timestamp):
    """
    Encounters database model.
    """

    guid = db.Column(
        db.GUID, default=uuid.uuid4, primary_key=True
    )  # pylint: disable=invalid-name
    title = db.Column(db.String(length=50), nullable=False)

    def __repr__(self):
        return (
            '<{class_name}('
            'guid={self.id}, '
            'title=\'{self.title}\''
            ')>'.format(
                class_name=self.__class__.__name__,
                self=self
            )
        )

    @db.validates('title')
    def validate_title(self, key, title):  # pylint: disable=unused-argument,no-self-use
        if len(title) < 3:
            raise ValueError('Title has to be at least 3 characters long.')
        return title
