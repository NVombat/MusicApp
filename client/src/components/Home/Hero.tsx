import { useState } from 'react';

import logo from '../../utils/images/jvt-logo.jpg';
import group from '../../utils/images/group.jpg';
import { EnglishSong } from './index';

const Hero = () => {
  const [englishSong, setEnglishSong] = useState<boolean>(true);

  return (
    <div>
      <figure className="w-96 mx-auto mt-4">
        <img src={logo} alt="jvt-logo" />
      </figure>
      <div className="flex flex-col justify-center items-center my-5">
        <h1 className="font-bold text-2xl uppercase py-1">VR1 Movement</h1>
        <h1 className="font-bold text-2xl uppercase py-1">WE ARE ALL ONE</h1>
        <h1 className="font-bold text-2xl uppercase py-1">
          LET US SING, SAY, DANCE AND UNITE THE GLOBE TOGETHER
        </h1>
      </div>
      <div className="flex justify-center items-center font-semibold text-3xl">
        Listen to the song
      </div>
      {englishSong ? <EnglishSong /> : ''}
      <figure className="flex justify-center py-5">
        <img src={group} alt="group of people" />
      </figure>
    </div>
  );
};

export default Hero;
