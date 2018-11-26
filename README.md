# EC601-Arm-wheelchair-control
## Attention: If you cannot run our MATLAB code, because you don't have MATLAB openCV part access. Please contact us for demo.

# Sprint2 part
## MATLAB part
In our project, we have finished sprint 2 part. In this part, you can see our different part code above. First part we used MATLAB to detect objects. It has two different part for our detection. The first is using MATLAB code to detect object. In our code, we used MATLAB object detection tools to detect some simple objects. When you finish run the "object_detect.m" file, you can see our detect target, it is a stop sign. Becuase our project is smart wheelchair, we need to detect handicap sign. In sprint 2, we just achieve some easy function that is why we detect stop sign.

Second, we want to use MATLAB open CV function to give our project some extra functions which is lane detection. We want to make our wheelchair automatically drive itself. This function will help people who cannot drive wheelchair in a good way. In this part, we use lane detection function to show two lanes of road and we also add a midline to tell people your wheelchair is driving in a wrong way. At the same time, we add "bird's eye view" function to get a better view direction for our wheelchair.

Third, for using our code, you need to download two "lane_detect.m" files. You need our video to achieve our results which we showed in sprint 2 slides. You can email me to get this video. Or you can use any video to replace our video to test our code. Then you can directly run our code in your computer MATLAB program. You will get some pictures of object detection. And you will get a video of lane detection. In the video, the yellow line is midline. At the right up corner of this video, you will get a small window which is "bird's eye view". This two different view from a same camera.

=================================================================================

## Alexa module

In order to test the module, you first need to registrate a developer account for getting access to the Amazon Skill Kit, then copy the code into the JSON file editor, Amazon Skill Kit allows you use AWS Lambda ARN to hold and write your code. So that you don't have to implement any kind of logic code except the interaction module (defined by the JSON file).

After copying the code into the JSON file editor, click "Build Module" and click Endpoint, set your Default Reagion to be arn:aws:lambda:us-east-1:448610050284:function:aws-serverless-repository-alexaskillskitnodejsfact-1SAIXZTQF732N (this code is automatically returned by the AWS Lambda function and is also the place where the code of the whole module is stored and runned).

Our project take advantage of Voice Control feature by letting voice input to actually call the CV module, since that part has not yet finished, the Alexa module shown here is NOT the finnal deliver of our project, instead, it's a simple demo to basically show you the idea how to implement Voice Control into your product. The whole dataset of this module comes from Amazon.com, browse https://developer.amazon.com for more information.

=================================================================================
# Sprint 3 part
## Button Recognition:
One of the most important tasks of pressing an elevator button is to identify buttons and recognise the numbers. We achieved this using openCV and pytesseract. 
1. The file buttonrecognition.py contains the python code for button and number recognition. The image to be tested is passed as an argument.
2. The above code was tested on three images : button.jpg and el.jpg are images obtained from the internet, lift.jpg is an acutal elevator images clicked for testing.
3. In order to use the code, download buttonrecognition.py and install pytesseract. Pass the image to be tested as an argument. The image after button and number recognition is saved as result.png with marked areas.

## MATLAB Recognition:
In the MATLAB folder, I create the sprint3 folder. It include the recognition file and a picture which you will need to use. You need to make sure the file and picture in same path. If you cannot run this MATLAB code, you need more MATLAB access for your MATLAB program. Please free to contact us if you want to review our results.


# Sprint 4 part
## Solidwork Robot Arm design
In the sprint4 folder, you will find all of files about the arm design. Because these are solidwork files, you need download solidwork programs. I got some screenshots for you conconvenient. And there is a video folder which can show you how our arm work. You can just download the video .zip file to watch our resutlts.


