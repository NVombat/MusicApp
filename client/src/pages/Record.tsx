import { useState } from 'react';
import { Video, RecordAudio, RecordVideo } from '../components/Record/Index';
import { Camera, Mic } from '../utils/icons/Index';

const Record = () => {
  const [recordAudio, setRecordAudio] = useState<boolean>(false);
  const [recordVideo, setRecordVideo] = useState<boolean>(false);

  const switchToAudioHandler = () => {
    setRecordAudio(true);
    setRecordVideo(false);
  };

  const switchToVideoHandler = () => {
    setRecordVideo(true);
    setRecordAudio(false);
  };

  return (
    <div className="flex flex-col justify-center items-center mt-10">
      <Video />
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
    </div>
  );
};

export default Record;
