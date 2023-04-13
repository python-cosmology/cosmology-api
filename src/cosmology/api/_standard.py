"""The API for the standard cosmology."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from cosmology.api._array_api import ArrayT_co
from cosmology.api._components import (
    BaryonComponent,
    CurvatureComponent,
    DarkEnergyComponent,
    DarkMatterComponent,
    MatterComponent,
    NeutrinoComponent,
    PhotonComponent,
    TotalComponent,
)
from cosmology.api._core import Cosmology, InputT_contra
from cosmology.api._distances import DistanceMeasures
from cosmology.api._extras import CriticalDensity, HubbleParameter

__all__: list[str] = []


@runtime_checkable
class StandardCosmology(
    NeutrinoComponent[ArrayT_co, InputT_contra],
    BaryonComponent[ArrayT_co, InputT_contra],
    PhotonComponent[ArrayT_co, InputT_contra],
    DarkMatterComponent[ArrayT_co, InputT_contra],
    MatterComponent[ArrayT_co, InputT_contra],
    DarkEnergyComponent[ArrayT_co, InputT_contra],
    CurvatureComponent[ArrayT_co, InputT_contra],
    TotalComponent[ArrayT_co, InputT_contra],
    HubbleParameter[ArrayT_co, InputT_contra],
    CriticalDensity[ArrayT_co, InputT_contra],
    DistanceMeasures[ArrayT_co, InputT_contra],
    Cosmology[ArrayT_co, InputT_contra],
    Protocol,
):
    """API Protocol for the standard cosmology and expected set of components.

    This is a protocol class that defines the standard API for the standard
    (FLRW-like) cosmology cosmology. It is not intended to be instantiaed.
    Instead, it should be used for ``isinstance`` checks or as an ABC for
    libraries that wish to define a compatible cosmology class.
    """

    # Override from the base classes, for better docstring.
    @property
    def Omega_tot0(self) -> ArrayT_co:
        r"""Omega total; the total density/critical density at z=0.

        .. math::

            \Omega_{\rm tot} = \Omega_{\rm m} + \Omega_{\rm \gamma} +
            \Omega_{\rm \nu} + \Omega_{\rm de} + \Omega_{\rm k}

        Returns
        -------
        Array
        """
        ...

    # Override from the base classes, for better docstring.
    def Omega_tot(self, z: InputT_contra, /) -> ArrayT_co:
        r"""Redshift-dependent total density parameter.

        This is the sum of the matter, radiation, neutrino, dark energy, and
        curvature density parameters.

        .. math::

            \Omega_{\rm tot} = \Omega_{\rm m} + \Omega_{\rm \gamma} +
            \Omega_{\rm \nu} + \Omega_{\rm de} + \Omega_{\rm k}

        Parameters
        ----------
        z : Array
            Input redshift(s).

        Returns
        -------
        Array
        """
        ...
