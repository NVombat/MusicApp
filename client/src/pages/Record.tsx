import { useState } from 'react';
import {
  Video,
  RecordAudio,
  RecordVideo,
  Upload,
  Hero,
} from '../components/Record/Index';
import { Camera, Mic } from '../utils/icons/Index';

const Record = () => {
  const [recordAudio, setRecordAudio] = useState<boolean>(false);
  const [recordVideo, setRecordVideo] = useState<boolean>(false);
  const [upload, setUpload] = useState<boolean>(false);
  const [showVideo, setShowVideo] = useState<boolean>(true);

  const switchToAudioHandler = () => {
    setUpload(true);
    setRecordAudio(true);
    setRecordVideo(false);
  };

  const switchToVideoHandler = () => {
    setUpload(true);
    setRecordVideo(true);
    setRecordAudio(false);
  };

  const toggleVideoHandler = () => {
    setShowVideo(!showVideo);
  };

  return (
    <div className="flex flex-col justify-center items-center mt-10">
      <Hero />
      <div className="flex my-5">
        <button
          className="flex items-center bg-red-300 px-3 py-1 rounded-xl mx-3"
          onClick={toggleVideoHandler}
        >
          {showVideo ? 'Record Without Background' : 'Record With Background'}
        </button>
      </div>
      {showVideo ? <Video /> : ''}
      <div className="flex my-5">
        <button
          onClick={switchToVideoHandler}
          className="flex items-center bg-red-300 px-3 py-1 rounded-xl mx-3"
        >
          <Mic /> Record Video
        </button>
        <button
          onClick={switchToAudioHandler}
          className="flex items-center bg-red-300 px-3 py-1 rounded-xl mx-3"
        >
          <Camera /> Record Audio
        </button>
      </div>
      {recordAudio && <RecordAudio />}
      {recordVideo && <RecordVideo />}
      {upload && <Upload />}
    </div>
  );
};

export default Record;
