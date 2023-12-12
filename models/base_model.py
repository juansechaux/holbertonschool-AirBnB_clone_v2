#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from sqlalchemy import DateTime, Column, String
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:

            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())
            if "created_at" not in kwargs:
                kwargs["created_at"] = datetime.now()
            else:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f'
                )
            if "updated_at" not in kwargs:
                kwargs["updated_at"] = datetime.now()
            else:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f'
                )

            if "__class__" in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    # def __init__(self, *args, **kwargs):
    #     """Instatntiates a new model"""
    #     if not kwargs:
    #         # !!!!!!!!!Update BaseModel puntito 4
    #         self.id = str(uuid.uuid4())
    #         self.created_at = datetime.now()
    #         self.updated_at = datetime.now()
    #         # !!!!!!!!!Update BaseModel puntito 4
    #     else:
    #         kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
    #                                                  '%Y-%m-%dT%H:%M:%S.%f')
    #         kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
    #                                                  '%Y-%m-%dT%H:%M:%S.%f')
    #         # !!!!!!!!!Update BaseModel puntito 5
    #         for key, value in kwargs.items():
    #             if key != '__class__' and not hasattr(self, key):
    #                 setattr(self, key, value)

    #         del kwargs['__class__']
    #         self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)  # !!!!!!!!!Update BaseModel puntito 4
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # Eliminar la clave "_sa_instance_state" si está presente
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        '''Delete the current instance from the storage'''
        models.storage.delete()
