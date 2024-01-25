# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Medicin(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id_sensor: str=None, fecha_muestreo: str=None, unidad: str=None, medicion: float=None):  # noqa: E501
        """Medicin - a model defined in Swagger

        :param id_sensor: The id_sensor of this Medicin.  # noqa: E501
        :type id_sensor: str
        :param fecha_muestreo: The fecha_muestreo of this Medicin.  # noqa: E501
        :type fecha_muestreo: str
        :param unidad: The unidad of this Medicin.  # noqa: E501
        :type unidad: str
        :param medicion: The medicion of this Medicin.  # noqa: E501
        :type medicion: float
        """
        self.swagger_types = {
            'id_sensor': str,
            'fecha_muestreo': str,
            'unidad': str,
            'medicion': float
        }

        self.attribute_map = {
            'id_sensor': 'id_sensor',
            'fecha_muestreo': 'fecha_muestreo',
            'unidad': 'unidad',
            'medicion': 'medicion'
        }

        self._id_sensor = id_sensor
        self._fecha_muestreo = fecha_muestreo
        self._unidad = unidad
        self._medicion = medicion

    @classmethod
    def from_dict(cls, dikt) -> 'Medicin':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Medición of this Medicin.  # noqa: E501
        :rtype: Medicin
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_sensor(self) -> str:
        """Gets the id_sensor of this Medicin.


        :return: The id_sensor of this Medicin.
        :rtype: str
        """
        return self._id_sensor

    @id_sensor.setter
    def id_sensor(self, id_sensor: str):
        """Sets the id_sensor of this Medicin.


        :param id_sensor: The id_sensor of this Medicin.
        :type id_sensor: str
        """

        self._id_sensor = id_sensor

    @property
    def fecha_muestreo(self) -> str:
        """Gets the fecha_muestreo of this Medicin.


        :return: The fecha_muestreo of this Medicin.
        :rtype: str
        """
        return self._fecha_muestreo

    @fecha_muestreo.setter
    def fecha_muestreo(self, fecha_muestreo: str):
        """Sets the fecha_muestreo of this Medicin.


        :param fecha_muestreo: The fecha_muestreo of this Medicin.
        :type fecha_muestreo: str
        """

        self._fecha_muestreo = fecha_muestreo

    @property
    def unidad(self) -> str:
        """Gets the unidad of this Medicin.


        :return: The unidad of this Medicin.
        :rtype: str
        """
        return self._unidad

    @unidad.setter
    def unidad(self, unidad: str):
        """Sets the unidad of this Medicin.


        :param unidad: The unidad of this Medicin.
        :type unidad: str
        """

        self._unidad = unidad

    @property
    def medicion(self) -> float:
        """Gets the medicion of this Medicin.


        :return: The medicion of this Medicin.
        :rtype: float
        """
        return self._medicion

    @medicion.setter
    def medicion(self, medicion: float):
        """Sets the medicion of this Medicin.


        :param medicion: The medicion of this Medicin.
        :type medicion: float
        """

        self._medicion = medicion
