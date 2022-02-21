import React from 'react';

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
    <div className="flex items-center border-2 border-black px-5 py-3 my-2 w-96">
      <a href={link}>
        <div className="px-2 text-3xl">{downloadIcon}</div>
      </a>
      <div className="text-xl font-semibold">{filename}</div>
    </div>
  );
};

export default Card;
