imgFiles = dir('*.png') ; 
N = length(imgFiles) ; 
% create the video writer with 1 fps
writerObj = VideoWriter('myVideo.avi');
writerObj.FrameRate= 10;
% open the video writer
open(writerObj);
% write the frames to the video
for i=1:N
    img = imgFiles(i).name ; 
    I = imread(img) ; 
    imshow(I) ; 
    F = getframe(gcf) ;
    writeVideo(writerObj, F);
end
% close the writer object
close(writerObj);