import { ReactMediaRecorder } from 'react-media-recorder';
import { Play, Stop } from '../../utils/icons/Index';

const RecordVideo = () => {
  return (
    <div>
      <ReactMediaRecorder
        video
        render={({ status, startRecording, stopRecording, mediaBlobUrl }) => (
          <div>
            <p className="flex justify-center">Status: {status}</p>
            <div className="flex justify-center items-center my-5">
              <button
                className="flex items-center bg-blue-400 text-xl mx-3 px-2 py-1 rounded-xl"
                onClick={startRecording}
              >
                <Play /> Start
              </button>
              <button
                className="flex items-center bg-blue-400 text-xl mx-3 px-2 py-1 rounded-xl"
                onClick={stopRecording}
              >
                <Stop /> Stop
              </button>
            </div>
            <span className="flex justify-center">
              <video src={mediaBlobUrl} controls />
            </span>
          </div>
        )}
      />
    </div>
  );
};

export default RecordVideo;
