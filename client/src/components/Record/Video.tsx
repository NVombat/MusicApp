const Video = () => {
  return (
    <div>
      <h1 className="flex justify-center my-3 text-2xl font-semibold">
        We Are One Song
      </h1>
      <iframe
        width="560"
        height="315"
        src="https://www.youtube.com/embed/rYLHFMjNZjo"
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      ></iframe>
    </div>
  );
};

export default Video;
