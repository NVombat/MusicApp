import { useState } from 'react';
import Plus from '../../utils/icons/Plus';
import Minus from '../../utils/icons/Minus';
const Faq = () => {
  const [question, setquestion] = useState(0);
  return (
    <div className="pt-10">
      <div className="container mx-auto pt-10">
        <div className="text-center pb-3 md:pb-10">
          <h1 className="px-2 xl:px-0 text-3xl font-extrabold ">
            Frequently Asked Questions
          </h1>
        </div>
        <div className="w-10/12 mx-auto">
          <ul>
            <li className="py-6 border-gray-200 border-solid border-b">
              <div className="flex justify-between items-center">
                <h3 className="text-lg w-10/12 font-semibold">
                  How should we contact you?
                </h3>
                <div
                  className="cursor-pointer"
                  onClick={() =>
                    question === 0 ? setquestion(1) : setquestion(0)
                  }
                >
                  {question === 0 ? <Plus /> : <Minus />}
                </div>
              </div>
              {question === 0 && (
                <p className="pt-2 md:pt-3  lg:pt-5 text-gray-800 text-lg rounded-b-lg">
                  You can contact us at{' '}
                  <a
                    className="font-bold"
                    href="mailto:jvtfoundation@gmail.com"
                  >
                    jtvfoundation@gmail.com
                  </a>{' '}
                  and{' '}
                  <a className="font-bold" href="mailto:vr1movement@gmail.com">
                    vr1movement@gmail.com
                  </a>
                </p>
              )}
            </li>
            {/* <li className="py-6 border-gray-200 border-solid border-b">
              <div className="flex justify-between items-center">
                <h3 className="text-lg w-10/12 font-semibold">
                  What does lorem ipsum actually mean?
                </h3>
                <div
                  className="cursor-pointer"
                  onClick={() =>
                    question === 1 ? setquestion(2) : setquestion(1)
                  }
                >
                  {question === 1 ? <Plus /> : <Minus />}
                </div>
              </div>
              {question === 1 && (
                <p className="pt-2 md:pt-3  lg:pt-5 text-gray-800 text-lg rounded-b-lg">
                  Find the latest events updates or create events, concerts,
                  conferences, workshops, exhibitions, and cultural events in
                  all cities of the US. The aim of Eventistan is to promote
                  healthy and entertaining event. Greatest appreciation to you
                  and your team for the outstanding job you did for us. The
                  website is just what we wanted, and we were thrilled with the
                  speed your team exercised.{' '}
                </p>
              )}
            </li> */}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Faq;
