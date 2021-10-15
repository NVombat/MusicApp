import { useEffect, useState } from 'react';
import axios from 'axios';

import ResetPassword from './ResetPasswordForm';

const Hero = () => {
  const [userData, setUserData] = useState<any>([]);

  useEffect(() => {
    axios
      .post(`${process.env.REACT_APP_GET_USER}`, {
        idToken: localStorage.getItem('token'),
      })
      .then((res) => {
        //@ts-ignore
        setUserData(res.data.users);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <div>
        {
          //@ts-ignore
          userData.map((item, index) => (
            <ol key={index}>
              <li>{item.displayName}</li>
              <li>{item.email}</li>
            </ol>
          ))
        }
      </div>
      <ResetPassword />
    </div>
  );
};

export default Hero;
