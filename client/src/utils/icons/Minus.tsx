const Minus = () => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width={36}
      height={36}
      viewBox="0 0 24 24"
      strokeWidth="1.5"
      stroke="#A0AEC0"
      fill="none"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-label="Open"
    >
      <path stroke="none" d="M0 0h24v24H0z" />
      <circle cx={12} cy={12} r={9} />
      <line x1={9} y1={12} x2={15} y2={12} />
      <line x1={12} y1={9} x2={12} y2={15} />
    </svg>
  );
};

export default Minus;
