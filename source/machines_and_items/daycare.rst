.. _daycare:

*************
Daycare Block
*************

.. image:: ../_images/machines_items/daycare.*

The Daycare Block converts emeralds into EXP for nearby |pokemobs|. You must use a hopper, or similar to get the emeralds into the block, and you can also use a hopper to get un-used emeralds out of the block.

The options mentioned below are all located in the ``[machine]`` section of :ref:`pokecube_adventures-common.toml`.

when a |pokemobs| is near the the daycare block, the following will occur:

1. They will gain the amount of EXP specified by ``dayCareExpFunction``
2. Their breeding cooldown will have ``dayCareBreedAmount`` applied to it, depending on the setting of ``dayCareBreedSpeedup``
3. Depending on the amount of power needed by the above functions (specified via ``dayCarePowerPerExp``), emeralds will be consumed. The number of emeralds consumed depends on the value of ``dayCarePowerPerFuel``, and for applying the breeding cooldown to a lvl 100 pokemob, it will instead cost power as if the pokemob was the level specified in ``dayCareLvl100EffectiveLevel``.

These will happen every ``dayCareTickRate`` ticks, so lower values for that will result in faster action of the daycare block.