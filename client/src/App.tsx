import { Switch, Route, Redirect } from 'react-router-dom';
import { useContext } from 'react';
import {
  Home,
  Auth,
  About,
  Profile,
  ForgetPassword,
  PageNotFound,
} from './pages/Index';
import Layout from './components/shared/Layout';
import AuthContext from './context/auth-context';

const App = () => {
  const authCtx = useContext(AuthContext);
  return (
    <Layout>
      <Switch>
        <Route path="/" exact component={Home} />
        {!authCtx.isLoggedIn && <Route path="/auth" exact component={Auth} />}
        <Route path="/forgetpassword" exact component={ForgetPassword} />
        <Route path="/about" exact component={About} />
        <Route path="/profile">
          {authCtx.isLoggedIn && <Profile />}
          {!authCtx.isLoggedIn && <Redirect to="/auth" />}
        </Route>

        <Route path="*" component={PageNotFound} />
      </Switch>
    </Layout>
  );
};

export default App;
