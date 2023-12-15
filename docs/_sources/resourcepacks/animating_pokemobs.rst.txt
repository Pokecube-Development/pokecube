***************************************
|Pokemob| Animation and Wearables Setup
***************************************

|Pokemob| animations are defined by keyframe or function animations defined in an xml file of the same name as the |pokemob|'s model.

Step 1: Making an un-zipped resourcepack
----------------------------------------

The first step to setting up for animations and wearables is to make an un-zipped resourcepack containing the xml file for the |pokemob| in question. This should go in the standard minecraft resourcepacks directory. The following example would be for adjusting animations for abra.
The following file was created in resourcepacks: ``animation_tests/assets/pokecube_mobs/gen_1/entity/models/abra.xml``. The initial contents of this XML file are copied from the default file located in the mod's jar, or downloaded from the github repository.

Also created are ``animation_tests/pack.mcmeta`` and ``animation_tests/pack.png`` for the resourcepack to be valid.

Step 2: Enabling the animation gui
-----------------------------------

This is done by assigning a hotkey for opening this gui.

.. figure:: ../_images/animation_gui/gui hotkey button.png
   :alt: animation gui hokey
   :name: hokey_setup
   :width: 600
   
   Hotkey to enable animation gui

Pressing this hotkey should open the following screen:


.. figure:: ../_images/animation_gui/initial screen.png
   :alt: Animation Gui
   :name: initial_screen
   :width: 600
   
   Initial screen for gui.

Pressing the modules button in the lower left will bring up the display for wearables setup and animation testing.

.. figure:: ../_images/animation_gui/wearables module.png
   :alt: Animation Gui
   :name: wearables_screen
   :width: 600


.. include:: ../.shared.rst