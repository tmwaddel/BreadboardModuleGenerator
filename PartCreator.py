totalPins = 30 # Minimum 4 pins (2x2)
moduleWidth = 16 # Tenths of an inch

for pinCount in range(4, totalPins+1, 2):
	drillSize = 0.75

	numPad = pinCount
	footprintOffset = 0
	pinOffset = 0

	if (numPad/2) % 2 == 0:
		footprintOffset = 1.27
		pinOffset = 1

	outlineHeightMM = round((2.54 * (int(numPad/2) + round(numPad/4 - numPad/2, 0))) - footprintOffset + 1.27, 2)

	partName = "PINS2X" + str(int(numPad/2))
	fileName = "Breadboard_Module_2x" + str(int(numPad/2)) + ".lbr"

	newLibrary = open(fileName, 'w')

	newLibrary.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
	newLibrary.write("<!DOCTYPE eagle\n")
	newLibrary.write("SYSTEM 'eagle.dtd'>\n")
	newLibrary.write("<eagle version=\"9.6.2\">\n")
	newLibrary.write("<drawing>\n")
	newLibrary.write("<settings>\n")
	newLibrary.write("<setting alwaysvectorfont=\"no\"/>\n")
	newLibrary.write("<setting verticaltext=\"up\"/>\n")
	newLibrary.write("</settings>\n")
	newLibrary.write("<grid altdistance=\"0.01\" altunit=\"inch\" altunitdist=\"inch\" display=\"no\" distance=\"0.1\" multiple=\"1\" style=\"lines\" unit=\"inch\" unitdist=\"inch\"/>\n")
	newLibrary.write("<layers>\n")
	newLibrary.write("<layer active=\"yes\" color=\"4\" fill=\"1\" name=\"Top\" number=\"1\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"1\" fill=\"1\" name=\"Bottom\" number=\"16\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"2\" fill=\"1\" name=\"Pads\" number=\"17\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"2\" fill=\"1\" name=\"Vias\" number=\"18\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"6\" fill=\"1\" name=\"Unrouted\" number=\"19\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"24\" fill=\"1\" name=\"Dimension\" number=\"20\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"tPlace\" number=\"21\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"bPlace\" number=\"22\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"15\" fill=\"1\" name=\"tOrigins\" number=\"23\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"15\" fill=\"1\" name=\"bOrigins\" number=\"24\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"tNames\" number=\"25\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"bNames\" number=\"26\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"tValues\" number=\"27\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"bValues\" number=\"28\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"3\" name=\"tStop\" number=\"29\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"6\" name=\"bStop\" number=\"30\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"4\" name=\"tCream\" number=\"31\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"5\" name=\"bCream\" number=\"32\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"6\" fill=\"3\" name=\"tFinish\" number=\"33\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"6\" fill=\"6\" name=\"bFinish\" number=\"34\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"4\" name=\"tGlue\" number=\"35\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"5\" name=\"bGlue\" number=\"36\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"tTest\" number=\"37\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"bTest\" number=\"38\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"4\" fill=\"11\" name=\"tKeepout\" number=\"39\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"1\" fill=\"11\" name=\"bKeepout\" number=\"40\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"4\" fill=\"10\" name=\"tRestrict\" number=\"41\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"1\" fill=\"10\" name=\"bRestrict\" number=\"42\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"2\" fill=\"10\" name=\"vRestrict\" number=\"43\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"Drills\" number=\"44\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"Holes\" number=\"45\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"3\" fill=\"1\" name=\"Milling\" number=\"46\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"Measures\" number=\"47\" visible=\"no\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"Document\" number=\"48\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"Reference\" number=\"49\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"tDocu\" number=\"51\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"bDocu\" number=\"52\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"9\" fill=\"1\" name=\"SimResults\" number=\"88\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"9\" fill=\"1\" name=\"SimProbes\" number=\"89\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"5\" fill=\"1\" name=\"Modules\" number=\"90\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"2\" fill=\"1\" name=\"Nets\" number=\"91\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"1\" fill=\"1\" name=\"Busses\" number=\"92\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"2\" fill=\"1\" name=\"Pins\" number=\"93\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"4\" fill=\"1\" name=\"Symbols\" number=\"94\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"Names\" number=\"95\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"Values\" number=\"96\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"7\" fill=\"1\" name=\"Info\" number=\"97\" visible=\"yes\"/>\n")
	newLibrary.write("<layer active=\"yes\" color=\"6\" fill=\"1\" name=\"Guide\" number=\"98\" visible=\"yes\"/>\n")
	newLibrary.write("</layers>\n")
	newLibrary.write("<library>\n")
	newLibrary.write("<packages>\n")

	for partWidth in range (1, moduleWidth, 1):
		partWidthMM = partWidth * 1.27
		outlineWidthMM = partWidthMM + 1.27
		devName = partName + "_WIDTH" + str(partWidth) + "TENTHS"

		newLibrary.write("<package name=\"" + devName + "\">\n")

		for i in range(1, int(numPad/2) + 1, 1):
			padLocationY = round((2.54 * (i + round(numPad/4 - numPad/2, 0))) - footprintOffset, 2)
			newLibrary.write("<pad drill=\"" + str(drillSize) + "\" name=\"P$" + str(i) + "\" shape=\"octagon\" x=\"" + str(-partWidthMM) + "\" y=\"" + str(-padLocationY) + "\"/>\n")

		for i in range(1, int(numPad/2) + 1, 1):
			padLocationY = round((2.54 * (i + round(numPad/4 - numPad/2, 0))) - footprintOffset, 2)
			newLibrary.write("<pad drill=\"" + str(drillSize) + "\" name=\"P$" + str(i+int(numPad/2)) + "\" shape=\"octagon\" x=\"" + str(partWidthMM) + "\" y=\"" + str(padLocationY) + "\"/>\n")

		newLibrary.write("<wire layer=\"21\" width=\"0.127\" x1=\"" + str(-outlineWidthMM) + "\" x2=\"" + str(-outlineWidthMM) + "\" y1=\"" + str(outlineHeightMM) + "\" y2=\"" + str(-outlineHeightMM) + "\"/>\n")
		newLibrary.write("<wire layer=\"21\" width=\"0.127\" x1=\"" + str(-outlineWidthMM) + "\" x2=\"" + str(outlineWidthMM) + "\" y1=\"" + str(-outlineHeightMM) + "\" y2=\"" + str(-outlineHeightMM) + "\"/>\n")
		newLibrary.write("<wire layer=\"21\" width=\"0.127\" x1=\"" + str(outlineWidthMM) + "\" x2=\"" + str(outlineWidthMM) + "\" y1=\"" + str(-outlineHeightMM) + "\" y2=\"" + str(outlineHeightMM) + "\"/>\n")
		newLibrary.write("<wire layer=\"21\" width=\"0.127\" x1=\"" + str(outlineWidthMM) + "\" x2=\"" + str(-outlineWidthMM) + "\" y1=\"" + str(outlineHeightMM) + "\" y2=\"" + str(outlineHeightMM) + "\"/>\n")

		newLibrary.write("</package>\n")

	newLibrary.write("</packages>\n")

	newLibrary.write("<symbols>\n")
	newLibrary.write("<symbol name=\"" + partName + "\">\n")

	for i in range(1, int(numPad/2) + 1, 1):
		pinLocationY = round((-2.54 * i) + (2.54 * round(numPad/4,0)), 2)
		newLibrary.write("<pin length=\"middle\" name=\"P$" + str(i) + "\" x=\"" + str(-17.78) + "\" y=\"" + str(pinLocationY) + "\"/>\n")

	for i in range(1, int(numPad/2) + 1, 1):
		pinLocationY = round((2.54 * i) - (2.54 * (round(numPad/4,0)+pinOffset)), 2)
		newLibrary.write("<pin length=\"middle\" name=\"P$" + str(i+int(numPad/2)) + "\" rot=\"R180\" x=\"" + str(17.78) + "\" y=\"" + str(pinLocationY) + "\"/>\n")


	wireLocationYMax = round((-2.54 * 1) + (2.54 * round(numPad/4,0)) + 2.54, 2)
	wireLocationYMin = round((2.54 * 1) - (2.54 * (round(numPad/4,0)+pinOffset)) - 2.54, 2)

	newLibrary.write("<wire layer=\"94\" width=\"0.254\" x1=\"" + str(-12.7) + "\" x2=\"" + str(-12.7) + "\" y1=\"" + str(wireLocationYMax) + "\" y2=\"" + str(wireLocationYMin) + "\"/>\n")
	newLibrary.write("<wire layer=\"94\" width=\"0.254\" x1=\"" + str(-12.7) + "\" x2=\"" + str(12.7) + "\" y1=\"" + str(wireLocationYMin) + "\" y2=\"" + str(wireLocationYMin) + "\"/>\n")
	newLibrary.write("<wire layer=\"94\" width=\"0.254\" x1=\"" + str(12.7) + "\" x2=\"" + str(12.7) + "\" y1=\"" + str(wireLocationYMin) + "\" y2=\"" + str(wireLocationYMax) + "\"/>\n")
	newLibrary.write("<wire layer=\"94\" width=\"0.254\" x1=\"" + str(12.7) + "\" x2=\"" + str(-12.7) + "\" y1=\"" + str(wireLocationYMax) + "\" y2=\"" + str(wireLocationYMax) + "\"/>\n")

	newLibrary.write("<text x=\"-12.7\" y=\"" + str(round(wireLocationYMax + 2.54, 2)) + "\" size=\"1.778\" layer=\"95\">&gt;NAME</text>\n")
	newLibrary.write("<text x=\"-12.7\" y=\"" + str(round(wireLocationYMin - 2.54, 2)) + "\" size=\"1.778\" layer=\"96\">&gt;VALUE</text>\n")

	newLibrary.write("</symbol>\n")
	newLibrary.write("</symbols>\n")
	newLibrary.write("<devicesets>\n")

	for partWidth in range (1, moduleWidth, 1): #Tenths of an inch
		partWidthMM = partWidth * 1.27
		outlineWidthMM = partWidthMM + 1.27
		devName = partName + "_WIDTH" + str(partWidth) + "TENTHS"

		newLibrary.write("<deviceset name=\"" + devName + "\">\n")
		newLibrary.write("<gates>\n")
		newLibrary.write("<gate name=\"G$1\" symbol=\"" + partName + "\" x=\"0\" y=\"0\"/>\n")
		newLibrary.write("</gates>\n")
		newLibrary.write("<devices>\n")
		newLibrary.write("<device name=\"\" package=\"" + devName + "\">\n")
		newLibrary.write("<connects>\n")

		for i in range(1, numPad + 1, 1):
			newLibrary.write("<connect gate=\"G$1\" pad=\"P$" + str(i) + "\" pin=\"P$" + str(i) + "\"/>\n")

		newLibrary.write("</connects>\n")

		newLibrary.write("<technologies>\n")
		newLibrary.write("<technology name=\"\"/>\n")
		newLibrary.write("</technologies>\n")
		newLibrary.write("</device>\n")
		newLibrary.write("</devices>\n")
		newLibrary.write("</deviceset>\n")

	newLibrary.write("</devicesets>\n")
	newLibrary.write("</library>\n")
	newLibrary.write("</drawing>\n")
	newLibrary.write("</eagle>\n")

	print("DONE")

	newLibrary.close()
