import Layout from '../components/shared/Layout';
import TopHeader from '../components/About/TopHeader';
import Team from '../components/About/Team';
import Faq from '../components/About/Faq';

const About = () => {
  return (
    <Layout>
      <TopHeader />
      <Team />
      <Faq />
    </Layout>
  );
};

export default About;
