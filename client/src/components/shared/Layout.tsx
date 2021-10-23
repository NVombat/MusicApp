import { Navbar, Footer } from './index';
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
