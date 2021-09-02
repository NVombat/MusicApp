import Layout from '../components/shared/Layout';

import { Hero } from '../components/Profile/Index';
import firebase from 'firebase';

interface Props {}

const Profile = (props: Props) => {
  const userEmail = firebase.auth().currentUser?.email;
  // const fullName = firebase.auth().currentUser?.fullName;

  return (
    <Layout>
      <div className="flex justify-center items-center text-4xl">
        Welcome {userEmail}
      </div>
      <Hero />
    </Layout>
  );
};

export default Profile;
