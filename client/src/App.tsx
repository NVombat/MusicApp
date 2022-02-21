import { Switch, Route, Redirect } from 'react-router-dom';
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
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/about" exact component={About} />
        <Route path="/posts" exact component={Posts} />
        <Route path="/forgetpassword" exact component={ForgetPassword} />
        <Route path="/contact-us" exact component={ContactUs} />

        <Route path="/profile">
          {authCtx.isLoggedIn && <Profile />}
          {!authCtx.isLoggedIn && <Redirect to="/auth" />}
        </Route>
        <Route path="/record">
          {authCtx.isLoggedIn && <Record />}
          {!authCtx.isLoggedIn && <Redirect to="/auth" />}
        </Route>

        {!authCtx.isLoggedIn && <Route path="/auth" exact component={Auth} />}

        <Route path="*" component={PageNotFound} />
      </Switch>
    </Layout>
  );
};

export default App;
