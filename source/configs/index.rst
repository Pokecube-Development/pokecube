Configs
--------

These are the default config files added by Pokecube AIO

The files which end in ``-server`` are world specific. If you want to include them in a modpack, they should be placed in ``defaultconfigs`` instead of in ``configs``, and then they will be copied over to the individual worlds when created. The contents of these files get synchronized to the clients upon joining the server.

The files which end in ``-client`` contain settings which only apply client side, and the ones with ``-common`` apply to both single and multiplayer, but do not require synchronization to players on servers.

.. toctree::
   :maxdepth: 2
   :glob:

   *
