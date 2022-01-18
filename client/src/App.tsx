import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from 'react-router-dom';
import { useContext } from 'react';
import {
  Home,
  Auth,
  About,
  Profile,
  ForgetPassword,
  PageNotFound,
  Posts,
  Record,
  ContactUs,
} from './pages/Index';
import { Layout } from './components/shared/index';
import AuthContext from './context/auth-context';

const App = () => {
  const authCtx = useContext(AuthContext);
  return (
    <Layout>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/posts" element={<Posts />} />
          <Route path="/forgetpassword" element={<ForgetPassword />} />
          <Route path="/contact-us" element={<ContactUs />} />

          <Route path="/profile">
            {authCtx.isLoggedIn && <Profile />}
            {!authCtx.isLoggedIn && <Navigate replace to="/auth" />}
          </Route>
          <Route path="/record">
            {authCtx.isLoggedIn && <Record />}
            {!authCtx.isLoggedIn && <Navigate replace to="/auth" />}
          </Route>

          {!authCtx.isLoggedIn && <Route path="/auth" element={<Auth />} />}

          <Route path="*" element={PageNotFound} />
        </Routes>
      </Router>
    </Layout>
  );
};

export default App;
