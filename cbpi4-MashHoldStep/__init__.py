import logging
from cbpi.api import *
from cbpi.api.step import CBPiStep
from cbpi.api.dataclasses import NotificationAction, NotificationType
from cbpi.extension.mashstep import MashInStep

logger = logging.getLogger(__name__)

@parameters([Property.Number(label="Temp", configurable=True),
             Property.Sensor(label="Sensor"),
             Property.Kettle(label="Kettle"),
             Property.Text(label="Notification",configurable = True, description = "Text for notification when Temp is reached"),
             Property.Select(label="AutoMode",options=["Yes","No"], description="Switch Kettlelogic automatically on and off -> Yes"),
             Property.Select(label="ResetTarget",options=["Yes","No"], description="Reset Kettle target to 0 at step completion? Default: No")])
class MashInAndHoldStep(MashInStep):
    
    async def on_timer_done(self,timer):
        self.summary = ""
        # Replace self.kettle.target_temp = 0 with a check of whether to reset target temp or not
        if self.props.get("ResetTarget","No") == "No":
            #self.kettle.target_temp = int(self.props.get("Temp", 0))
            pass
        else:
            self.kettle.target_temp = 0
            await self.push_update()
        if self.AutoMode == True:
            await self.setAutoMode(False)
        self.cbpi.notify(self.name, self.props.get("Notification","Target Temp reached. Please add malt and click next to move on."), action=[NotificationAction("Next Step", self.NextStep)])


def setup(cbpi):
    cbpi.plugin.register("MashInAndHoldStep", MashInAndHoldStep)
