import { Link } from 'react-router-dom';
import Layout from './Layout';
const ErrorPage = () => {
  return (
    <Layout>
      <div>
        <div className="flex justify-center items-center text-4xl font-extrabold my-10">
          404
        </div>
        <div className="flex justify-center items-center text-2xl font-semibold my-5">
          Go back to
        </div>
        <Link
          className="bg-blue-400 rounded-lg py-1 px-2 text-white text-xl my-5"
          to="/"
        >
          Home
        </Link>
      </div>
    </Layout>
  );
};

export default ErrorPage;
