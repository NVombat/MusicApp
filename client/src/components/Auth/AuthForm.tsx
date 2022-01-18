import { useContext, useState } from 'react';
import { useHistory, Link } from 'react-router-dom';
import AuthContext from '../../context/auth-context';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const EmailAuthForm = () => {
  const [isLogin, setIsLogin] = useState<boolean>(true);
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [authError, setAuthError] = useState<boolean>(false);
  const history = useHistory();

  const authCtx = useContext(AuthContext);

  const switchAuthModehandler = () => {
    setIsLogin((prevState) => !prevState);
  };

  const submitHandler = (event: any) => {
    event.preventDefault();
    let url;
    if (isLogin) {
      url = `https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=${process.env.REACT_APP_FIREBASE_API_KEY}`;
    } else {
      url = `https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=${process.env.REACT_APP_FIREBASE_API_KEY}`;
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
        history.replace('/profile');
        toast.success('Login successful');
        toast.success(
          'Make Sure you update your name in Update Profile Section'
        );
      })
      .catch((err) => {
        toast.error('Authentication error, please try again');
        setAuthError(true);
        setEmail('');
        setPassword('');
      });
  };

  return (
    <div>
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
              </div>
              {authError && (
                <div className="text-red-500 font-semibold my-4">
                  Authentication Error, Please Try Again
                </div>
              )}
              <div className="mt-7">
                <button
                  onClick={submitHandler}
                  className="bg-blue-500 w-full py-3 rounded-xl text-white shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105"
                >
                  {isLogin ? 'Login' : 'Register'}
                </button>
              </div>
              <Link to="/forgetpassword">
                <span className="flex justify-center mt-3 text-gray-600">
                  Forget Password?
                </span>
              </Link>

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
      <ToastContainer />
    </div>
  );
};

export default EmailAuthForm;
