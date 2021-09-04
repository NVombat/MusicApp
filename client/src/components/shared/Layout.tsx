import { Navbar } from './Navbar';
import { Footer } from './Footer';
import { LayoutProps } from '../../utils/interfaces';

const Layout = (props: LayoutProps) => {
  return (
    <div>
      <Navbar />
      <div className="min-h-screen">{props.children}</div>
      <Footer />
    </div>
  );
};

export default Layout;
