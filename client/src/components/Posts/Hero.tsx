import { useState, useEffect } from 'react';
import axios from 'axios';

const url = 'http://localhost:8000/api/posts';

const Hero = () => {
  const [posts, setPosts] = useState<any>([]);

  useEffect(() => {
    axios
      .get(url)
      .then((res) => {
        console.log('axios response', res.data);
        console.log('type of axios data', typeof res.data);
        setPosts(res.data);
      })
      .catch((err) => console.log(err, err?.response));
  }, []);

  return (
    <div>
      <span className="flex justify-center mt-5 text-2xl font-semibold">
        Posts
      </span>

      {
        //@ts-ignore
        posts.map((item, index) => (
          <li key={index}>
            <ol>{item.Name}</ol>
            <ol>{item.Email}</ol>
            <ol>{item.Filename}</ol>
            <ol>{item.CloudFilename}</ol>
            <a href={item.ObjectURL}>Download</a>
          </li>
        ))
      }
    </div>
  );
};

export default Hero;
