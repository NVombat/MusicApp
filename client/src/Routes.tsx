import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import AuthRoute from './components/Auth/AuthRoute';
import {
  Home,
  About,
  Auth,
  Profile,
  ForgetPassword,
  PageNotFound,
  ResetPassword,
} from './pages/Index';

const Routes: React.FC = () => (
  <BrowserRouter>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/about" component={About} />
      <Route exact path="/auth" component={Auth} />
      <Route exact path="/forgetpassword" component={ForgetPassword} />
      <AuthRoute>
        <Route exact path="/profile" component={Profile} />
        <Route exact path="/resetpassword" component={ResetPassword} />
      </AuthRoute>
      <Route path="*" component={PageNotFound} />
    </Switch>
  </BrowserRouter>
);

export default Routes;
