%% Detecting Lanes
%% Load Camera/Sensor Configuration and Sensor Recording
close all
clear 
clc

% Define Camera Configuration
vidReader = VideoReader('joyride2.mp4');
focalLength    = [1260 1400]; 
principalPoint = [640 220]; 
imageSize      = [600 640];
height = 1.45;
pitch = 1.25;
roll = 0.15;

% vidReader = VideoReader('caltech_cordova1.avi');
% focalLength    = [309.4362, 344.2161]; % [fx, fy] in pixel units
% principalPoint = [318.9034, 257.5352]; % [cx, cy] optical center in pixel coordinates
% imageSize      = [480, 640];           % [nrows, mcols]
% height = 2.1798;    % mounting height in meters from the ground
% pitch  = 14;        % pitch of the camera in degrees
% roll = 0;

camIntr = cameraIntrinsics(focalLength,principalPoint,imageSize);

mCam = monoCamera(camIntr,height,'Pitch',pitch,'Roll',roll);

%% Load Test Video
% Get sample frame
timeStep = 1;                   % time from the beginning of the video
vidReader.CurrentTime = timeStep;   % point to the chosen frame
frame = readFrame(vidReader); % read frame at timeStamp seconds
% Display frame
figure;
imshow(frame);

%% Perform Bird's Eyeview Transform
% Using vehicle coordinates, define area to transform
distAheadOfSensor = 30; % in meters, as previously specified in monoCamera height input
spaceToOneSide    = 6;  % all other distance quantities are also in meters
bottomOffset      = 3;

outView   = [bottomOffset, distAheadOfSensor, -spaceToOneSide, spaceToOneSide]; % [xmin, xmax, ymin, ymax]
imageSize = [NaN, 250]; % output image width in pixels; height is chosen automatically to preserve units per pixel ratio

birdsEyeConfig = birdsEyeView(mCam, outView, imageSize);

birdsEyeImage = transformImage(birdsEyeConfig, frame);
figure;
imshow(birdsEyeImage);

%% Find lane markers in vehicle coordinates
%% Convert to grayscale

birdsEyeImage = rgb2gray(birdsEyeImage);

%% Lane marker segmentation ROI in world units
vehicleROI = outView - [-1, 2, -3, 3]; % look 3 meters to left and right, and 4 meters ahead of the sensor
approxLaneMarkerWidthVehicle = 0.25; % 25 centimeters

%% Detect lane features
laneSensitivity = 0.25;
birdsEyeViewBW = segmentLaneMarkerRidge...
    (birdsEyeImage, birdsEyeConfig, approxLaneMarkerWidthVehicle,...
    'ROI', vehicleROI, 'Sensitivity', laneSensitivity);

figure
imshow(birdsEyeViewBW)

%% Obtain lane candidate points in vehicle coordinates and fit lanes
[imageX, imageY] = find(birdsEyeViewBW);
xyBoundaryPoints = imageToVehicle(birdsEyeConfig, [imageY, imageX]);

maxLanes      = 2; % look for maximum of two lane markers
boundaryWidth = 3*approxLaneMarkerWidthVehicle; % expand boundary width to search for double markers

boundaries = findParabolicLaneBoundaries...
    (xyBoundaryPoints,boundaryWidth,'MaxNumBoundaries', maxLanes);

%% Find candidate ego boundaries
xOffset    = 0;   %  0 meters from the sensor
distanceToBoundaries  = boundaries.computeBoundaryModel(xOffset);
rightEgoBoundary = boundaries(distanceToBoundaries < xOffset);
leftEgoBoundary = boundaries(distanceToBoundaries > xOffset);
%% Show lanes
xVehiclePoints = bottomOffset:distAheadOfSensor;
birdsEyeWithEgoLane = insertLaneBoundary...
    (birdsEyeImage, leftEgoBoundary , birdsEyeConfig,...
    xVehiclePoints, 'Color','Red');
birdsEyeWithEgoLane = insertLaneBoundary...
    (birdsEyeWithEgoLane, rightEgoBoundary, birdsEyeConfig,...
    xVehiclePoints, 'Color','Green');

frameWithEgoLane = insertLaneBoundary...
    (frame, leftEgoBoundary, mCam, xVehiclePoints, 'Color','Red');
frameWithEgoLane = insertLaneBoundary...
    (frameWithEgoLane, rightEgoBoundary, mCam, xVehiclePoints, 'Color','Green');

figure
subplot('Position', [0, 0, 0.5, 1.0]) % [left, bottom, width, height] in normalized units
imshow(birdsEyeWithEgoLane)
subplot('Position', [0.5, 0, 0.5, 1.0])
imshow(frameWithEgoLane)

%% Loop Data and Video
timeStep = 0;
vidReader.CurrentTime = 0;
framePlayer = vision.DeployableVideoPlayer;
birdsEyePlayer = vision.DeployableVideoPlayer;
load groundTruthLanes.mat
idx = 0;

while(hasFrame(vidReader))
    
    idx = idx + 1;
    % Get frame 
    frame = readFrame(vidReader);
    
    % Perform Bird's Eyeview Transform
    birdsEyeImage = transformImage(birdsEyeConfig, frame);
    
    % Convert to grayscale
    birdsEyeImage = rgb2gray(birdsEyeImage);

    % Detect lane features
    birdsEyeViewBW = segmentLaneMarkerRidge...
        (birdsEyeImage, birdsEyeConfig, approxLaneMarkerWidthVehicle,...
        'ROI', vehicleROI, 'Sensitivity', laneSensitivity);
    
    % Obtain lane candidate points in vehicle coordinates
    [imageX, imageY] = find(birdsEyeViewBW);
    xyBoundaryPoints = imageToVehicle(birdsEyeConfig, [imageY, imageX]);
    
    boundaries = findParabolicLaneBoundaries...
        (xyBoundaryPoints,boundaryWidth,'MaxNumBoundaries', maxLanes);
    
    % Find candidate ego boundaries
    xOffset    = 0;   %  0 meters from the sensor
    distanceToBoundaries  = boundaries.computeBoundaryModel(xOffset);
    rightEgoBoundary = boundaries(distanceToBoundaries < xOffset);
    leftEgoBoundary = boundaries(distanceToBoundaries > xOffset);

    % Show lanes
    birdsEyeWithEgoLane = insertLaneBoundary...
        (birdsEyeImage, leftEgoBoundary , birdsEyeConfig,...
        xVehiclePoints, 'Color','Red');
    birdsEyeWithEgoLane = insertLaneBoundary...
        (birdsEyeWithEgoLane, rightEgoBoundary, birdsEyeConfig,...
        xVehiclePoints, 'Color','Green');

    frameWithEgoLane = insertLaneBoundary...
        (frame, leftEgoBoundary, mCam, xVehiclePoints, 'Color','Red');
    frameWithEgoLane = insertLaneBoundary...
        (frameWithEgoLane, rightEgoBoundary, mCam, xVehiclePoints, 'Color','Green');

    % Display frame
    framePlayer(frameWithEgoLane);
    birdsEyePlayer(birdsEyeWithEgoLane);
    
    pause(0.05);
    
    laneResults.Boundaries{idx} = [leftEgoBoundary rightEgoBoundary];
    
    gTruthFrame = gTruth.LabelData.lanes{idx};
    
    for jdx = 1:numel(gTruthFrame)
        gTruthVCoord{jdx} = imageToVehicle(mCam, gTruthFrame{jdx});
    end
    
    laneResults.GroundTruth{idx} = gTruthVCoord;  
    
end

%% Evalutate detections against ground truth
threshold = 0.1;
[numMatches, numMisses, numFP] = evaluateLaneBoundaries(laneResults.Boundaries,...
    laneResults.GroundTruth,threshold)
