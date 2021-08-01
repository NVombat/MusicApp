import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/shared/Navbar';
import { Home, Auth, Profile, PageError } from './Pages/Index';

const App = () => {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path='/' exact component={Home} />
        <Route path='/auth' exact component={Auth} />
        <Route path='/profile' exact component={Profile} />
        <Route path='*' exact component={PageError} />
      </Switch>
    </Router>
  );
};

export default App;
