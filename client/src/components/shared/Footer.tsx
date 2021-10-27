import jvtlogo from '../../utils/images/jvt-logo.jpg';
const Footer = () => {
  return (
    <>
      <div className="bg-linear-pink-invert">
        <div className="mx-auto container pt-20 lg:pt-10 flex flex-col items-center justify-center">
          <div>
            <img src={jvtlogo} alt="logo" height="300" width="300" />
          </div>
          <div className="text-black flex flex-col md:items-center f-f-l pt-3">
            <div className="my-6 text-base text-color f-f-l">
              <ul className="md:flex items-center">
                <li className=" md:mr-6 cursor-pointer pt-4 lg:py-0">Home</li>
                <li className=" md:mr-6 cursor-pointer pt-4 lg:py-0">About</li>
                <li className=" md:mr-6 cursor-pointer pt-4 lg:py-0">Login</li>
                <li className=" md:mr-6 cursor-pointer pt-4 lg:py-0">Posts</li>
              </ul>
            </div>
            <div className="flex-row md:flex justify-center items-center text-sm text-color mb-10 f-f-l">
              <p className="px-4"> Sponsored by JTV Foundation India</p>
              <p className="px-4"> Developed by Shivam Shekhar & Nikhill Vombatkere, Networking & Communications Dept, SRMIST, India</p>
              <p className="px-4"> © 2021 JTV. All rights reserved</p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Footer;
