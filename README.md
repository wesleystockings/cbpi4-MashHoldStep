# Mash Hold Step plugin

This is a simple plugin to override the default behaviour of one or more mash steps (currently only the MashIn step) to allow the step to determine whether or not it should set the target temperature to 0 or not at completion.

The reason for this plugin is to allow for an apparent change in step behaviour between Craftbeerpi 3 and 4. In v3 at the completion of a step the kettle remained powered and at its setpoint, whereas in v4 you have one of two options - either automatically turn off the kettle logic associated with the step (AutoMode = Yes) or to leave it in its current state (AutoMode = No), but in both cases the kettle's target temperature is set to 0.

This change in behaviour can create an issue with workflow, particularly with a single vessel system, when both heating initial mash and when lifting the grain basket for sparging. In both cases the user may wish to keep the kettle running in Auto mode and at its last target set point - during initial strike water heating so that it maintains strike temperature until ready to add malt, and during sparging when lifting a grain basket out of a single vessel system if you don't want to immediately start ramping the kettle to boil (or simply forget to do so initially).

In this plugin, based on the standard MashIn step, it simply adds a new parameter to the step to indicate whether the target set point should be set to 0 or not and acts accordingly. This allows mash steps to use AutoMode = No and to maintain their target temperature at their conclusion. I've only bothered to implement this for the MashIn step initially since I use this step type for both initial strike water heating as well as notification of time to sparge.

### Installation:

You can install (or clone) it from the GIT Repo. In case of updates, you will find them here first:
- sudo pip3 install https://github.com/Wobbly74/cbpi4-MashHoldStep/archive/main.zip

Afterwards you will need to activate the plugin:
- cbpi add cbpi4-MashHoldStep

- this was based on Alexander Vollkopf's fork of cbpi4 available at https://github.com/avollkopf/craftbeerpi4

## Usage:

To use this custom mash step simply select the step type MashInAndHoldStep in your mash profile or recipe, just as you would for the regular MashInStep.

## Parameters:

- Additional parameter added:
	- ResetTarget: Yes | No - when set to No (default) the target temperature for the kettle is not set to 0 at step completion
	
Changelog:

- 05.01.22: Initial version
