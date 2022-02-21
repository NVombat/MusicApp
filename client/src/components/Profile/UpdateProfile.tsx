import React, { useState, useContext } from 'react';
import { useHistory } from 'react-router-dom';

import AuthContext from '../../context/auth-context';

const UpdateProfile = () => {
  const [name, setName] = useState<string>('');
  const authCtx = useContext(AuthContext);
  const history = useHistory();

  const updateProfileAPI = `https://identitytoolkit.googleapis.com/v1/accounts:update?key=${process.env.REACT_APP_FIREBASE_API_KEY}`;

  const submitHandler = (e: React.FormEvent) => {
    e.preventDefault();

    fetch(updateProfileAPI, {
      method: 'POST',
      body: JSON.stringify({
        idToken: authCtx.token,
        displayName: name,
        returnSecureToken: true,
      }),
    })
      .then((res) => {
        history.replace('/');
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div>
      <div className="font-sans">
        <div className="relative mt-16 flex flex-col sm:justify-center items-center ">
          <div className="relative sm:max-w-sm w-full">
            <div className="card bg-blue-400 shadow-lg  w-full h-full rounded-3xl absolute  transform -rotate-6"></div>
            <div className="card bg-red-400 shadow-lg  w-full h-full rounded-3xl absolute  transform rotate-6"></div>
            <div className="relative w-full rounded-3xl  px-6 py-4 bg-gray-100 shadow-md">
              <label
                htmlFor=""
                className="block mt-3 text-xl font-bold text-gray-700 text-center"
              >
                Update Profile
              </label>
              <form className="mt-10" onSubmit={submitHandler}>
                <div></div>
                <div className="mt-7">
                  <label>Name</label>
                  <input
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    type="text"
                    placeholder="John Doe"
                    className="mt-1 px-4 block w-full border-none bg-gray-100 h-11 rounded-xl shadow-lg hover:bg-blue-100 focus:bg-blue-100 focus:ring-0 focus:outline-none"
                    required
                  />
                </div>
                <div className="mt-7">
                  <button className="bg-blue-500 w-full my-3 py-3 rounded-xl text-white shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                    Update
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UpdateProfile;
