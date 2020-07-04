import time
import sys
import ibmiotf.application
import ibmiotf.device

#  IBM Watson Device Credentials each device has its own credentials

# To acess different bus different credential is listed below

# ------------------------------------------------------------------

# for BUS_NUMBER 29C:
#Device Type = "bus29c"
#Device ID = "0029"
#AuthMethod = "token"
#AuthToken = "123456729"

# --------------------------------------------------------------
# FOR BUS_NUMBER 28F:
#Device Type="bus28f"
#Device ID = "0028"
#AuthMethod = "token"
#AuthToken ="123456728"

# ---------------------------------------------------------------
#For BUS_NUMBER 7G:
#Device Type ="bus7g"
#Device ID ="0007"
#AuthMethod = "token"
#AuthToken ="123456787"

# ------------------------------------------------------------------
#FOR BUS_NUMBER BUS12A :
#Device Type = "bus12a"
#Device ID = "0012"
#AuthMethod = "token"
#AuthToken = "123456712"

#------------------------------------------------------------------
#FOR BUS_NUMBER BUS46G :
#Device Type = "bus46g"
#Device ID = "0046"
#AuthMethod = "token"
#AuthToken = "123456746"

#------------------------------------------------------------------
#FOR BUS_NUMBER BUS6a :
#Device Type = "bus6a"
#Device ID = "0006"
#AuthMethod = "token"
#AuthToken = "123456786"

#-----------------------------------------------------------------
#FOR BUS_NUMBER BUS23E:
#Device Type = "bus23e"
#Device ID = "0023"
#AuthMethod = "token"
#AuthToken = "123456723"

#-------------------------------------------------------------------

# SAMPLE VALUE TO ACCESS THE DEVICE IS SHOWN BELOW  :)

organization = "xkpuae"  # organization ID
deviceType = "bus1a"  # device type
deviceId = "0001"  # device id
authMethod = "token"
authToken = "123456781"  # token







try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod,
                     "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)


except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

deviceCli.connect()
# !! AS WE ARE REPLACING HARDWARE WITH PYTHON PROGRAMMING THE COUNT AND THE LOCATION VALUES ARE TO BE ENTRED MANUALLY !!!

C=31
S='ONLINE'
L='12a'
while True:
    data = {'d': {'Location': L, 'Count': C,'Live': S}} #data formate


    def myOnPublishCallback():                            # to determine the location and count values

        print("Location = %s " % L, "Count = %s " % C, "Live = %s " % S, "to IBM Watson ")

    success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Problem in  connecting  to IOT platform")
    time.sleep(3)



deviceCli.disconnect()