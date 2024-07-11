import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import RegisterPatient from './components/RegisterPatient';
import Login from './components/Login';
import PatientProfile from './components/PatientProfile';


const App = () => {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <Link className="navbar-brand" to="/">Healthcare App</Link>
          <div className="collapse navbar-collapse">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item">
                <Link className="nav-link" to="/register">Register</Link>
              </li>
            </ul>
          </div>
        </nav>
        <Routes>
        <Route path="/register" element={<RegisterPatient />} />
        <Route path="/login" element={<Login />} />
        <Route path="/profile" element={<PatientProfile />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
