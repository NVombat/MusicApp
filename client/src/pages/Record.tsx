import Video from '../components/Record/Video';
import RecordAudio from '../components/Record/Record';
const Record = () => {
  return (
    <div className="flex flex-col justify-center items-center mt-10">
      <div className="mb-5">We are one Song</div>
      <Video />
      <RecordAudio />
    </div>
  );
};

export default Record;
