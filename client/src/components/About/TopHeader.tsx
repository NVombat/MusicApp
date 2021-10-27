import AboutUsIcon from '../../utils/images/aboutus';

const TopHeader = () => {
  return (
    <div>
      <div className="flex justify-center items-center py-10 bg-gradient-to-r from-green-400 to-blue-500 text-3xl font-bold text-white">
        About Us
      </div>
      <div className="flex justify-between items-center mx-36">
        <div className="mx-4">
          <div className="my-4 text-3xl font-bold">What is the VR1 Music App about</div>
          <div>
            We aim to come together to show solidarity towards the fact that even
            with our differences, we are all one and alike. We should support
            one another and accept every individual for who they are. It is our
            aim to unite the globe through the power of music and celebrate that
            we are indeed all one
          </div>
          <div className="py-4">
            VR1 Music App is a Karaoke App where you can register yourself
            and then sing the song along with the karaoke track. You can also upload
            the recorded audio or video for the rest of the people to view
          </div>
          <div className="py-1">
            We encourage everyone to go record and upload the files
            as well as go, check out and appreciate other peoples recordings.
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
