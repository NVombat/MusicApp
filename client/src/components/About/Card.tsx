import { CardProps } from '../../utils/interfaces';

const Card = (props: CardProps) => {
  return (
    <div className="flex lg:flex-row md:flex-col sm:flex-col justify-center content-center mt-8">
      <div className="max-w-sm rounded overflow-hidden shadow-lg mx-2 px-4">
        <img
          src={props.src}
          alt={props.name}
          className="h-72 w-56 rounded-full"
        />
        <h1 className="pt-10 text-center font-bold text-2xl">{props.name}</h1>
        <h1 className="py-2 text-center font-semibold text-xl">
          {props.desgination}
        </h1>
      </div>
    </div>
  );
};

export default Card;
