# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.coordinate import Coordinate
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model
import re

class Rectangle(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, coordinates: List[Coordinate]=None, name: str='rectangle'):
        """
        Rectangle - a model defined in Swagger

        :param coordinates: The coordinates of this Rectangle.
        :type coordinates: List[Coordinate]
        :param name: The name of this Rectangle.
        :type name: str
        """
        self.swagger_types = {
            'coordinates': List[Coordinate],
            'name': str
        }

        self.attribute_map = {
            'coordinates': 'coordinates',
            'name': 'name'
        }

        self._coordinates = coordinates
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Rectangle':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Rectangle of this Rectangle.
        :rtype: Rectangle
        """
        return deserialize_model(dikt, cls)

    @property
    def coordinates(self) -> List[Coordinate]:
        """
        Gets the coordinates of this Rectangle.

        :return: The coordinates of this Rectangle.
        :rtype: List[Coordinate]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates: List[Coordinate]):
        """
        Sets the coordinates of this Rectangle.

        :param coordinates: The coordinates of this Rectangle.
        :type coordinates: List[Coordinate]
        """

        self._coordinates = coordinates

    @property
    def name(self) -> str:
        """
        Gets the name of this Rectangle.

        :return: The name of this Rectangle.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this Rectangle.

        :param name: The name of this Rectangle.
        :type name: str
        """
        if name is not None and not re.search('', name):
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^rectangle$/`")

        self._name = name

