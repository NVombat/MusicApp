import React from 'react';
import { Redirect } from 'react-router-dom';
import { auth } from '../../firebaseConfig';

export interface IAuthRouteProps {}

const AuthRoute: React.FunctionComponent<IAuthRouteProps> = (props) => {
  const { children } = props;

  if (!auth.currentUser) {
    return <Redirect to="/auth" />;
  }

  return <div>{children}</div>;
};

export default AuthRoute;
