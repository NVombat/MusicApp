import { useContext, useState } from 'react';
import { useHistory, Link } from 'react-router-dom';
import AuthContext from '../../context/auth-context';
import { Phone, Email } from '../../utils/icons/Index';

const AuthForm = () => {
  const [isLogin, setIsLogin] = useState<boolean>(true);
  const [isPhoneAuth, setIsPhoneAuth] = useState<boolean>(false);
  const [isEmailAuth, setIsEmailAuth] = useState<boolean>(true);
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [phoneNumber, setPhoneNumber] = useState<string>('');
  const [otp, setotp] = useState<string>();
  const [authError, setAuthError] = useState<boolean>(false);
  const history = useHistory();

  const authCtx = useContext(AuthContext);

  const switchAuthModehandler = () => {
    setIsLogin((prevState) => !prevState);
  };

  const switchPhoneAuthHandler = () => {
    if (isPhoneAuth === false) {
      setIsPhoneAuth(true);
      setIsEmailAuth(false);
    }
  };

  const switchEmailAuthHandler = () => {
    if (isEmailAuth === false) {
      setIsEmailAuth(true);
      setIsPhoneAuth(false);
    }
  };

  const submitHandler = (event: any) => {
    event.preventDefault();
    let url;
    if (isLogin) {
      url = `https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyD7Q3HVTZsUp7b9jhXENrpuoqB40V0zmdw`;
    } else {
      url = `https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyD7Q3HVTZsUp7b9jhXENrpuoqB40V0zmdw`;
    }
    fetch(url, {
      method: 'POST',
      body: JSON.stringify({
        email: email,
        password: password,
        returnSecureToken: true,
      }),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          return res.json().then((data) => {
            let errorMessage = 'Authentication failed!';
            throw new Error(errorMessage);
          });
        }
      })
      .then((data) => {
        const expirationTime = new Date(
          new Date().getTime() + +data.expiresIn * 1000
        );
        //@ts-ignore
        authCtx.login(data.idToken, expirationTime.toISOString());
        history.replace('/');
      })
      .catch((err) => {
        setAuthError(true);
        setEmail('');
        setPassword('');
      });
  };

  return (
    <div className="font-sans mt-10">
      <div className="relative min-h-screen flex flex-col sm:justify-center items-center ">
        <div className="relative sm:max-w-sm w-full">
          <div className="card bg-blue-400 shadow-lg  w-full h-full rounded-3xl absolute  transform -rotate-6"></div>
          <div className="card bg-red-400 shadow-lg  w-full h-full rounded-3xl absolute  transform rotate-6"></div>
          <div className="relative w-full rounded-3xl  px-6 py-4 bg-gray-100 shadow-md">
            <label
              htmlFor=""
              className="block mt-3 text-xl font-bold text-gray-700 text-center"
            >
              {isLogin ? 'Login' : 'Register'}
            </label>
            <form className="mt-10">
              <div>
                <label htmlFor="Email">
                  {isPhoneAuth ? 'Phone number' : 'Email'}
                </label>
                {isPhoneAuth ? (
                  <input
                    value={phoneNumber}
                    onChange={(e) => setPhoneNumber(e.target.value)}
                    type="number"
                    placeholder="+91 XXXXXXXXXX"
                    className="mt-1 text-center px-4 block w-full border-none bg-gray-100 h-11 rounded-xl shadow-lg hover:bg-blue-100 focus:bg-blue-100 focus:ring-0 focus:outline-none"
                    min="0"
                    maxLength={10}
                    minLength={10}
                    required
                  />
                ) : (
                  <input
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    type="email"
                    placeholder="johndoe@gmail.com"
                    className="mt-1 px-4 block w-full border-none bg-gray-100 h-11 rounded-xl shadow-lg hover:bg-blue-100 focus:bg-blue-100 focus:ring-0 focus:outline-none"
                    required
                  />
                )}
              </div>
              <div className="mt-7">
                {isPhoneAuth ? (
                  <div>
                    <label htmlFor="Otp">OTP</label>
                    <input
                      value={otp}
                      onChange={(e) => setotp(e.target.value)}
                      type="password"
                      placeholder="X X X X"
                      className="mt-1 text-center px-4 block w-full border-none bg-gray-100 h-11 rounded-xl shadow-lg hover:bg-blue-100 focus:bg-blue-100 focus:ring-0 focus:outline-none"
                      required
                    />
                  </div>
                ) : (
                  <div>
                    <label htmlFor="Password">Password</label>
                    <input
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      type="password"
                      placeholder="********"
                      className="mt-1 px-4 block w-full border-none bg-gray-100 h-11 rounded-xl shadow-lg hover:bg-blue-100 focus:bg-blue-100 focus:ring-0 focus:outline-none"
                    />
                  </div>
                )}
              </div>
              {authError && (
                <div className="text-red-500 font-semibold my-4">
                  Authentication Error, Please Try Again
                </div>
              )}
              <div className="mt-7">
                {isEmailAuth ? (
                  <button
                    onClick={submitHandler}
                    className="bg-blue-500 w-full py-3 rounded-xl text-white shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105"
                  >
                    {isLogin ? 'Login' : 'Register'}
                  </button>
                ) : (
                  <div>
                    <button className="bg-blue-500 w-full my-3 py-3 rounded-xl text-white shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                      Get OTP
                    </button>
                    <button className="bg-blue-500 w-full my-3 py-3 rounded-xl text-white shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
                      Login
                    </button>
                  </div>
                )}
              </div>
              <Link to="/forgetpassword">Forget Password?</Link>
              <div className="flex mt-7 items-center text-center">
                <hr className="border-gray-300 border-1 w-full rounded-md" />
                <label className="block font-medium text-sm text-gray-600 w-full">
                  Login Options
                </label>
                <hr className="border-gray-300 border-1 w-full rounded-md" />
              </div>
              <div className="flex mt-7 justify-center w-full">
                <button
                  className="mr-5 bg-blue-500 border-none px-4 py-2 rounded-xl cursor-pointer text-white shadow-xl hover:shadow-inner transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105"
                  onClick={switchPhoneAuthHandler}
                >
                  <div className="flex items-center">
                    <Phone /> Phone
                  </div>
                </button>

                <button
                  className="bg-red-400 border-none px-4 py-2 rounded-xl cursor-pointer text-white shadow-xl hover:shadow-inner transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105"
                  onClick={switchEmailAuthHandler}
                >
                  <div className="flex items-center">
                    <Email /> Email
                  </div>
                </button>
              </div>
              <div className="mt-7">
                <div className="flex justify-center items-center">
                  <label className="mr-2">New User?</label>
                  <button
                    className="bg-blue-500 text-white px-4 py-1 rounded-lg"
                    onClick={switchAuthModehandler}
                  >
                    {isLogin ? 'Register' : 'Login'}
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AuthForm;
