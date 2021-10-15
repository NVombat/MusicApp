import { useEffect, useState } from 'react';
import axios from 'axios';

const url = 'http://localhost:8000/api/uploads';

enum Inputs {
  File = 'File',
}

const Upload = () => {
  const [userData, setUserData] = useState<any>([]);
  const [name, setName] = useState<string>('');
  const [email, setEmail] = useState<string>('');

  useEffect(() => {
    axios
      .post(`${process.env.REACT_APP_GET_USER}`, {
        idToken: localStorage.getItem('token'),
      })
      .then((res) => {
        //@ts-ignore
        setUserData(res.data.users);
        //@ts-ignore
        userData.map((user) => {
          setEmail(user.email);
          setName(user.displayName);
        });
        console.log(typeof userData);

        console.log('email:', email, 'name:', name);
      })
      .catch((err) => console.log(err));
  }, []);

  const submitForm = (e: React.FormEvent) => {
    e.preventDefault();

    let _name = name;
    // Enter Dynamic Email option
    let _email = email;
    let _file = (e.target as HTMLFormElement)[Inputs.File].files[0];
    const finalFormData = new FormData();

    finalFormData.append('Name', _name);
    finalFormData.append('Email', _email);
    finalFormData.append('File', _file);
    finalFormData.append('Filename', _file.name);

    axios
      .post(url, finalFormData)
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err, err?.response);
        console.log('in catch block');
      });
  };

  return (
    <div>
      <div className="relative min-h-full flex flex-col sm:justify-center items-center mt-10">
        <div className="relative sm:max-w-sm w-full">
          <div className="card bg-blue-400 shadow-lg  w-full h-full rounded-3xl absolute  transform -rotate-6"></div>
          <div className="card bg-red-400 shadow-lg  w-full h-full rounded-3xl absolute  transform rotate-6"></div>
          <div className="relative w-full rounded-3xl  px-6 py-4 bg-gray-100 shadow-md">
            <label className="block mt-3 text-xl font-bold text-gray-700 text-center">
              Upload Media
            </label>
            <form className="mt-10" onSubmit={submitForm}>
              <div className="mt-7">
                <div>
                  <label>Choose File</label>
                  <input
                    name={Inputs.File}
                    type="file"
                    placeholder="John Doe"
                    className="mt-1 px-4 block"
                    required
                  />
                </div>
              </div>
              <div className="mt-7">
                <button
                  type="submit"
                  className="bg-blue-500 w-full py-3 rounded-xl text-white shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105"
                >
                  Upload
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Upload;
