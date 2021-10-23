import AboutUsIcon from '../../utils/images/aboutus';

const TopHeader = () => {
  return (
    <div>
      <div className="flex justify-center items-center py-10 bg-gradient-to-r from-green-400 to-blue-500 text-3xl font-bold text-white">
        About Us
      </div>
      <div className="flex justify-between items-center mx-36">
        <div className="mx-4">
          <div className="my-4 text-xl font-bold">What is VR1 Music App</div>
          <div>
            VR1 Music App is a Karaoke App in which you can register yourself
            and then sing the song along with karaoke and also upload it for the
            rest of the people to view it
          </div>
          <div className="py-1">
            We encourage other people as well to go record and upload the files
            as well as appreciate other people's work.
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
