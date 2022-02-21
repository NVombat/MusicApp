import { useEffect, useState } from 'react';
import axios from 'axios';

import ResetPassword from './ResetPasswordForm';
import UpdateProfile from './UpdateProfile';

const getUserDataURL = `https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=${process.env.REACT_APP_FIREBASE_API_KEY}`;

const Hero = () => {
  const [userData, setUserData] = useState<any>([]);
  const [reset, setReset] = useState<boolean>(false);
  const [update, setUpdate] = useState<boolean>(false);

  useEffect(() => {
    axios
      .post(getUserDataURL, {
        idToken: localStorage.getItem('token'),
      })
      .then((res) => {
        //@ts-ignore
        setUserData(res.data.users);
      })
      .catch((err) => console.log(err));
  }, []);

  const showReset = () => {
    setReset(true);
    setUpdate(false);
  };

  const showUpdate = () => {
    setUpdate(true);
    setReset(false);
  };

  return (
    <div>
      {
        //@ts-ignore
        userData.map((item, index) => (
          <div key={index}>
            <h1 className="text-2xl font-semibold flex justify-center mt-6">
              Welcome, {item.displayName}
            </h1>
            <h2 className="text-2xl font-semibold flex justify-center mt-6">
              Email - {item.email}
            </h2>
          </div>
        ))
      }

      <div className="flex justify-center mt-5">
        <button
          onClick={showReset}
          className="bg-blue-400 text-xl text-white font-bold px-2 py-1 rounded-lg mx-2"
        >
          Reset Your Password
        </button>
        <button
          onClick={showUpdate}
          className="bg-blue-400 text-xl text-white font-bold px-2 py-1 rounded-lg mx-2"
        >
          Update your Profile
        </button>
      </div>
      {reset && <ResetPassword />}
      {update && <UpdateProfile />}
    </div>
  );
};

export default Hero;
