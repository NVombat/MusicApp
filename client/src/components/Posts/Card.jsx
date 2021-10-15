const Card = (props) => {
  return (
    <div className="flex items-center border-2 border-black px-5 py-3 my-2">
      <a href={props.link}>
        <div className="px-2 text-3xl">{props.downloadIcon}</div>
      </a>
      <div className="text-xl font-semibold px-2">{props.name}</div>
      <div className="text-xl font-semibold">({props.filename})</div>
    </div>
  );
};

export default Card;
