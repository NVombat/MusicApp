import { ReactMediaRecorder } from 'react-media-recorder';

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
                className="bg-blue-400 text-xl mx-3 px-2 py-1 rounded-xl"
                onClick={startRecording}
              >
                ▶ Start Recording
              </button>
              <button
                className="bg-blue-400 text-xl mx-3 px-2 py-1 rounded-xl"
                onClick={stopRecording}
              >
                ⏹ Stop Recording
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
