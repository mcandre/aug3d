#!/usr/bin/env python

# aug3d
# Andrew Pennebaker
# 2 March 2012

import SimpleCV
import sys
import os
import time

def main():
    camera = SimpleCV.Camera()

    d = os.path.abspath(os.path.dirname(sys.argv[0])) + os.sep

    haar = d + "haar-eyes.xml"

    shades = SimpleCV.ImageClass.Image(d + "glasses.png")

    while True:
        image = camera.getImage()

        features = image.findHaarFeatures(haar)

        try:
            # features.draw(SimpleCV.Color.GREEN)

            for i in range(len(features)):
                feature = features[i]
                coords = feature.coordinates()

                image.blit(shades, (coords[0], coords[1]), True)
        except:
            pass

        image.show()

        time.sleep(0.05)

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass