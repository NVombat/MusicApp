import { Navbar } from './Navbar';
import { Footer } from './Footer';
import { LayoutProps } from '../../utils/interfaces';

const Layout = (props: LayoutProps) => {
  return (
    <div>
      <Navbar />
      {props.children}
      <Footer />
    </div>
  );
};

export default Layout;
