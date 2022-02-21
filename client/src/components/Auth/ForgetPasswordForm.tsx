import { useState } from 'react';
import { useHistory } from 'react-router-dom';

const ForgetPassword = () => {
  const [email, setEmail] = useState<string>('');
  const history = useHistory();

  const forgetPasswordHandler = () => {
    fetch(
      `https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=${process.env.REACT_APP_FIREBASE_API_KEY}`,
      {
        method: 'POST',
        body: JSON.stringify({
          email: email,
          requestType: 'PASSWORD_RESET',
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      }
    )
      .then((res) => {
        if (res.ok) {
          console.log('yey');
        }
      })
      .catch((err) => {
        history.replace('/');
      });
  };
  return (
    <div className="font-sans">
      <div className="relative min-h-screen flex flex-col sm:justify-center items-center bg-gray-100 ">
        <div className="relative sm:max-w-sm w-full">
          <div className="card bg-blue-400 shadow-lg  w-full h-full rounded-3xl absolute  transform -rotate-6"></div>
          <div className="card bg-red-400 shadow-lg  w-full h-full rounded-3xl absolute  transform rotate-6"></div>
          <div className="relative w-full rounded-3xl  px-6 py-4 bg-gray-100 shadow-md">
            <label
              htmlFor=""
              className="block mt-3 text-xl font-bold text-gray-700 text-center"
            >
              Reset Password
            </label>
            <form className="mt-10" onSubmit={forgetPasswordHandler}>
              <div></div>
              <div className="mt-7">
                <label htmlFor="Email">Email</label>
                <input
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  type="email"
                  placeholder="johndoe@gmail.com"
                  className="mt-1 px-4 block w-full border-none bg-gray-100 h-11 rounded-xl shadow-lg hover:bg-blue-100 focus:bg-blue-100 focus:ring-0 focus:outline-none"
                  required
                />
              </div>
              <div className="mt-7">
                <button className="bg-blue-500 w-full my-3 py-3 rounded-xl text-white shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                  Reset Password
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ForgetPassword;
