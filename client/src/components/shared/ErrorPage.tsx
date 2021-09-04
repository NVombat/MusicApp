import { Link } from 'react-router-dom';
const ErrorPage = () => {
  return (
    <div>
      <div className="flex justify-center items-center text-4xl font-extrabold my-10">
        404
      </div>
      <div className="flex justify-center items-center text-2xl font-semibold my-5">
        Go back to
      </div>
      <div className="flex justify-center">
        <Link
          className="bg-blue-400 rounded-lg py-1 px-2 text-white text-xl my-5"
          to="/"
        >
          Home
        </Link>
      </div>
    </div>
  );
};

export default ErrorPage;
