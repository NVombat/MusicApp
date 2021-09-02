import { Link } from 'react-router-dom';
const Hero = () => {
  return (
    <div>
      <p>yoyo</p>
      <Link className="bg-red-400 text-4xl" to="/resetpassword">
        <span>click here</span>
      </Link>
    </div>
  );
};

export default Hero;
