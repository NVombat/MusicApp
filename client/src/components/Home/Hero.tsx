import logo from '../../utils/images/jvt-logo.jpg';
const Hero = () => {
  return (
    <div>
      <figure className="w-64 mx-auto mt-4">
        <img src={logo} alt="jvt-logo" />
      </figure>
      <div className="flex flex-col justify-center items-center my-5">
        <h1 className="font-bold text-3xl uppercase">VR1 Movement</h1>
        <h1 className="font-bold text-3xl uppercase">
          LET US SING AND UNITE US ALL
        </h1>
      </div>
    </div>
  );
};

export default Hero;
