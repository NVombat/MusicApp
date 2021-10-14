import axios from 'axios';

const url = 'http://localhost:8000/api/uploads';

enum Inputs {
  Name = 'Name',
  Email = 'Email',
  File = 'File',
}

const Upload = () => {
  const submitForm = (e: React.FormEvent) => {
    e.preventDefault();
    let _name = (e.target as HTMLFormElement)[Inputs.Name].value;
    let _email = 'abc@gmail.com';
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
        console.log('messed up in catch block');
      });
  };

  return (
    <div>
      <h1 className="flex justify-center px-2 font-bold text-xl my-10">
        Upload
      </h1>
      <div className="relative min-h-full flex flex-col sm:justify-center items-center ">
        <div className="relative sm:max-w-sm w-full">
          <div className="card bg-blue-400 shadow-lg  w-full h-full rounded-3xl absolute  transform -rotate-6"></div>
          <div className="card bg-red-400 shadow-lg  w-full h-full rounded-3xl absolute  transform rotate-6"></div>
          <div className="relative w-full rounded-3xl  px-6 py-4 bg-gray-100 shadow-md">
            <label className="block mt-3 text-xl font-bold text-gray-700 text-center">
              Upload Media
            </label>
            <form className="mt-10" onSubmit={submitForm}>
              <div>
                <label>Name</label>
                <input
                  name={Inputs.Name}
                  type="text"
                  placeholder="John Doe"
                  className="mt-1 px-4 block w-full border-none bg-gray-100 h-11 rounded-xl shadow-lg hover:bg-blue-100 focus:bg-blue-100 focus:ring-0 focus:outline-none"
                />
              </div>
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
