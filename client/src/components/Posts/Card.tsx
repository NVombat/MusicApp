import { url } from 'inspector';
import React from 'react';

import ReactPlayer from 'react-player'

interface CardProps {
  link: string;
  downloadIcon: any;
  filename: string;
}

const Card: React.FC<CardProps> = ({
  link,
  downloadIcon,
  filename,
}: CardProps) => {
  return (
    <div className="flex items-center flex-col border-2 border-black px-5 py-1 my-3 w-80 ">
      {/* <a href={link}>
        <div className="px-2 text-3xl">{downloadIcon}</div>
      </a> */}
      
      {/* added react player to preview audio and video files */}
      <ReactPlayer url={link} controls width={300} height={100} light='https://media.istockphoto.com/photos/sound-wave-picture-id1287065554?b=1&k=20&m=1287065554&s=170667a&w=0&h=6JIPYTu98DAXdChKSeu-Td3zv8KyLC3yhu-rWfkDQQc='  />
      

      <div className="text-sm text-center mt-2 font-semibold">{filename}</div>
    </div>
  );
};

export default Card;
