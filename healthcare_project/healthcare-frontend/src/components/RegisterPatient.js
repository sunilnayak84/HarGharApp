import React, { useState } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
import { useNavigate } from 'react-router-dom';

const RegisterPatient = () => {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    contact_details: '',
    username: '',
    password: ''
  });
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const csrfToken = Cookies.get('csrftoken');
      const response = await axios.post('http://127.0.0.1:8000/register/', formData, {
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken
        },
        withCredentials: true
      });
      setMessage('Registration successful!');
      setTimeout(() => {
        navigate('/login'); // Redirect to login page after 2 seconds
      }, 2000);
    } catch (error) {
      setMessage('There was an error! Please try again.');
      console.error('There was an error!', error);
    }
  };

  return (
    <div className="container">
      <h2>Register Patient</h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Name</label>
          <input type="text" name="name" value={formData.name} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Age</label>
          <input type="number" name="age" value={formData.age} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Contact Details</label>
          <input type="text" name="contact_details" value={formData.contact_details} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Username</label>
          <input type="text" name="username" value={formData.username} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input type="password" name="password" value={formData.password} onChange={handleChange} className="form-control" />
        </div>
        <button type="submit" className="btn btn-primary">Register</button>
      </form>
    </div>
  );
};

export default RegisterPatient;
