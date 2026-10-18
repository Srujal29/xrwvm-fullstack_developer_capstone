import React, { useState } from "react";
import "./Register.css";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const registeruser = async (e) => {
    e.preventDefault();
    let register_url = window.location.origin + "/djangoapp/register";

    const res = await fetch(register_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userName: userName,
        password: password,
        firstName: firstName,
        lastName: lastName,
        email: email,
      }),
    });

    const json = await res.json();
    if (json.status === "Authenticated") {
      window.location.href = window.location.origin;
    } else {
      alert("Registration failed");
    }
  };

  return (
    <div className="register_container">
      <h2>Sign-Up</h2>
      <form onSubmit={registeruser}>
        <div className="input_panel">
          <label>Username</label>
          <input
            type="text"
            name="username"
            placeholder="Username"
            className="input_field"
            onChange={(e) => setUserName(e.target.value)}
            required
          />
        </div>
        <div className="input_panel">
          <label>First Name</label>
          <input
            type="text"
            name="first_name"
            placeholder="First Name"
            className="input_field"
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </div>
        <div className="input_panel">
          <label>Last Name</label>
          <input
            type="text"
            name="last_name"
            placeholder="Last Name"
            className="input_field"
            onChange={(e) => setLastName(e.target.value)}
            required
          />
        </div>
        <div className="input_panel">
          <label>Email</label>
          <input
            type="email"
            name="email"
            placeholder="Email"
            className="input_field"
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="input_panel">
          <label>Password</label>
          <input
            type="password"
            name="password"
            placeholder="Password"
            className="input_field"
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div>
          <input className="submit_button" type="submit" value="Register" />
        </div>
      </form>
    </div>
  );
};

export default Register;