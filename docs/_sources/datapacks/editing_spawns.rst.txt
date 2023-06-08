
***************************
Custom Spawns via Datapacks
***************************

These packs go in ``/config/pokecube/datapacks/`` and require a reboot to apply. They can either be in a zip format, or extracted as a folder based datapack. A folder based pack may be easier to quickly adjust and edit.

Sample Datapacks:
#################

- Removing all Spawns: :download:`no_spawns.zip`
    This datapack overwrites the default files with completely blank spawns, thereby removing the existing spawns

- Adding Subbiomes and Spawns: :download:`new_subbiomes.zip`
    This datapack adds a set of new spawns, for new subbiomes `route_1` and `route_23`, these spawns have specific levels set.


.. _spawn_rules:

Json Spawn Rule Format:
-----------------------


Location selection in |Pokecube| uses a json object called a `SpawnRule`, this is used for location specific spawning, evolution, etc. Below I will discuss the general structure of these.
Here is an example of a spawns json

.. code-block:: json

    {
      "values":{
        "types":"#minecraft:is_ocean,cave",
        "typesBlacklist":"wet"
      }
    }


This example will match a location which is of types `#minecraft:is_ocean` and `cave`, and not `wet`.

Below is a list of accepted values, and what they will do.
Any below that are a list, will be separated by commas, like in `types` in the example above

-  `types` - list of types which are all required to be valid
-  `typesBlacklist` - list of types which, if present, will invalidate

-  `structures` - list of structures which are required for spawning in
-  `noStructures` - list of structures which will invalidate

-  `command` - will apply whatever this is as a `/pokemake` argument to a pokemob as it spawns in

-  `day` - valid during the day time *
-  `night` - valid at night *
-  `dust` - valid at dusk *
-  `dawn` - valid at dawn *

-  `air` - air is the material to spawn in (default `true`)
-  `water` - water is the material to spawn in (default `false`)

-  `minLight` - needs at least this much light to spawn (0-1, default 0)
-  `maxLight` - light must be less than or equal this to spawn (0-1, default 1)

-  `weather` - Specifies a list of weathers required for valid, defaults to not caring
-  `noWeather` - Specifies a list of weathers which will invalidate the rule

\* if none of these 4 are present, the rule will be valid at all times

Biome Types
~~~~~~~~~~~

For the types related fields, there are two different objects checked for validity. First, the Biome tags are checked. These use the same format as regular vanilla biome tags for names.

These will be checked first. If the listing does not match any of the Biome Types, then it will be assumed to be a Subbiome instead, and if not present, a Subbiome for the name will be added.

.. _subbiomes:

Here is the list of built in Subbiome types:

::

    none
    sky
    flower
    lake
    industrial
    meteor
    ruin
    cave
    cavewater
    village
    all


Creating the custom spawn rules
###############################

Custom spawn rules should go in the datapack under ``/data/<id>/database/pokemobs/spawns``. Examples of these files can be found in the `new_subbiomes` pack above, which uses `my_datapack` for `<id>`.

Spawn rules then generally have an additional set of values, for specifying rates, numbers, etc, and are as follows:

-  `min` - minimum number in a spawn pack (default 2)
-  `max` - maximum number in a spawn pack (default 4)
-  `rate` - chance of spawn succeeding if selected (default 0, range: 0-1)
-  `level` - override level for the spawn
-  `variance` - override variance function for the spawn

| An example of a spawn rule implementing several of these options is below:

.. code-block:: Json
    {
        "rules": [
            {
              "and_preset": "route_1",
              "entries": [
                  { "key": "rattata", "rate": 0.55, "level": 2, "variance": "x + (3 * rand())" },
                  { "key": "rattata", "rate": 0.45, "level": 2, "variance": "x + (4 * rand())" }
              ]
            },
            {
              "and_preset": "route_23",
              "entries": [
                  { "key": "sandslash", "rate": 0.05, "level": 41 },
                  { "key": "arbok", "rate": 0.05, "level": 41 }
              ]
            }
        ]
    }

Applying Custom Subbiomes ingame
################################

If an item is renamed ``subbiome-><name>``, then it can be used as a subbiome setter, and will apply the subbiome ``<name>``
This works by sneak right clicking 1 corner to set, then sneak right clicking the other corner. The volume in between will be set as the selected subbiome.
Note that to sync to the f3 menu, you may need to open the watch or pokedex's interface in that chunk

Extra Notes/Info
################

If trying to add a spawn for a Legendary |pokemob|, with a specific level and variance, you must set 

.. code-block::

      minLegendLevel = 0


in :ref:`pokecube-common.toml`.


.. include:: ../.shared.rst