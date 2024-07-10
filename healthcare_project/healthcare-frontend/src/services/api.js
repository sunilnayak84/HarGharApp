import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

const registerPatient = (patientData) => {
  return axios.post(`${API_URL}/patients/register/`, patientData);
};

export { registerPatient };
