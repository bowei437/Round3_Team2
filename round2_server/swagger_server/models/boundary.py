# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.coordinate import Coordinate
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Boundary(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, boundary_info: List[Coordinate]=None):
        """
        Boundary - a model defined in Swagger

        :param boundary_info: The boundary_info of this Boundary.
        :type boundary_info: List[Coordinate]
        """
        self.swagger_types = {
            'boundary_info': List[Coordinate]
        }

        self.attribute_map = {
            'boundary_info': 'boundary_info'
        }

        self._boundary_info = boundary_info

    @classmethod
    def from_dict(cls, dikt) -> 'Boundary':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Boundary of this Boundary.
        :rtype: Boundary
        """
        return deserialize_model(dikt, cls)

    @property
    def boundary_info(self) -> List[Coordinate]:
        """
        Gets the boundary_info of this Boundary.

        :return: The boundary_info of this Boundary.
        :rtype: List[Coordinate]
        """
        return self._boundary_info

    @boundary_info.setter
    def boundary_info(self, boundary_info: List[Coordinate]):
        """
        Sets the boundary_info of this Boundary.

        :param boundary_info: The boundary_info of this Boundary.
        :type boundary_info: List[Coordinate]
        """

        self._boundary_info = boundary_info
