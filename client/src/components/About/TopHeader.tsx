import AboutUsIcon from '../../utils/images/aboutus';

const TopHeader = () => {
  return (
    <div>
      <div className="flex justify-center items-center py-10 bg-gradient-to-r from-green-400 to-blue-500 text-3xl font-bold text-white">
        About Us
      </div>
      <div className="flex justify-between items-center mx-36">
        <div className="mx-4">
          <div className="my-4 text-xl font-bold">
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Repellendus, eaque?
          </div>
          <div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Repellendus, eaque? Itaque deleniti et provident molestias officia
            eos rem magnam commodi hic praesentium, fugiat eaque, est nemo
            maxime saepe sint! Tempore?
          </div>
          <div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Repellendus, eaque? Itaque deleniti et provident molestias officia
            eos rem magnam commodi hic praesentium, fugiat eaque, est nemo
            maxime saepe sint! Tempore?
          </div>
        </div>
        <div className="mx-4">
          <AboutUsIcon />
        </div>
      </div>
    </div>
  );
};

export default TopHeader;
