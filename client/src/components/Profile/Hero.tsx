import { useEffect, useState } from 'react';
import axios from 'axios';

import ResetPassword from './ResetPasswordForm';

const getUserDataURL = `https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=${process.env.REACT_APP_FIREBASE_API_KEY}`;

const Hero = () => {
  const [userData, setUserData] = useState<any>([]);
  const [reset, setReset] = useState<boolean>(false);

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
  };

  return (
    <div>
      {
        //@ts-ignore
        userData.map((item, index) => (
          <div>
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
          className="bg-blue-400 text-xl text-white font-bold px-2 py-1 rounded-lg"
        >
          Reset Your Password
        </button>
      </div>
      {reset && <ResetPassword />}
    </div>
  );
};

export default Hero;
