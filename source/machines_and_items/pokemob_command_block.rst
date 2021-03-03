.. _pokemob_commander:

***********************
|Pokemob| Command Block
***********************

.. image:: ../_images/machines_items/commander.*

This block allows using redstone signals, or a ComputerCraft interface to issue commands to a |pokemob|. To link a |pokemob| to the commander, you right click it with the cube containing said mob, this page will mostly discuss the redstone signal applications.

.. image:: ../_images/machines_items/commander_gui.*

The commander block has a very simple GUI. It contains the command type to send, and then the arguments for those commands. The arguments will be discussed below for each type of command:

-   ``ATTACKENTITY`` - ``<id>`` - Attacks mob with given entity ID, not really useful as no way to get this with just |Pokecube|
-   ``ATTACKLOCATION`` - ``<X> <Y> <Z>`` - Tells the |pokemob| to attack the given location, the :ref:`location_linker` can be used to get these coordinates
-   ``ATTACKNOTHING`` - No arguments, just uses the attack, this can be used for healing/self moves, etc
-   ``CHANGEMOVEINDEX`` - ``<Index>`` - Changes the selected move for the |pokemob|
-   ``CHANGEFORM`` - Commands your |pokemob| to change form, similar to the mega evolve key
-   ``MOVETO`` - ``<X> <Y> <Z> <S>`` - Tells the |pokemob| to move to the given location, with a speed specified by ``<S>``
-   ``STANCE`` - ``<value> <state>`` - this changes the "stance" of the |pokemob|, ``<value>`` is ``true`` (for on) or ``false`` for (off), and ``<state>`` is one of the following:

    -   ``0``   - Stay on/off
    -   ``1``   - Guard on/off
    -   ``2``   - Sit on/off
    -   ``3``   - Using G/Z Move on/off

-   ``SWAPMOVES`` - ``<A> <B>`` - Swaps moves of index ``<A>`` and ``<B>``
-   ``TELEPORT``  - No arguments, tells the |pokemob| to use teleport, this will mosty likely teleport the owner to the last selected teleport location, not very useful in general

The command is applied by sending a redstone pulse to the block. Multiple commander blocks can be linked to the same |pokemob|.

.. include:: ../.shared.rst