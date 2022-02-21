import { ReactMediaRecorder } from 'react-media-recorder';
import { Play, Stop } from '../../utils/icons/Index';

const RecordAudio = () => {
  return (
    <div>
      <ReactMediaRecorder
        audio
        render={({ status, startRecording, stopRecording, mediaBlobUrl }) => (
          <div>
            <p className="flex justify-center">Status: {status}</p>
            <div className="flex justify-center items-center my-5">
              <button
                className="flex items-center bg-red-500 text-xl mx-3 px-4 py-1 rounded-xl"
                onClick={startRecording}
              >
                <span className="text-white mr-2">
                  <Play />
                </span>{' '}
                Start
              </button>
              <button
                className="flex items-center bg-red-500 text-xl mx-3 px-4 py-1 rounded-xl"
                onClick={stopRecording}
              >
                <span className="text-white mr-2">
                  <Stop />
                </span>{' '}
                Stop
              </button>
            </div>
            <span className="flex justify-center">
              <audio src={mediaBlobUrl as string} controls />
            </span>
          </div>
        )}
      />
    </div>
  );
};

export default RecordAudio;
