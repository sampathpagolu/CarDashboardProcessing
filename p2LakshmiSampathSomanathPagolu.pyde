transmissionRatios = [3.35, 1.93, 1.29, 1.0, 0.68] # individual transmission ratios of each gear. Assuming the car has 5 gears excluding Reverse and Neutral
rearEndRatio = 3.15 #:1
tireSize = 29 # inches 
speed = 0
# fuel = 50
mpg = 30 # miles per gallon
constant = 336 # RPM constant
totalTime = 0





def setup():
    size(1000,500)
    


def draw():
    translate(0, 50)
    # print(mouseX, mouseY)
    dashboard()
    saveFrame("./final/gif-########.png")
        
    

def dashboard():
    background(19,19,19)
    moving = False
    global totalTime
    global speed
    distance = 0


    if speed != 0:
        moving = True
    # print(moving)
    warningSigns()
    initTime = millis() # finding time to calculate distance
    speedDisplay(floor(speed))
    # speed = speedCalculation()
    RPM = RPMSpeedCalculation()
    totalTime = totalTime + (millis() - initTime)
    displayRPM(RPM)
    displayDistance(calculateDistance(totalTime, RPM, moving))
    fuel(distance)
    turnSignals()
    engineTemperature()
    outsideTemperature()


# calculates RPM and speed
def RPMSpeedCalculation():
    global speed
    if key == CODED :
        if keyCode == UP:
            if speed < 160:
                speed +=0.3
            elif speed == 159.9 or speed > 160: pass

        if keyCode == DOWN:
            if speed != 0:
                speed -= 0.5
            else: pass
    if speed == 0 or None:
        return 900
    # RPM = speed * transmission Ratio of the gear * rear end ration * 336 / tire size
    if speed<20: # gear 1
        return floor((speed * transmissionRatios[0] * rearEndRatio * constant)/ tireSize)
    if speed >20 and speed <45: # gear 2
        return floor((speed * transmissionRatios[1] * rearEndRatio * constant)/ tireSize)
    if speed >45 and speed <60:# gear 3
        return floor((speed * transmissionRatios[2] * rearEndRatio * constant)/ tireSize)
    if speed >60 and speed <100: # gear 4
        return floor((speed * transmissionRatios[3] * rearEndRatio * constant)/ tireSize)
    if speed >100 and speed < 161: # gear 5
        return floor((speed * transmissionRatios[4] * rearEndRatio * constant)/ tireSize)
    else: return 1500

# displays speed
def speedDisplay(speed):
    x = 400
    y = 200
    if speed > 9:
        x -= 50
    if speed > 99:
        x -= 50
    speed = str(speed)
    SpeedFont = loadFont("Verdana-BoldItalic-200.vlw")
    textFont(SpeedFont, 200)
    fill(8, 125, 231)
    text(speed, x, y)


# calculates the total distance using the formula
def calculateDistance(totalTime, RPM, moving):
    if moving:
        distance = ((PI * tireSize * totalTime * RPM)/(63360* 60000)) # 63360 to convert inches to miles 60000 to convert milli seconds to hours
        # print(distance)
        return ceil(distance)

# displays distance
def displayDistance(distanceDisp):
    trip = 69420
    # print(distanceDisp)
    if distanceDisp == None:
        distanceDisp = 0
    tripFont = loadFont("OCRAExtended-50.vlw")
    textFont(tripFont, 50)
    trip += distanceDisp
    trip = str(trip)
    fill(230, 230, 230)
    text(trip, 400, 250)

def displayRPM(RPM):
    redRPM = 19
    greenRPM = 19
    blueRPM = 19
    strokeValue = "#131313"

    # display the colors Green, Yellow and Red according to the RPM value
    if RPM == None:
        RPM = 900
    if RPM < 1500:
        redRPM = 61
        greenRPM = 171
        blueRPM = 50
        strokeValue = "#3dab32"
    if RPM > 1500 and RPM < 3000:
        redRPM = 219
        greenRPM = 206
        blueRPM = 50
        strokeValue = "#dbce32"
    if RPM > 3000:
        redRPM = 219
        greenRPM = 76
        blueRPM = 50
        strokeValue = "#db4c32"

    RPMmapped = map(RPM, 900, 9000, 50, 500) # mapping the values to create a RPM simulator

    stroke(strokeValue)
    strokeWeight(5)
    noFill()
    rect(230, 265, 500, 65)
    fill(redRPM, greenRPM, blueRPM)

    rect(230, 265, RPMmapped, 65)
    RPMFont = loadFont("Castellar-50.vlw")
    textFont(RPMFont, 50)
    fill(255)
    RPMText = "RPM: " + str(RPM)
    text(RPMText, 365, 315)
    noStroke()


# calculate the fuel 
def fuel(distance):
    fuel = 0
    fuelImage = loadImage("petrolSymbol.png")
    if distance == None:
        distance = 0
    elif distance % 3 == 0 :
        if fuel != 300:
            fuel +=100
        else: fuel = 300
    redFuel = 50
    greenFuel = 170
    blueFuel = 50
    strokeValue = "#FFFFFF"

    # display the colors Green, Yellow and Red according to the fuel value
    if fuel > 0 and fuel < 100:
        redFuel = 61
        greeFuel = 171
        blueFuel = 50
        strokeValue = "#3dab32"
    if fuel > 100 and RPM < 200:
        redFuel = 219
        greenFuel = 206
        blueFuel = 50
        strokeValue = "#dbce32"
    if fuel > 200:
        redFuel = 219
        greenFuel = 76
        blueFuel = 50
        strokeValue = "#db4c32"

    # fuelMapped = map(fuel, 0, 50, 10, 500) # mapping the values to create a RPM simulator
    rotate(PI)
    stroke(strokeValue)
    strokeWeight(5)
    noFill()
    rect(-150, -350, 60, 300)
    fill(redFuel, greenFuel, blueFuel)

    rect(-150, -350, 60, 300-fuel)
    rotate(PI)
    image(fuelImage, 100, 300, 50, 50)
    noStroke()
    fill(255)
    triangle(70, 70, 90, 50, 90, 90)
    # RPMFont = loadFont("Castellar-50.vlw")
    # textFont(RPMFont, 50)
    # fill(255)
    # RPMText = "uel: " + str(fuel) + " | "+ str(distance)
    # text(RPMText, 300, 600)

# turn signals
def turnSignals():
    # translate(500, 250)
    leftArrow = loadImage("leftYellow.png")
    rightArrow = loadImage("rightYellow.png")
    leftArrowLight = loadImage("lightLeft.png")
    rightArrowLight = loadImage("lightRight.png")
    lPressed = False
    rPressed = False
    hazardPressed = False
    while keyPressed:
        if key == "l" or key == "L":
            lPressed = True
        if key =="r" or key == "R":
            rPressed = True
        if key == 'h' or key == 'H':
            hazardPressed = True
        

        if lPressed:
            print(lPressed)
            image(leftArrow, 250, 400, 100, 50)
            # lpressed = False

        if rPressed:
            image(rightArrow, 600, 400, 100, 50)
            # rPressed = False
        if hazardPressed:
            image(leftArrow, 250, 400, 100, 50)
            image(rightArrow, 600, 400, 100, 50)
        break

# warning signs 
def warningSigns():

    # load images
    carDoorWarning = loadImage("carDoorWarning.jpg")
    bonnetWarning = loadImage("bonnetWarning.jpg")
    checkEngine = loadImage("checkEngine.PNG")
    lowBeam = loadImage("lowBeam.jpg")
    fuelWarning = loadImage("fuel.jpg")
    lowBattery = loadImage("lowBattery.PNG")
    highBeam = loadImage("highBeam.jpg")

    # Bools
    CarDoorWarningBool = False
    bonnetWarningBool = False
    checkEngineBool = False
    beamBool = True
    fuelWarningBool = False
    lowBatteryBool = False
    
    stroke("#FFFFFF")
    strokeWeight(3)
    noFill()
    rect(850, 45, 65, 310)

    # Check if keys pressed
    if keyPressed:
        if key == '1':
            CarDoorWarningBool = 1
        if key == '2':
            bonnetWarningBool = 1
        if key == '3':
            checkEngineBool = 1
        if key == '4':
            beamBool = 0
        if key == '5':
            fuelWarningBool = 1
        if key == '6':
            lowBatteryBool = 1

    # car door warning
    if CarDoorWarningBool == 1:
        print(CarDoorWarningBool)
        image(carDoorWarning, 860, 50, 50, 50)
    # bonnet warning
    if bonnetWarningBool == 1:
        print(bonnetWarningBool)
        image(bonnetWarning, 860, 100, 50, 50);
    #check engine warning
    if checkEngineBool == 1:
        image(checkEngine, 860, 150, 50, 50)
    if beamBool == 1:
        image(lowBeam, 860, 200, 50, 50)
    elif beamBool == 0:
        image(highBeam, 860, 200, 50, 50)
    if fuelWarningBool == 1:
        image(fuelWarning, 860, 250, 40, 40)
    if lowBatteryBool == 1:
        image(lowBattery, 860, 300, 50, 50)
        
def engineTemperature():
    eT = loadImage("engineTemperature.jpg")
    strokeWeight(1)
    stroke(255)
    noFill()
    rect(190, 150, 100, 60)
    fill(255)
    textSize(50)
    text("M", 250, 195)
    image(eT, 195, 155, 50, 50)
def outsideTemperature():
    
    # degree = 'u\00B0'.decode("utf-8", "replace")
    textSize(65)
    text('69F', 710, 210)
    
    
