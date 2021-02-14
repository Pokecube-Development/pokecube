********************
Commands in Pokecube
********************

Pokecube adds a variety of commands, mostly for debugging/utility purposes. These commands are discussed below.

Note that any argument which is represented surrounded by [] is optional. A large number of these commands offer tab completion, so ensure to check those options ingame for valid values.

/pokecube
#########

This is the base command for some of the ``OP`` utility commands. These commands are meant to be used by admins.

Arguments:
----------

-   ``cull``            - This will remove any wild pokemobs not near a player
-   ``kill``            - This kills all wild pokemobs
-   ``kill_all``        - this kills all pokemobs
-   ``count``           - This will display the number of each type of pokemob currently loaded, it will include wild and tamed pokemobs
-   ``restore``         - This is used to recover lost/missing pokemobs
-   ``reset <user>``    - This allows the target to select a new starter

.. _pokerestore:

/pokecube restore
~~~~~~~~~~~~~~~~~

This command then takes a few additional arguments:

-   ``check <player> [name]``  - [name] is optional, this will print a list of pokemobs owned by <player>, and clicking on the name (or the [] around the name) will teleport the user to the last known location of the pokemob. The user may need to first transfer to the dimension the pokemob was last seen in, as this command does not track the last known dimension
-   ``give <player> [name]``   - similar to ``check``, however clicking will instead give you the pokecube for the pokemob, you can then send this to the owner's PC by tossing it, or send it out by throwing it.
-   ``clear <player>``                  - This will clear the cache for the targetted player, Only use this if their cache is too corrupted to use!

There are then versions of these options, with ``_pc`` and ``_deleted``, which list pokemobs last seen in PC, or pokemobs which were intentionally released/deleted by the owner.

/pokerecall
###########

This command is used to recall pokemobs, it will only work if the target pokemob is in a loaded chunk. If a player has abandoned a pokemob somewhere, and that chunk has unloaded, this command will not work, and they will need to go back to where they left it before they can recall it.

This command takes one of the following arguments:

-   ``name``    - targets by the given name
-   ``all``     - targets all of your mobs
-   ``staying`` - targets your mobs set to "stay"
-   ``sitting`` - targets your mobs set to "sit"

.. _pokemake:

/pokemake
#########

This command will spawn a pokemob, based on the arguments given. The general format of this command is as follows:

``/pokemake <pokemob> <arguents>``

where ``<pokemob>`` is the name of the pokemob to spawn, and ``<arguments>`` is explained below:

if the first value in ``<arguments>`` is a valid player selector, then that player will be assigned ownership of the spawned mob. Otherwise, arguments are usually a single letter, optionally preceeding a ``:`` followed by a value.

Valid such arguments are below:

-   ``s``           - Makes the pokemob shiny
-   ``item:<var>``  - <var> is a valid argument for /give, it will assign this as the held item for the pokemob
-   ``l:<level>``   - Sets the level of the pokemob to <level>
-   ``f:<name>``    - Assigns the alternate texture/model for this mob, useful for unown, alcremie, etc
-   ``x:<f|m>``     - Sets the gender to male (m) or female (f)
-   ``r:<int>``     - Sets the (integer) red value for the pokemob
-   ``g:<int>``     - Sets the (integer) green value for the pokemob
-   ``b:<int>``     - Sets the (integer) blue value for the pokemob
-   ``a:<name>``    - Gives the pokemob the ability <name>
-   ``m:<name>``    - Adds <name> as a move for the mob, this argument can be repeated up to 4 times with different moves. Use :ref:`poketm` to determine the valid options for this argument
-   ``v:<x,y,z>``   - Spawns the pokemob with an offset defined by <x,y,z>
-   ``i:<ivs>``     - Sets the IVs for the mob, <ivs> should either be a single number, or a ``,`` separated list of 6 numbers
-   ``w``           - Does the same initialization as for wild spawns (may trigger evolution, etc)
-   ``h:<size>``    - Sets the mob's size
-   ``p:<nature>``  - Sets the nature of the pokemob to <nature>
-   ``n:<name>``    - Sets the nickname for the pokemob

/pokeegg
########

This command takes the same arguments as ``/pokemake``, however then converts the mob into an egg. This may result in loss of some of the information (such as nickname, etc)

.. _poketm:

/poketm
#######

This command is used as:

``/poketm <movename> [player]``

It will generate a TM for the move <movename>, and if present, will give it to [player], otherwise it will give it to the user of the command.

/pokebase
#########

This command is used to enter/exit secret bases, without needing to use the blocks created with secretpower.

.. _meteor_cmd:

/meteor
#######

This command summons an explosive meteor at the user's coordinates It takes an additional argument of the power of the blast to use, otherwise it uses a power of 100. The size of the blast can be adjusted via the meteor related options in :ref:`pokecube-common.toml` and the explosion related options in :ref:`thutcore-common.toml`.