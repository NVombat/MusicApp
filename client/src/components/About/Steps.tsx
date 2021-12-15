import { Arrow } from '../../utils/icons/Index';

const Steps = () => {
  return (
    <div className="my-2">
      <h1 className="flex justify-center items-center text-3xl font-bold">
        Want to record your own track? Do it in 3 simple steps
      </h1>
      <div className="flex flex-col justify-center items-center text-center">
        <ul className="text-xl text-center my-2 font-bold">
          <li className="border-2 my-1 py-2 px-4 rounded-lg bg-blue-400 text-white">
            Go to the record page and Click on record
          </li>
          <Arrow />
          <li className="border-2 my-1 py-2 px-4 rounded-lg bg-blue-400 text-white">
            Download what you recorded
          </li>
          <Arrow />
          <li className="border-2 my-1 py-2 px-4 rounded-lg bg-blue-400 text-white">
            Upload it right there to our posts page
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Steps;
