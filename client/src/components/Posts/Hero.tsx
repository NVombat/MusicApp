import { useState, useEffect } from 'react';
import axios from 'axios';

import Card from './Card';
import { Downlaod } from '../../utils/icons/Index';

const Hero = () => {
  const [posts, setPosts] = useState<any>([]);

  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_GET_API}`)
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
          <div className="flex justify-center items-center">
            <Card
              key={index}
              link={item.ObjectURL}
              downloadIcon={<Downlaod />}
              name={item.Name}
              filename={item.Filename}
            />
          </div>
        ))
      }
    </div>
  );
};

export default Hero;
