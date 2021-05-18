#The scripts plots pseudocolor plot with specific formatting
#OPTIONAL: plotting fixed contours in the background 

#---------------------------------------------------------------------------------------------------
# To run this script, use following command
# visit -cli -nowin -s scriptname.py <database_filename_with_path> <variable_name_in_visit_file>'


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

from visit_utils import *
import sys

#--------------------------------------------------------------------------------------------------------


def user_db():
    OpenDatabase(database, 0)
    AddPlot("Pseudocolor", variable)
    DrawPlots()
    print("Psuedocolor plot success")
#input for whether to plot contours
    user_response = raw_input("Also want to plot contours in background? y/n ")
    if user_response=='y':
        print("Enter locations for contour separated by comma")
        locations=input()
        #cvalue=locations.sp

        AddPlot("Contour", "psi_norm", 1, 1)
        SetPlotFollowsTime(0)
	## Contour attributes
        ContourAtts = ContourAttributes()
        ContourAtts.changedColors = ()
        ContourAtts.legendFlag = 0
        ContourAtts.lineWidth = 2
        ContourAtts.colorType = ContourAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable             
    	ContourAtts.singleColor = (0, 0, 0, 255)
    	ContourAtts.contourValue =locations
    	ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
    	ContourAtts.min = 0
    	ContourAtts.max = 1
    	ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
    	ContourAtts.wireframe = 0
    	SetPlotOptions(ContourAtts)
    	DrawPlots()
        print("Contour plot success")


    #print(contourValue)
    elif user_response=='n':
        print("NO contours will be plotted")
    else:
        print("Invalid input")

##2D Attributes: window coordinates and and plot coordinates
    
    View2DAtts = View2DAttributes()
    #View2DAtts.windowCoords = (9, 11, -0.999999, 0.999999)
    View2DAtts.viewportCoords = (0.14, 0.7, 0.15, 0.94)
    View2DAtts.fullFrameActivationMode = View2DAtts.Auto # On, Off, Auto
    View2DAtts.fullFrameAutoThreshold = 100
    View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.windowValid = 1
    SetView2D(View2DAtts)
    RecenterView()

## Annotation attributes
    AnnotationAtts = AnnotationAttributes()
    AnnotationAtts.axes2D.visible = 1
    AnnotationAtts.axes2D.autoSetTicks = 1
    AnnotationAtts.axes2D.autoSetScaling = 0
    AnnotationAtts.axes2D.lineWidth = 1
    AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Inside  # Inside, Outside, Both
    AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
    AnnotationAtts.axes2D.xAxis.title.visible = 1
    AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Times  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.title.font.scale = 1.25
    AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.title.font.bold = 1
    AnnotationAtts.axes2D.xAxis.title.font.italic = 1
    AnnotationAtts.axes2D.xAxis.title.userTitle = 1
    AnnotationAtts.axes2D.xAxis.title.userUnits = 1
    AnnotationAtts.axes2D.xAxis.title.title = "R"
    AnnotationAtts.axes2D.xAxis.title.units = "m"
    AnnotationAtts.axes2D.xAxis.label.visible = 1
    AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Times  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.label.font.scale = 1.25
    AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.label.font.bold = 1
    AnnotationAtts.axes2D.xAxis.label.font.italic = 1
    AnnotationAtts.axes2D.xAxis.label.scaling = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1

    AnnotationAtts.axes2D.yAxis.title.visible = 1
    AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Times  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.title.font.scale = 1.25
    AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.title.font.bold = 1
    AnnotationAtts.axes2D.yAxis.title.font.italic = 1
    AnnotationAtts.axes2D.yAxis.title.userTitle = 1
    AnnotationAtts.axes2D.yAxis.title.userUnits = 1
    AnnotationAtts.axes2D.yAxis.title.title = "Z"
    AnnotationAtts.axes2D.yAxis.title.units = "m"
    AnnotationAtts.axes2D.yAxis.label.visible = 1
    AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Times  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.label.font.scale = 1.25
    AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.label.font.bold = 1
    AnnotationAtts.axes2D.yAxis.label.font.italic = 1
    AnnotationAtts.axes2D.yAxis.label.scaling = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.timeInfoFlag = 1
    AnnotationAtts.legendInfoFlag = 1
    AnnotationAtts.databaseInfoFlag =0
    SetAnnotationAttributes(AnnotationAtts)

# Legend attributes
    legend = GetAnnotationObject(GetPlotList().GetPlots(0).plotName)
    legend.managePosition = 0
    legend.position = (0.62, 0.96)
    legend.fontFamily = 2  # Arial, Courier, Times
    legend.fontBold = 0
    legend.drawBoundingBox = 0
    legend.numberFormat = "%# -9.4g"
    legend.drawLabels = 1 # None, Values, Labels, Both
    legend.fontHeight = 0.05
    legend.xScale = 0.5
    legend.yScale = 3.1
    legend.drawTitle = 1
    legend.drawMinMax = 0
    legend.orientation = 0  # VerticalRight, VerticalLeft, HorizontalTop, HorizontalBottom
    legend.controlTicks = 1
    legend.numTicks = 5          # set number of ticks
    legend.minMaxInclusive = 1

# Save images of all timesteps and add each image filename to a list.
    names = []
    slider = CreateAnnotationObject("TimeSlider")
    title = CreateAnnotationObject("Text2D")
    slider.visible = 0
    for state in range(TimeSliderGetNStates()):
        SetTimeSliderState(state)
        SaveWindowAtts = SaveWindowAttributes()
        SaveWindowAtts.outputToCurrentDirectory = 1
        SaveWindowAtts.outputDirectory = "."
        #SaveWindowAtts.fileName = "visit1"
        #SaveWindowAtts.title = "time =$time"
        #figure title

        Query("Time")
        t=float(GetQueryOutputValue())
        time1=t*(2.97*10**(-4))       #time in milli-seconds
        time2=format(time1, '5f')
        string="t="+str.format(str(time2))
        title.visible = 1
        title.position = (0.3, 0.95)
        title.height = 0.02
        title.textColor = (0, 0, 0, 255)
        title.text = string
        title.fontFamily = 2  # Arial, Courier, Times
        title.fontBold = 1
        title.fontItalic = 1
    	SaveWindowAtts.family = 1
    	SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
    	SaveWindowAtts.width = 1024
    	SaveWindowAtts.height = 420
    	SaveWindowAtts.screenCapture = 0
    	SaveWindowAtts.quality = 90
    	SaveWindowAtts.opts.types = ()
    	SaveWindowAtts.opts.help = ""
    	SetSaveWindowAttributes(SaveWindowAtts)
    	SaveWindow()

###=================================================================================================
#Main Program

arguments = sys.argv[1:]
count = len(arguments)
if count != 2 :
    print "Please specify database filename and variable name"
    print "Usage: visit -cli -nowin -s scriptname.py <database_filename_with_path>  <variable_name_in_visit_files> "
    sys.exit(1)
database= sys.argv[1]   #"../omg.xdmf"
variable = sys.argv[2]   #"Vorticity"
print "database is located at : ", database
print "variable chosen for plotting : ", variable
user_db()
exit()



