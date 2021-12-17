import { useState } from 'react';
import { English, Hindi, Malyalam, Tamil } from './Songs/index';

const Video = () => {
  const [english, setEnglish] = useState<boolean>(true);
  const [hindi, setHindi] = useState<boolean>(false);
  const [tamil, setTamil] = useState<boolean>(false);
  const [malyalam, setMalyalam] = useState<boolean>(false);

  const englishChangeHandler = () => {
    setEnglish(true);
    setHindi(false);
    setMalyalam(false);
    setTamil(false);
  };
  const hindiChangeHandler = () => {
    setEnglish(false);
    setHindi(true);
    setMalyalam(false);
    setTamil(false);
  };
  const tamilChangeHandler = () => {
    setEnglish(false);
    setHindi(false);
    setMalyalam(false);
    setTamil(true);
  };
  const malyalamChangeHandler = () => {
    setEnglish(false);
    setHindi(false);
    setMalyalam(true);
    setTamil(false);
  };

  return (
    <div className="flex flex-col justify-center items-center my-3">
      <h1 className="mb-2 font-semibold ">
        If recording with earphones please play the music in the background so
        it can be recorded as well.
      </h1>

      {english ? (
        <English />
      ) : hindi ? (
        <Hindi />
      ) : tamil ? (
        <Tamil />
      ) : malyalam ? (
        <Malyalam />
      ) : (
        'OOPS! Something went wrong here!'
      )}

      <h3 className="mt-5">Record in More Languages</h3>

      <div className="flex">
        <button
          className="mx-2 mt-5 bg-blue-400 focus:outline-none text-white px-2 py-1 rounded-lg"
          onClick={englishChangeHandler}
        >
          English
        </button>
        <button
          className="mx-2 mt-5 bg-blue-400 focus:outline-none text-white px-2 py-1 rounded-lg"
          onClick={hindiChangeHandler}
        >
          Hindi
        </button>
        <button
          className="mx-2 mt-5 bg-blue-400 focus:outline-none text-white px-2 py-1 rounded-lg"
          onClick={tamilChangeHandler}
        >
          Tamil
        </button>
        <button
          className="mx-2 mt-5 bg-blue-400 focus:outline-none text-white px-2 py-1 rounded-lg"
          onClick={malyalamChangeHandler}
        >
          Malyalam
        </button>
      </div>
    </div>
  );
};

export default Video;
