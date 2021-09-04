import { ReactMediaRecorder } from 'react-media-recorder';

const RecordAudio = () => {
  return (
    <div>
      <ReactMediaRecorder
        audio
        render={({ status, startRecording, stopRecording, mediaBlobUrl }) => (
          <div>
            <p className="flex justify-center">{status}</p>
            <button
              className="bg-gray-300 text-xl mx-3 px-2 py-1 rounded-xl"
              onClick={startRecording}
            >
              ▶ Start Recording
            </button>
            <button
              className="bg-gray-300 text-xl mx-3 px-2 py-1 rounded-xl"
              onClick={stopRecording}
            >
              ⏹ Stop Recording
            </button>
            <span className="flex justify-center">
              <audio src={mediaBlobUrl} controls />
            </span>
          </div>
        )}
      />
    </div>
  );
};

export default RecordAudio;
