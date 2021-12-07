import { useState } from 'react';
import { useHistory } from 'react-router';
import axios from 'axios';

const Form = () => {
  const [name, setName] = useState<String>('');
  const [email, setEmail] = useState<String>('');
  const [message, setMessage] = useState<String>('');

  const history = useHistory();

  const formSubmitHandler = () => {
    axios
      .post(`${process.env.REACT_APP_POST_CONTACTUS_DATA}`, {
        name: name,
        email: email,
        message: message,
      })
      .then((res) => {
        history.push('/');
      })
      .catch((err) => alert('Something went wrong, please try again'));
  };

  return (
    <div>
      <form
        className="text-gray-700 body-font relative"
        onSubmit={formSubmitHandler}
      >
        <div className="container px-5 pb-24 mx-auto">
          <div className="lg:w-1/2 md:w-2/3 mx-auto">
            <div className="flex flex-wrap -m-2">
              <div className="p-2 w-1/2">
                <div className="relative">
                  <label className="leading-7 text-sm text-gray-600">
                    Name
                  </label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    className="w-full bg-gray-100 rounded border border-gray-300 focus:border-blue-400 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                    onChange={(e) => setName(e.target.value)}
                    required
                  />
                </div>
              </div>
              <div className="p-2 w-1/2">
                <div className="relative">
                  <label className="leading-7 text-sm text-gray-600">
                    Email
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    className="w-full bg-gray-100 rounded border border-gray-300 focus:border-blue-400 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>
              </div>
              <div className="p-2 w-full">
                <div className="relative">
                  <label className="leading-7 text-sm text-gray-600">
                    Message
                  </label>
                  <textarea
                    id="message"
                    name="message"
                    className="w-full bg-gray-100 rounded border border-gray-300 focus:border-blue-400 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
                    onChange={(e) => setMessage(e.target.value)}
                    required
                  ></textarea>
                </div>
              </div>
              <div className="p-2 w-full">
                <button className="flex mx-auto text-white bg-blue-400 border-0 py-2 px-8 focus:outline-none hover:bg-blue-600 rounded text-lg">
                  Submit
                </button>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  );
};

export default Form;