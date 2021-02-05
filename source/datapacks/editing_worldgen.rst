
********************************
Adjusting Worldgen via Datapacks
********************************

Worldgen for Pokecube can be adjusted via datapacks. These datapacks should go in ``/config/pokecube/datapacks/`` and require a reboot to apply.

By default, there are 2 of these present, one under ``data/pokecube/structures``, and one under ``data/pokecube_legends/structures``, so those are the ones you would need to include in your datapack if you wish to override the default behaviour.

Json Format:
------------

The primary file in these datapacks is the ``worldgen.json``, located in ``/data/<modid>/structures/``. This json file is formatted as follows:

.. code-block:: json

    {
      "pools":[],
      "jigsaws":[]
    }

These are lists of the following types of objects:

-   ``pool`` - a set of buildings/features which count as generally the same type
-   ``jigsaw`` - the structure to register for worldgen, it will build features from ``pools``

Format for a pool:
~~~~~~~~~~~~~~~~~~

Below is an example of a pool:

.. code-block:: json

    {
      "name":"pokecube:scattered/ruins_rigid",
      "rigid":true,
      "biomeType":"ruin",
      "options":[
        "pokecube:scattered/ruins_rigid/ancient_tomb",
        "pokecube:scattered/ruins_rigid/ruin_1"
      ]
    }

This example pool registers a pool by the name ``pokecube:scattered/ruins_rigid``, which contains 2 options. Note that the files this references are ``/data/pokecube/scattered/ruins_rigid/ancient_tomb.nbt``, and are ``.nbt`` files produced by the vanilla structure blocks.

Options available for pools are as follows:

-   ``name`` - a unique name for this pool, this is required.
-   ``rigid`` - if false, the structure will fall to match terrain (default ``true``)
-   ``water`` - if true, the structure will be allowed to spawn below sea level (default ``false``)
-   ``biomeType`` - This is what :ref:`subbiome <subbiomes>` will be assigned to the structure.
-   ``options`` - this is a list of nbt files to include in the pool
-   ``include`` - this is a list of vanilla pools to also include in the pool

Format for a jigsaw:
~~~~~~~~~~~~~~~~~~~~

Below is an example of a jigsaw:

.. code-block:: json

    {
      "type":"pokecube:village",
      "name":"pokecube:village/plains",
      "root":"pokecube:village/plains/town_centers",
      "distance":32,
      "separation":12,
      "size":6,
      "priority":10,
      "biomeType":"village",
      "needed_once":[
        "pokecenter",
        "gym"
      ],
      "dimBlacklist":[
        "the_nether",
        "the_end"
      ],
      "spawn":{
        "values":{
          "types":"all",
          "typesBlacklist":"snowy",
          "categoryBlacklist":"desert,ocean,river,beach,mushroom,the_end,nether,savanna,mesa,taiga,icy,taiga"
        }
      }
    },

This shows most of the features of the jigsaw. It will register a structure that will show in ``/locate`` as ``pokecube:village``, and will have a structure in it called ``pokecube:village.plains``.

valid options for the jigsaw are as follows:

-   ``name`` - This is the unique identifier for this jigsaw
-   ``type`` - If specified, this is what will be registered for the structure in ``/locate``, if not specified, ``name`` is used isntead.
-   ``offset``
-   ``size`` - This is the maximum "depth" of the jigsaw, for things like villages, this represents how many times the roads are allowed to branch
-   ``distance`` - The structure is guarenteed to try to spawn at least every this many chunks
-   ``separation`` - The structure shouldn't spawn closer than this many chunks to another copy of itself
-   ``biomeType`` - Similar to in the pools, except a default for the entire structure
-   ``spawn`` - the :ref:`spawn rule<spawn_rules>` for the structure, Note that this only matches based on biome, not subbiome or local values such as weather, etc
-   ``surface`` - This spawns on the top of the ground (default ``true``)
-   ``base_under`` - This generates a "natural" base under the structure (default ``true``)
-   ``water`` - the structure will be allowed to generate under water (default ``false``)
-   ``air`` - the structure will generate a random distance above the ground, limited by ``variance`` and ``height`` (default ``false``)
-   ``allow_void`` - If false, the structure will not be allowed to spawn over an area which is lower than ``minY`` (default ``false``)
-   ``minY`` - see ``allow_void``
-   ``height`` - see ``air``
-   ``variance`` - see ``air``
-   ``needed_once`` - pool options with these flags must be present exactly once for this structure to complete
-   ``dimBlacklist`` - This structure shouldn't spawn in these dimensions
-   ``dimWhitelist`` - This allows letting the structure spawn in dimensions in the :ref:`softWorldgenDimBlacklist <pokecube-common.toml>`
