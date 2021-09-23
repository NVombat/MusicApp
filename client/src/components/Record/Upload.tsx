const Upload = () => {
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
            <label
              htmlFor=""
              className="block mt-3 text-xl font-bold text-gray-700 text-center"
            >
              Upload Media
            </label>
            <form className="mt-10">
              <div>
                <label htmlFor="Email">Name</label>
                <input
                  type="text"
                  placeholder="John Doe"
                  className="mt-1 px-4 block w-full border-none bg-gray-100 h-11 rounded-xl shadow-lg hover:bg-blue-100 focus:bg-blue-100 focus:ring-0 focus:outline-none"
                  required
                />
              </div>
              <div className="mt-7">
                <div>
                  <label htmlFor="upload-file">Choose File</label>
                  <input
                    type="file"
                    placeholder="John Doe"
                    className="mt-1 px-4 block"
                    required
                  />
                </div>
              </div>
              <div className="mt-7">
                <button className="bg-blue-500 w-full py-3 rounded-xl text-white shadow-xl hover:shadow-inner focus:outline-none transition duration-500 ease-in-out  transform hover:-translate-x hover:scale-105">
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
