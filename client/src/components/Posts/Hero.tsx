import { useState, useEffect } from 'react';
import axios from 'axios';
import Card from './Card';
import { Downlaod } from '../../utils/icons/Index';
import ReactAudioPlayer from 'react-audio-player';
const Hero = () => {
  const [posts, setPosts] = useState<any>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [hasNextPage, setHasNextPage] = useState<boolean>(false);
  const [hasPreviousPage, setHasPreviousPage] = useState<boolean>(false);

  useEffect(() => {
    axios({
      method: 'GET',
      url: `${process.env.REACT_APP_GET_API}`,
      params: {
        Page: currentPage,
      },
    })
      .then((res: any) => {
        setPosts(res.data.data);
        setCurrentPage(res.data.currentPage);
        setHasNextPage(res.data.hasNextPage);
        setHasPreviousPage(res.data.hasPreviousPage);
      })
      .catch((err: any) => {
        console.log(err);
      });
  }, [currentPage, hasNextPage, hasPreviousPage]);

  return (
    <div>
      <span className="flex justify-center mt-5 text-2xl font-semibold">
        Posts
      </span>

      {posts.length === 0 && (
        <div className="flex justify-center items-center font-bold text-3xl md:my-4">
          No Posts Available
        </div>
      )}
      {
        //@ts-ignore
        posts.map((item, index) => (
          <div key={index} className="flex gap-4 justify-center items-center m-3">
            {/* <Card
              link={item.ObjectURL}
              downloadIcon={<Downlaod />}
              filename={item.Filename}
            /> */}
            <ReactAudioPlayer
              src={item.ObjectURL}
              controls
            />
            
        
      
          </div>
        ))
      }
      <div className="flex justify-center items-center">
        {hasPreviousPage && (
          <button
            onClick={() => setCurrentPage(currentPage - 1)}
            className="bg-blue-400 text-white text-2xl font-semibold text-center px-2 py-1 mx-3 my-3 rounded-lg"
          >
            Prev
          </button>
        )}
        {hasNextPage && (
          <button
            onClick={() => setCurrentPage(currentPage + 1)}
            className="bg-blue-400 text-white text-2xl font-semibold text-center px-2 py-1 mx-3 rounded-lg"
          >
            Next
          </button>
        )}
      </div>
    </div>
  );
};

export default Hero;
