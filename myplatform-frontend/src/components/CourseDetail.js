import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import API_URL from '../api';
import Header from '../components/Header';


function CourseDetail() {
  const { id } = useParams();
  const [course, setCourse] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    phone: ''
  });
  const navigate = useNavigate();

  useEffect(() => {
    axios.get(`${API_URL}/courses/${id}/`)
      .then(response => {
        setCourse(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the course details!', error);
      });
  }, [id]);

  const handleSignUp = () => {
    if (course.status === 'free') {
      // Add the course to user's library (implementation to be added later)
      console.log('Course added to user library');
    } else {
      // Show payment form
      setShowForm(true);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log('Form submitted with data:', formData);
    // Example: send data to the server
    // axios.post(`${API_URL}/courses/${id}/enroll/`, formData)
    //   .then(response => {
    //     console.log('Enrollment successful:', response.data);
    //     navigate('/confirmation'); // Redirect to a confirmation page
    //   })
    //   .catch(error => {
    //     console.error('Error enrolling in the course:', error);
    //   });
  };

  if (!course) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Header/>
      <div className="container mt-5">
      <h1>{course.title}</h1>
      <p>{course.description}</p>
      <p><strong>Duration:</strong> {course.duration} тижнів</p>
      <p><strong>Status:</strong> {course.status}</p>
      <p><strong>Price:</strong> {course.price ? `${course.price} UAH` : 'Free'}</p>
      <button className="btn btn-primary" onClick={handleSignUp}>
        {course.status === 'free' ? 'Add to Library' : 'Sign Up'}
      </button>
      {course.status === 'premium'  && (
        <div className="mt-5">
          <h3>Payment Details</h3>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="firstName">First Name</label>
              <input
                type="text"
                id="firstName"
                name="firstName"
                className="form-control"
                value={formData.firstName}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="lastName">Last Name</label>
              <input
                type="text"
                id="lastName"
                name="lastName"
                className="form-control"
                value={formData.lastName}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                className="form-control"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="phone">Phone Number</label>
              <input
                type="tel"
                id="phone"
                name="phone"
                className="form-control"
                value={formData.phone}
                onChange={handleChange}
                required
              />
            </div>
            <button type="submit" className="btn btn-primary">Submit Payment</button>
          </form>
        </div>
      )}
    </div>
    </div>
  );
}

export default CourseDetail;
