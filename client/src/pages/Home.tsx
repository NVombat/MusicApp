import Layout from '../components/shared/Layout';
import Hero from '../components/Home/Hero';

interface Props {}

const Home = (props: Props) => {
  console.log('here');

  return (
    <Layout>
      <Hero />
    </Layout>
  );
};

export default Home;
