import React, { useState } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';

const RegisterPatient = () => {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    contact_details: '',
    username: '',
    password: ''
  });

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
      const response = await axios.post('http://127.0.0.1:8000/patients/register/', formData, {
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken
        },
        withCredentials: true
      });
      console.log('Registration successful:', response.data);
    } catch (error) {
      console.error('There was an error!', error);
    }
  };

  return (
    <div className="container">
      <h2>Register Patient</h2>
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
