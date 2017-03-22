# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.coordinate import Coordinate
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Triangle(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, coordinates: List[Coordinate]=None):
        """
        Triangle - a model defined in Swagger

        :param coordinates: The coordinates of this Triangle.
        :type coordinates: List[Coordinate]
        """
        self.swagger_types = {
            'coordinates': List[Coordinate]
        }

        self.attribute_map = {
            'coordinates': 'coordinates'
        }

        self._coordinates = coordinates

    @classmethod
    def from_dict(cls, dikt) -> 'Triangle':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Triangle of this Triangle.
        :rtype: Triangle
        """
        return deserialize_model(dikt, cls)

    @property
    def coordinates(self) -> List[Coordinate]:
        """
        Gets the coordinates of this Triangle.

        :return: The coordinates of this Triangle.
        :rtype: List[Coordinate]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates: List[Coordinate]):
        """
        Sets the coordinates of this Triangle.

        :param coordinates: The coordinates of this Triangle.
        :type coordinates: List[Coordinate]
        """

        self._coordinates = coordinates

