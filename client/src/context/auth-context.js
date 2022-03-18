// import React, { useState, useEffect, useCallback } from 'react';

// const AuthContext = React.createContext({
//   token: '',
//   isLoggedIn: false,
//   login: (token) => {},
//   logout: () => {},
// });

// const retrieveStoredToken = () => {
//   const storedToken = localStorage.getItem('token');
//   const storedExpirationDate = localStorage.getItem('expirationTime');

//   const remainingTime = calculateRemainingTime(storedExpirationDate);

//   if (remainingTime <= 3600) {
//     localStorage.removeItem('token');
//     localStorage.removeItem('expirationTime');
//     return null;
//   }

//   return {
//     token: storedToken,
//     duration: remainingTime,
//   };
// };

// export const AuthContextProvider = (props) => {
//   const tokenData = retrieveStoredToken();

//   let initialToken;
//   if (tokenData) {
//     initialToken = tokenData.token;
//   }

//   const [token, setToken] = useState(initialToken);

//   const userIsLoggedIn = !!token;

//   const logoutHandler = useCallback(() => {
//     setToken(null);
//     localStorage.removeItem('token');
//     localStorage.removeItem('expirationTime');

//     if (logoutTimer) {
//       clearTimeout(logoutTimer);
//     }
//   }, []);

//   const loginHandler = (token, expirationTime) => {
//     setToken(token);
//     localStorage.setItem('token', token);
//     localStorage.setItem('expirationTime', expirationTime);

//     const remainingTime = calculateRemainingTime(expirationTime);

//     logoutTimer = setTimeout(logoutHandler, remainingTime);

//   };

//   useEffect(() => {
//     if (tokenData) {
//       logoutTimer = setTimeout(logoutHandler, tokenData.duration);
//     }
//   }, [tokenData, logoutHandler]);

//   const contextValue = {
//     token: token,
//     isLoggedIn: userIsLoggedIn,
//     login: loginHandler,
//     logout: logoutHandler,
//   };

import React, { createContext, useState, useEffect } from 'react';
import jwt_decode from 'jwt-decode'; // this package is used to decode the token and give back the object !
import { useHistory } from 'react-router-dom';

const AuthContext = React.createContext({
  token: 'access_token' && 'refresh_token', // check weather this is right or wrong !!!
  loginUser: false,
  login: (token) => {},
  logout: () => {},
});

export const AuthProvider = ({ children }) => {
  let [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem('authTokens')
      ? JSON.parse(localStorage.getItem('authTokens'))
      : null
  ); // here we can access the authTokens
  let [user, setUser] = useState(() =>
    localStorage.getItem('authTokens')
      ? jwt_decode(localStorage.getItem('authTokens'))
      : null
  );
  //let [loading, setLoading] = useState(true);

  const history = useHistory();
  let logoutTimer;

  // this function should take 2 arguements, access and refresh tokens
  // set these tokens in localstorage
  // check for expiration time
  // logic for logout timer

  const calculateRemainingTime = (expirationTime) => {
    const currentTime = new Date().getTime();
    const adjExpirationTime = new Date(expirationTime).getTime();

    const remainingDuration = adjExpirationTime - currentTime;

    return remainingDuration;
  };

  let loginUser = (access_token, refresh_token) => {
    setAuthTokens(access_token, refresh_token);
    localStorage.setItem('access_token', access_token);
    localStorage.setItem('refresh_token', refresh_token);
    let oneHrs = 1000 * 60 * 60;
    const remainingTime = calculateRemainingTime(oneHrs);

    logoutTimer = setTimeout(logoutUser, remainingTime);
  };

  // let loginUser = async (e) => {
  //   e.preventDefault();
  //   let response = await fetch(`${process.env.REACT_APP_FETCH_URL}`, {
  //     method: 'POST',
  //     headers: {
  //       'Content-Type': 'application/json',
  //       Authorization: 'Bearer ' + toString(authTokens.access_token),
  //     },
  //     body: JSON.stringify({
  //       email: e.target.email.value,
  //       password: e.target.password.value,
  //     }),
  //   });
  //   let data = await response.json();

  //   if (response.status === 200) {
  //     // this is the check code !! 🤞
  //     setAuthTokens(data);
  //     console.log(authTokens);
  //     setUser(jwt_decode(data.access_token));
  //     localStorage.setItem('authTokens', JSON.stringify(data)); // here is the code that will be used to storedToken
  //     history.replace('/profile'); // this will send the user to the profile page the moment he logs in
  //   } else {
  //     alert('Something went wrong!');
  //   }
  // };

  //logout condition -
  // 1. There is no token (both refresh and access) && there is no expiration
  // 2. The expiration time is up

  //logic for logout
  //1. clear the localstorage on logout button press

  let logoutUser = () => {
    // this is for the time we are logged out
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem('authTokens');
    history.replace('/login');
  };

  const updateToken = async () => {
    let response = await fetch(`${process.env.REACT_APP_FETCH_URL}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer ' + toString(authTokens.refresh_token),
      },
      body: JSON.stringify({ refresh_token: authTokens.refresh_token }),
    });

    let data = await response.json();

    if (response.status === 200) {
      setAuthTokens(data);
      setUser(jwt_decode(data.access_token));
      localStorage.setItem('authTokens', JSON.stringify(data));
    } else {
      logoutUser();
    }

    //   if (loading) {
    //     setLoading(false);
    //   }
  };

  let contextData = {
    // here we can access the data from the server
    user: user,
    authTokens: authTokens,
    loginUser: loginUser,
    logoutUser: logoutUser,
  };

  useEffect(() => {
    // if (loading) {
    //   updateToken();
    // }

    let oneHrs = 1000 * 60 * 60;

    let interval = setInterval(() => {
      if (authTokens) {
        updateToken();
      }
    }, oneHrs);
    return () => clearInterval(interval);
  }, [authTokens]);

  return (
    <AuthContext.Provider value={contextData}>{children}</AuthContext.Provider>
  );
};

export default AuthContext;
