const Video = () => {
  return (
    <div>
      <h1 className="flex justify-center my-3 text-2xl font-semibold">
        VR1 - HERE WE ARE ALL ONE
      </h1>
      <iframe
        width="560"
        height="315"
        src="https://www.youtube.com/embed/DvmQzFFLY1c"
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      ></iframe>
    </div>
  );
};

export default Video;
