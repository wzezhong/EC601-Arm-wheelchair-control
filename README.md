# EC601-Arm-wheelchair-control
EC601 arm wheel control

MATLAB part
In our project, we have finished sprint 2 part. In this part, you can see our code above. We used MATLAB to detect objects. It has two different part for our detection. The first part is using MATLAB code to detect object. In our code, we used MATLAB object detection tools to detect some simple object. When you finish run the ".m" file, you can see our detect target, it is a stop sign. Becuase our project is smart wheelchair, we need to detect handicap sign. In sprint 2, we just achieve some easy function that is why we detect stop sign.

Second, we want to use MATLAB open CV function to give us project some extra function which is lane detection. We want to make our wheelchair automatically drive itself. This function will help people who cannot drive wheelchair in a good way. In this part, we use lane detection function to show two lanes of road and we also add a midline to tell people your wheelchair is driving in a wrong way. At the same time, we add "bird's eye view" function to get a better view direction for our wheelchair.

Third, for using our code, you need to download two ".m" files which is lane detection code and another is object detection. Then you can directly run our code in your computer MATLAB program. You will get some pictures of object detection. And you will get a video of lane detection. In the video, the yellow line is midline. At the right up corner of this video, you will get a small window which is "bird's eye view". This two different view from a same camera.

===================================================================================================================================

Alexa module
In order to test the module, you first need to registrate a developer account for getting access to the Amazon Skill Kit, then copy the code into the JSON file editor, Amazon Skill Kit allows you use AWS Lambda ARN to hold and write your code. So that you don't have to implement any kind of logic code except the interaction module (defined by the JSON file).

After copying the code into the JSON file editor, click "Build Module" and click Endpoint, set your Default Reagion to be arn:aws:lambda:us-east-1:448610050284:function:aws-serverless-repository-alexaskillskitnodejsfact-1SAIXZTQF732N (this code is automatically returned by the AWS Lambda function and is also the place where the code of the whole module is stored and runned).

Our project take advantage of Voice Control feature by letting voice input to actually call the CV module, since that part has not yet finished, the Alexa module shown here is NOT the finnal deliver of our project, instead, it's a simple demo to basically show you the idea how to implement Voice Control into your product. The whole dataset of this module comes from Amazon.com, browse https://developer.amazon.com for more information.

