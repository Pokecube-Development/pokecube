.. _warppad:

********
Warp Pad
********

.. image:: ../_images/machines_items/warppad.*

The Warp Pad is a block which consumes Forge Energy to teleport mobs that step on it to a linked location. The amount of energy stored, and the energy cost to teleport can be configured via the ``warpPadMaxEnergy`` and ``warpPadCostFunction`` options in :ref:`pokecube_adventures-common.toml`, or energy cost can be entirely disabled via ``warpPadEnergy``. Individual Warp Pads may also have their energy cost disabled via NBT Editing.


Linking to a destination
~~~~~~~~~~~~~~~~~~~~~~~~

The Warp Pad is linked to a destination using the :ref:`location_linker`, It should not be linked to another Warp Pad! Right clicking the Warp Pad with the linker will link it to the stored location.

Linking to Siphon
~~~~~~~~~~~~~~~~~

To create a remote link to an :ref:`siphon`, the location where you are about to place the Warp Pad must first be selected with a :ref:`location_linker`. This generally means the following steps:

1. Place a dirt block where you want to place the Warp Pad
2. Use the linker on the dirt block
3. Replace the dirt block with the Warp Pad
4. Link the :ref:`siphon` to the location stored in the linker






.. include:: ../.shared.rst