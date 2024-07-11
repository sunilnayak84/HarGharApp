import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PatientProfile = () => {
  const [profileData, setProfileData] = useState(null);

  useEffect(() => {
    const fetchProfileData = async () => {
      const token = localStorage.getItem('token');
      try {
        const response = await axios.get('http://127.0.0.1:8000/patients/profile/', {
          headers: {
            'Authorization': `Token ${token}`
          }
        });
        setProfileData(response.data);
      } catch (error) {
        console.error('There was an error fetching the profile data!', error);
      }
    };

    fetchProfileData();
  }, []);

  if (!profileData) return <div>Loading...</div>;

  return (
    <div className="container">
      <h2>Patient Profile</h2>
      <p>Name: {profileData.name}</p>
      <p>Age: {profileData.age}</p>
      <p>Contact Details: {profileData.contact_details}</p>
    </div>
  );
};

export default PatientProfile;
