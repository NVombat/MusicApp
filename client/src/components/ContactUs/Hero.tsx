const Hero = () => {
  return (
    <div className="flex flex-col text-center w-full my-12">
      <h1 className="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">
        Contact Us
      </h1>
      <p className="lg:w-2/3 mx-auto leading-relaxed text-xl">
        Hate forms? Send us an{' '}
        <a href="mailto:jtvfoundation@gmail.com" className="underline">
          email
        </a>{' '}
        instead.
      </p>
    </div>
  );
};

export default Hero;
